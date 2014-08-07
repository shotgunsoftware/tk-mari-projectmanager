# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
Manage project creation in a Toolkit aware fashion
"""

import sgtk
from sgtk import TankError
from sgtk.platform.qt import QtGui

import os
import mari

from new_project_form import NewProjectForm

class ProjectManager(object):
    """
    """
    
    def __init__(self, app):
        """
        Construction
        """
        self._app = app
        
    def create_new_project(self, name, sg_publish_data):
        """
        Create a new project in the current Toolkit context and seed it
        with the specified geometry
        
        :param name:                The name to use in the project_name template when 
                                    generating the project name
        :param sg_publish_data:     List of the initial geometry publishes to load for 
                                    into the new project.  Each entry in the list is a
                                    Shotgun entity dictionary
        :returns:                   The new Mari project instance if successful or None 
                                    if not
        :raises:                    TankError if something went wrong at any stage!
        """
        # create the project name:
        project_name = None
        try:
            name_template = self._app.get_template("template_new_project_name")
            fields = self._app.context.as_template_fields(name_template)
            if name:
                fields["name"] = name
            project_name = name_template.apply_fields(fields)
        except TankError, e:
            raise TankError("Failed to create name for the new project: %s" % e)
        
        # check that a project with this name doesn't already exist:
        if project_name in mari.projects.names():
            raise TankError("Unable to create project as a project called '%s' already exists!" % project_name)
        
        # extract the file paths for the list of geometry publishes:
        # (TODO) - move this to use a centralized method in core
        class PublishedGeomDetails(object):
            def __init__(self, path, sg_publish):
                self.path = path
                self.sg_publish = sg_publish

        publishes_to_load = []
        for sg_publish in sg_publish_data:
            path = sg_publish.get("path", {}).get("local_path")
            if not path or not os.path.exists(path):
                self._app.log_warning("Publish '%s' couldn't be found on disk, skipping!" % path)
            publishes_to_load.append(PublishedGeomDetails(path, sg_publish))
        
        using_placeholder = False
        if not publishes_to_load:
            #raise TankError("Must select at least one valid geometry publish in order to create a new project!")
            # use placeholder geom instead:
            placeholder_alembic = os.path.join(os.path.dirname(__file__), "..", "..", "resources", "placeholder.abc")
            publishes_to_load.append(PublishedGeomDetails(placeholder_alembic, None))
            using_placeholder = True
        
        # close existing project if it's open:
        if mari.projects.current():
            mari.projects.close()
            if mari.projects.current():
                # the user cancelled and the project wasn't closed
                return
        
        # lets use default channels:
        empty_channels = []

        # define the options to be used for the geometry import:
        # (TODO) - move this to a hook?
        geometry_load_options = {}
        geometry_load_options["MappingScheme"] = mari.projects.UV_OR_PTEX
        geometry_load_options["CreateSelectionSets"] = mari.geo.SELECTION_GROUPS_CREATE_FROM_FACE_GROUPS
        geometry_load_options["MergeType"] = mari.geo.MERGETYPE_JUST_MERGE_NODES

        # create the project with the first geometry specified:
        try:
            self._app.log_debug("Creating a new project called: %s" % project_name)
            mari.projects.create(project_name, publishes_to_load[0].path, 
                                 empty_channels, empty_channels, 
                                 geometry_load_options)
        except Exception, e:
            raise TankError("Failed to create new project: %s" % e)

        # make sure that the current project is the one we created:
        new_project = mari.projects.current()
        if not new_project or new_project.name() != project_name:
            raise TankError("Newly created project '%s' wasn't opened!" % project_name)
        
        # add metadata to the project so that we can track the context:
        self.set_project_metadata(new_project, self._app.context)        
        
        if using_placeholder:
            return new_project
        
        # update the metadata, name and version on the loaded geometry:
        for geo in mari.geo.list():
            self.__init_published_geo(geo, publishes_to_load[0].path, publishes_to_load[0].sg_publish)
        
        # finally, load in any additional geometry that was selected:
        for published_geo in publishes_to_load[1:]:
            # load the geo from the file:
            new_geo = mari.geo.load(published_geo.path, options = geometry_load_options)
            
            # and init the geo so it's tracked by Toolkit:
            for geo in new_geo:
                self.__init_published_geo(geo, published_geo.path, published_geo.sg_publish)
             
        return new_project
        
        
    def show_new_project_dialog(self):
        """
        """
        res, new_project_form = self._app.engine.show_modal("Start New Project", self._app, NewProjectForm, 
                                                            self._init_new_project_form)
        
    def _init_new_project_form(self, new_project_form):
        """
        """
        # connect to signals:
        new_project_form.create_project.connect(self._on_create_new_project)
        
    def _on_create_new_project(self, new_project_form):
        """
        """
        try:
            name = new_project_form.project_name
            sg_publish_data = []
            
            # (AD) - TEMP!!
            #if not sg_publish_data:
            #    sg_publish_data.append({'version_number': 16,
            #                            'task': {'type': 'Task', 'id': 230, 'name': 'Animation'},
            #                            'entity': {'type': 'Shot', 'id': 914, 'name': '123'},
            #                            'project': {'type': 'Project', 'id': 67, 'name': 'Another Demo Project'},
            #                            'id': 1814, 
            #                            'path': {'local_path': '/tank_testbed/another_demo_project/sequences/Sequence-01/123/Anm/publish/caches/scene.v016.abc'}, 
            #                            'name': 'scene'})
            
            if self.create_new_project(name, sg_publish_data):
                new_project_form.close()
        except TankError, e:
            QtGui.QMessageBox.information(new_project_form, "Failed to create new project!", "%s" % e)
        except Exception, e:
            QtGui.QMessageBox.information(new_project_form, "Failed to create new project!", "%s" % e)
            self._app.log_exception("Failed to create new project!")


    def __init_published_geo(self, geo, path, sg_publish_data):
        """
        """
        publish_name = sg_publish_data.get("name")
        sg_project = sg_publish_data.get("project")            
        sg_entity = sg_publish_data.get("entity")
        sg_task = sg_publish_data.get("task")

        # set the geo name and metadata:            
        if not publish_name:
            # if not then fall back to the first part of the file name:
            publish_name = os.path.basename(path).split(".")[0]
        geo.setName(publish_name)
        self.set_geo_metadata(geo, sg_project, sg_entity, sg_task)
        
        # there should be a single version for the geo:
        geo_versions = geo.versionList()
        if len(geo_versions) != 1:
            raise TankError("Invalid number of version found for newly imported geometry "
                            "- expected 1 but found %d!" % len(geo_versions))
        
        self.__init_published_geo_version(geo_versions[0], path, sg_publish_data)

    def __init_published_geo_version(self, geo_version, path, sg_publish_data):
        """
        """
        sg_publish_id = sg_publish_data.get("id")
        sg_version = sg_publish_data.get("version_number")
        
        # set geo_version name:
        geo_version_name = "v%03d" % (sg_version or 0)
        if geo_version.name() != geo_version_name:
            geo_version.setName(geo_version_name)
            
        # and store metadata:
        self.set_geo_version_metadata(geo_version, path, sg_publish_id, sg_version)


    PROJECT_METADATA_INFO = {
        "project_id":{"display_name":"Shotgun Project Id", "visible":False},
        "entity_type":{"display_name":"Shotgun Entity Type", "visible":False, "default_value":""},
        "entity_id":{"display_name":"Shotgun Entity Id", "visible":False},
        "step_id":{"display_name":"Shotgun Step Id", "visible":False},
        "task_id":{"display_name":"Shotgun Task Id", "visible":False}
    }

    def set_project_metadata(self, mari_project, ctx):
        """
        Set the Toolkit metadata on a geo so that we can track where it came from
        """
        metadata = {}
        metadata["project_id"] = ctx.project["id"]
        if ctx.entity:
            metadata["entity_type"] = ctx.entity["type"]
            metadata["entity_id"] = ctx.entity["id"]
        if ctx.step:
            metadata["step_id"] = ctx.step["id"]
        if ctx.task:
            metadata["task_id"] = ctx.task["id"]
            
        self.set_metadata(mari_project, metadata, ProjectManager.PROJECT_METADATA_INFO)

    def get_project_metadata(self, mari_project):
        """
        """
        return self.get_metadata(mari_project, ProjectManager.PROJECT_METADATA_INFO)

    GEO_METADATA_INFO = {
        "project_id":{"display_name":"Shotgun Project Id", "visible":False},
        "project":{"display_name":"Shotgun Project", "visible":True, "default_value":""},
        "entity_type":{"display_name":"Shotgun Entity Type", "visible":False, "default_value":""},
        "entity_id":{"display_name":"Shotgun Entity Id", "visible":False},
        "entity":{"display_name":"Shotgun Entity", "visible":True, "default_value":""},
        "task_id":{"display_name":"Shotgun Task Id", "visible":False},
        "task":{"display_name":"Shotgun Task", "visible":True, "default_value":""}
    }

    def set_geo_metadata(self, geo, project, entity, task):
        """
        Set the Toolkit metadata on a geo so that we can track where it came from
        """
        metadata_info = ProjectManager.GEO_METADATA_INFO.copy()
        
        # define the metadata we want to store:
        metadata = {}
        if project:
            metadata["project_id"] = project["id"]
            metadata["project"] = project.get("name")
        if entity:
            metadata_info["entity"]["display_name"] = "Shotgun %s" % entity.get("type") or "Entity"
            metadata["entity_type"] = entity["type"]
            metadata["entity_id"] = entity["id"]
            metadata["entity"] = entity.get("name")
        if task:
            metadata["task_id"] = task["id"]
            metadata["task"] = task["name"] 
        
        self.set_metadata(geo, metadata, metadata_info)
    
    def get_geo_metadata(self, geo):
        """
        """
        return self.get_metadata(geo, ProjectManager.GEO_METADATA_INFO)    
    
    GEO_VERSION_METADATA_INFO = {
        "path":{"display_name":"Shotgun Project Id", "visible":True, "default_value":""},
        "publish_id":{"display_name":"Shotgun Project", "visible":True},
        "version":{"display_name":"Shotgun Entity Type", "visible":True}
    }

    def set_geo_version_metadata(self, geo_version, path, publish_id, version):
        """
        Set the Toolkit metadata on a geo so that we can track where it came from
        """
        # define the metadata we want to store:
        metadata = {"path":path, "publish_id":publish_id,"version":version}
        
        self.set_metadata(geo_version, metadata, ProjectManager.GEO_VERSION_METADATA_INFO)
    
    def get_geo_version_metadata(self, geo_version):
        """
        """
        return self.get_metadata(geo_version, ProjectManager.GEO_VERSION_METADATA_INFO)     
    
    def set_metadata(self, obj, metadata, md_details):
        """
        """
        for name, details in md_details.iteritems():
            value = metadata.get(name, details.get("default_value"))
            if value == None:
                continue

            md_name = "tk_%s" % name
            
            obj.setMetadata(md_name, value)
            if "display_name" in details:
                obj.setMetadataDisplayName(md_name, details["display_name"])
                
            flags = obj.METADATA_SAVED
            visible = details.get("visible", True)
            if visible:
                flags |= obj.METADATA_VISIBLE
            obj.setMetadataFlags(md_name, flags)

    def get_metadata(self, obj, md_details):
        """
        """
        metadata = {}
        for name, _ in md_details:
            md_name = "tk_%s" % name
            if obj.hasMetadata(md_name):
                metadata[name] = obj.metadata(md_name)
        return metadata

    """
    print "---------------"
    print "Project:"
    print mari.projects.current().metadata("tk_project_id")
    print mari.projects.current().metadata("tk_entity_type")
    print mari.projects.current().metadata("tk_entity_id")
    print mari.projects.current().metadata("tk_step_id")
    print mari.projects.current().metadata("tk_task_id")
    print "---------------"
    print "Geo:"
    for geo in mari.geo.list():
        print "   %s" % geo.name()
        print "   - %s" % geo.metadata("tk_project_id")
        print "   - %s" % geo.metadata("tk_project")
        print "   - %s" % geo.metadata("tk_entity_type")
        print "   - %s" % geo.metadata("tk_entity_id")
        print "   - %s" % geo.metadata("tk_entity")
        print "   - %s" % geo.metadata("tk_task_id")
        print "   - %s" % geo.metadata("tk_task")
    
        print "   ---------------"
        print "   Versions:"
        for geo_version in geo.versionList():
            print "     %s" % geo_version.name()
            print "     - %s" % geo_version.metadata("tk_path")
            print "     - %s" % geo_version.metadata("tk_publish_id")
            print "     - %s" % geo_version.metadata("tk_version")
    """












        
    
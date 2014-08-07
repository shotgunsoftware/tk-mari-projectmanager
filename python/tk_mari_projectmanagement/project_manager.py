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

from new_project_form import NewProjectForm

class ProjectManager(object):
    """
    """
    
    @staticmethod
    def start_new_project_ui():
        """
        """
        app = sgtk.platform.current_bundle()
        project_mngr = ProjectManager(app)
        project_mngr.show_new_project_dialog()
    
    def __init__(self, app):
        """
        Construction
        """
        self._app = app
        
    def show_new_project_dialog(self):
        """
        """
        new_project_form = self._app.engine.show_dialog("New Project", self._app, NewProjectForm)
        
        # connect to signals:
        new_project_form.create_project.connect(self._on_create_new_project)
        
    def _on_create_new_project(self, new_project_form):
        """
        """
        self._app.log_info("Creating project!")
        
    
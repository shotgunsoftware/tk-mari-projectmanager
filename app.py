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
Project management app for Mari that augments Mari's own project management 
functionality so that projects are Toolkit aware
"""

from sgtk.platform import Application

class MariProjectManagement(Application):
    """
    The main app instance
    """

    def init_app(self):
        """
        Called as the app is being initialized
        """
        self.log_debug("%s: Initializing..." % self)
    
        # register the start new project command:
        self.engine.register_command("New Project...", self.start_new_project_ui)

    def destroy_app(self):
        """
        Called when the app is being destroyed
        """
        self.log_debug("%s: Destroying..." % self)

    def start_new_project_ui(self):
        """
        Show the start new project UI
        """
        tk_mari_projectmanagement = self.import_module("tk_mari_projectmanagement")
        tk_mari_projectmanagement.ProjectManager.start_new_project_ui()




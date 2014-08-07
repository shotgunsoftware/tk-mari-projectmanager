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

    def init_app(self):
        """
        Called as the application is being initialized
        """

        tk_mari_projectmanagement = self.import_module("tk_mari_projectmanagement")
        #cb = lambda : tk_multi_breakdown.show_dialog(self)
        #self.engine.register_command("Scene Breakdown...", cb, { "short_name": "breakdown" })




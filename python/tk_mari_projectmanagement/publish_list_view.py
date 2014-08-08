# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

import os
from datetime import datetime, timedelta

import sgtk
from sgtk.platform.qt import QtCore, QtGui

browser_widget = sgtk.platform.import_framework("tk-framework-widget", "browser_widget")

class PublishListView(browser_widget.BrowserWidget):
    """
    UI for displaying a list of snapshot items
    """
    
    def __init__(self, parent=None):
        """
        Construction
        """
        browser_widget.BrowserWidget.__init__(self, parent)
        
        # tweak style
        self.title_style = "none"
        self.enable_search(False)
        self.enable_multi_select(True)
        self.set_label("")
        self.ui.browser_header.setVisible(False)
    
    def get_data(self, data):
        """
        """        
        return data
    
    def process_result(self, result):
        """
        Process worker result on main thread - can create list items here.
        """
        for sg_publish in result:
            list_item = self.add_item(browser_widget.ListItem)
            
            thumbnail_path = sg_publish.get("image")
            name = sg_publish.get("name")
            version = sg_publish.get("version_number")
            entity_type = sg_publish.get("entity", {}).get("type")
            entity_name = sg_publish.get("entity", {}).get("name")
            task_name = sg_publish.get("task.Task.content")
            
            list_item.set_thumbnail(thumbnail_path)
            
            line_1 = "<b>%s v%03d</b>" % (name, version)
            line_2 = "%s %s, %s" % (entity_type, entity_name, task_name)
            list_item.set_details("<br>".join([line_1, line_2]))

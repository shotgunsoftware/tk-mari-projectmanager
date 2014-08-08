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
UI for creating a new project
"""

import sgtk
from sgtk.platform.qt import QtGui, QtCore

class NewProjectForm(QtGui.QWidget):
    """
    """
    
    # define signals that this form exposes:
    create_project = QtCore.Signal(QtGui.QWidget)
    browse_publishes = QtCore.Signal(QtGui.QWidget)
    
    def __init__(self, app, init_proc, parent=None):
        """
        """
        QtGui.QWidget.__init__(self, parent)
        
        # set up the UI
        from .ui.new_project_form import Ui_NewProjectForm
        self.__ui = Ui_NewProjectForm()
        self.__ui.setupUi(self)
        
        self.__ui.create_btn.clicked.connect(self._on_create_clicked)
        self.__ui.add_publish_btn.clicked.connect(self._on_add_publish_clicked)
        
        self.__ui.publish_list.set_app(app)
        
        # temp as it's not hooked up yet!
        self.__ui.name_preview_label.setVisible(False)
        
        self.update_publishes()
        
        init_proc(self)
        
    @property
    def project_name(self):
        """
        """
        return self.__ui.name_edit.text()
    
    def update_publishes(self, sg_publish_data=None):
        """
        """
        self.__ui.publish_list.clear()
        if not sg_publish_data:
            self.__ui.publish_list.set_message("<i>You must add at least one publish before "
                                               "you can create the new project...</i>")
            self.__ui.create_btn.setEnabled(False)
        else:
            self.__ui.publish_list.load(sg_publish_data)
            self.__ui.create_btn.setEnabled(True)

    def closeEvent(self, event):
        """
        Called when the widget is closed.
        """
        # make sure the publish list BrowserWidget is 
        # cleaned up properly
        self.__ui.publish_list.destroy()
        
        return QtGui.QWidget.closeEvent(self, event)
    
    def _on_create_clicked(self):
        """
        """
        self.create_project.emit(self)
        
    def _on_add_publish_clicked(self):
        """
        """
        self.browse_publishes.emit(self)

    
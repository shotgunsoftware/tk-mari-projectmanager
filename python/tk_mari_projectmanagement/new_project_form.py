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

class NewProjectForm(QWidget):
    """
    """
    
    # define signals that this form exposes:
    create_project = QtCore.QSignal(QtGui.QWidget)
    
    def __init__(self, parent=None):
        """
        """
        QWidget.__init__(self, parent)
        
        # set up the UI
        from .ui.new_project_form import Ui_NewProjectForm
        self.__ui = Ui_NewProjectForm()
        self.__ui.setupUi(self)
        
        self.__ui.create_btn.clicked.connect(self._on_create_clicked)
        
    @property
    def project_name(self):
        """
        """
        return self.__ui.name_edit.text()
    
    def _on_create_clicked(self):
        """
        """
        create_project.emit(self)
        
    
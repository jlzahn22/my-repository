# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:51:07 2020

@author: Jessi's PC
"""

import StageControlWidget
from PyQt5 import QtGui, QtDesigner
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, qApp, QAction, QMainWindow, QFrame

class StageControlWidgetPlugin(QtDesigner.QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent = None):
        QtDesigner.QPyDesignerCustomWidgetPlugin.__init__(self)
        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return
        self.initialized = True

    def isInitialized(self):
        return self.initialized
    def createWidget(self, parent):
        return StageControlWidget.StageControlWidget(parent)
    def name(self):
        return "StageControlWidget"
    def group(self):
        return "PyQt Examples"
    def icon(self):
        return QtGui.QIcon(QtGui.QPixmap(16, 16))
    def toolTip(self):
        return ""
    def whatsThis(self):
        return ""
    def isContainer(self):
        return False
    def domXml(self):
        return (
                '<widget class="StageControlWidget" name=\"StageControlWidget\">\n'
                " <property name=\"toolTip\" >\n"
                "  <string>StageControlWidget.</string>\n"
                " </property>\n"
                " <property name=\"whatsThis\" >\n"
                "  <string>StageControlWidget.</string>\n"
                " </property>\n"
                "</widget>\n"
                )
    def includeFile(self):
        return "StageControlWidget"

import TemplateWidget
from PyQt5 import QtGui, QtDesigner
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, qApp, QAction, QMainWindow, QFrame

class TemplateWidgetPlugin(QtDesigner.QPyDesignerCustomWidgetPlugin):

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
        return TemplateWidget.TemplateWidget(parent)
    def name(self):
        return "TemplateWidget"
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
                '<widget class="TemplateWidget" name=\"TemplateWidget\">\n'
                " <property name=\"toolTip\" >\n"
                "  <string>TemplateWidget.</string>\n"
                " </property>\n"
                " <property name=\"whatsThis\" >\n"
                "  <string>TemplateWidget.</string>\n"
                " </property>\n"
                "</widget>\n"
                )
    def includeFile(self):
        return "TemplateWidget"

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:45:46 2020

@author: Jessi's PC
"""

from PyQt5 import QtCore, QtGui, QtWidgets

#create base widget ui from template widget ui
class Ui_stageControlWidget(object):
    def setupUi(self, stageControlWidget):
        stageControlWidget.setObjectName("stageControlWidget")
        stageControlWidget.resize(577, 502)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(stageControlWidget.sizePolicy().hasHeightForWidth())
        stageControlWidget.setSizePolicy(sizePolicy)
        stageControlWidget.setMinimumSize(QtCore.QSize(0, 0))
        stageControlWidget.setStyleSheet("font: 8pt \"Calibri\";")
        self.gridLayout = QtWidgets.QGridLayout(stageControlWidget)
        self.gridLayout.setObjectName("gridLayout")

        self.retranslateUi(stageControlWidget)
        QtCore.QMetaObject.connectSlotsByName(stageControlWidget)

    def retranslateUi(self, stageControlWidget):
        _translate = QtCore.QCoreApplication.translate
        stageControlWidget.setWindowTitle(_translate("stageControlWidget", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    stageControlWidget = QtWidgets.QWidget()
    ui = Ui_stageControlWidget()
    ui.setupUi(stageControlWidget)
    stageControlWidget.show()
    sys.exit(app.exec_())
    
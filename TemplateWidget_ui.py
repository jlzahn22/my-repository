# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TemplateWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_templateWidget(object):
    def setupUi(self, templateWidget):
        templateWidget.setObjectName("templateWidget")
        templateWidget.resize(577, 502)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(templateWidget.sizePolicy().hasHeightForWidth())
        templateWidget.setSizePolicy(sizePolicy)
        templateWidget.setMinimumSize(QtCore.QSize(0, 0))
        templateWidget.setStyleSheet("font: 8pt \"Calibri\";")
        self.gridLayout = QtWidgets.QGridLayout(templateWidget)
        self.gridLayout.setObjectName("gridLayout")

        self.retranslateUi(templateWidget)
        QtCore.QMetaObject.connectSlotsByName(templateWidget)

    def retranslateUi(self, templateWidget):
        _translate = QtCore.QCoreApplication.translate
        templateWidget.setWindowTitle(_translate("templateWidget", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    templateWidget = QtWidgets.QWidget()
    ui = Ui_templateWidget()
    ui.setupUi(templateWidget)
    templateWidget.show()
    sys.exit(app.exec_())

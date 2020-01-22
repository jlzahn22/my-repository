import TemplateWidget_ui
from PyQt5.QtWidgets import QWidget, QSpinBox, QComboBox, QLineEdit, QDoubleSpinBox
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject


class TemplateWidget(QWidget):

    # Define a new signal
    testSignal = pyqtSignal()
    
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = TemplateWidget_ui.Ui_templateWidget()
        self.ui.setupUi(self)

    @pyqtSlot()
    def testSlot(self):
        pass
        
    @pyqtSlot('QString')
    def testSlot(self, value):
        pass
        
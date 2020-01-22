# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:40:47 2020

@author: Jessi's PC
"""

import StageControlWidget_ui
from PyQt5.QtWidgets import QWidget, QSpinBox, QComboBox, QLineEdit, QDoubleSpinBox
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject

class StageControlWidget(Qwidget):
    
    signal = pyqtSignal()
    
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = StageControlWidget_ui.Ui_stageControlWidget()
        self.ui.setupUi(self)

    @pyqtSlot()
    def Slot(self):
        pass
        
    @pyqtSlot('QString')
    def testSlot(self, value):
        pass   
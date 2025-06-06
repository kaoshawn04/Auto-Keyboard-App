import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QSplitter
)

from UI import key_setting, basic_setting


class AutoKeyboardApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("按鍵助手")
        self.resize(500, 375)
        
        self.initUI()
        
        
    def initUI(self):
        self.main_layout = QHBoxLayout(self)
        self.setLayout(self.main_layout)
 
        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        self.main_layout.addWidget(self.splitter)
        
        self.splitter.addWidget(key_setting.KeySettingPanel().get())
        self.splitter.addWidget(basic_setting.BasicSettingPanel().get())
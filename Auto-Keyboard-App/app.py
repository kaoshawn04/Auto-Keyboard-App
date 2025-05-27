import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, 
    QTableWidgetItem, QHBoxLayout, QInputDialog, QMessageBox,
    QSplitter, QFrame, QLabel, QDialog, QRadioButton, QSpinBox, QDoubleSpinBox, QButtonGroup
)

from UI import key_setting, basic_setting
from UI.basic import Title, Button, ButtonGroup


class AutoKeyboardApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("按鍵助手")
        self.resize(400, 300)
        
        self.initUI()
        
        
    def initUI(self):
        self.main_layout = QHBoxLayout(self)
        self.setLayout(self.main_layout)

        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        self.main_layout.addWidget(self.splitter)
        
        self.splitter.addWidget(key_setting.KeySettingPanel().get())
        self.splitter.addWidget(basic_setting.BasicSettingPanel().get())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AutoKeyboardApp()
    window.show()
    
    sys.exit(app.exec())
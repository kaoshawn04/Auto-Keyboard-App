import auto_keyboard

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QFrame, QMessageBox
)

from library.common.path import realpath
from UI.basic import Title, ComboBox, Button


class BasicSettingPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.auto_keyboard = auto_keyboard.AutoKeyboard()
        
        self.Basic_panel = QFrame()
        layout = QVBoxLayout()
        self.Basic_panel.setLayout(layout)
        
        title = Title("基本設定").get()
        layout.addWidget(title)

        layout.addLayout(ComboBox("語言", ["繁體中文", "English"]).get())
        
        self.start_button = Button("開始", lambda: self.start()).get()
        self.stop_button = Button("停止", lambda: self.stop()).get()
        self.stop_button.setDisabled(True)
        
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        
        
    def start(self):
        with open(realpath("keysets.json"), "r+") as jf:
            if not jf.read(1):
                QMessageBox.warning(self, "按鍵不存在", "請先新增按鍵。")
                return
            
        self.auto_keyboard.start()
        self.start_button.setDisabled(True)
        self.stop_button.setDisabled(False)


    def stop(self):
        self.auto_keyboard.stop()
        self.start_button.setDisabled(False)
        self.stop_button.setDisabled(True)


    def get(self):
        return self.Basic_panel
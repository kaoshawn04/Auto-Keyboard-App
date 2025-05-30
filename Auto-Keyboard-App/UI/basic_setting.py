from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QFrame
)

from UI.basic import Title, ComboBox, Button


class BasicSettingPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.Basic_panel = QFrame()
        layout = QVBoxLayout()
        self.Basic_panel.setLayout(layout)
        
        title = Title("基本設定").get()
        layout.addWidget(title)
        
        layout.addLayout(ComboBox("語言", ["繁體中文", "English"]).get())
        
        layout.addWidget(Button("開始", self.start).get())
        
    
    def start(self):
        pass
       
    
    def get(self):
        return self.Basic_panel
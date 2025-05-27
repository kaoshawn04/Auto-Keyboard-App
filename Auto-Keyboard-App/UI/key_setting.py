from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget,
    QFrame, QLabel, QLineEdit, QPushButton
)

from UI.basic import Title, DTable, Button, ButtonGroup


class AddKeyDialog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("新增按鍵")
        layout = QVBoxLayout()
        
        key_layout = QVBoxLayout()
        key_label = QLabel("按鍵:")
        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("請輸入按鍵名稱 ( 以逗號分隔 )")
        
        key_layout.addWidget(key_label)
        key_layout.addWidget(self.key_input)
        layout.addLayout(key_layout)
        
        interval_layout = QVBoxLayout()
        interval_label = QLabel("間隔時間:")
        self.interval_input = QLineEdit()
        self.interval_input.setPlaceholderText("請輸入間隔時間 ( 秒 )")
        
        interval_layout.addWidget(interval_label)
        interval_layout.addWidget(self.interval_input)
        layout.addLayout(interval_layout)
        
        self.setLayout(layout)


class KeySettingPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.key_panel = QFrame()
        layout = QVBoxLayout()
        self.key_panel.setLayout(layout)
        
        title = Title("按鍵設定").get()
        layout.addWidget(title)
        
        layout.addWidget(DTable(["按鍵", "間隔時間 ( 秒 )", "重複次數"]).get())
        
        button = QPushButton("test")
        button.clicked.connect(self.test)
        
        layout.addWidget(button)
                
        button_group = ButtonGroup([
            Button("新增", self.add_key).get(),
            Button("編輯", self.edit_key).get(),
            Button("刪除", self.delete_key).get()
        ])
        
        layout.addLayout(button_group.get())
                

    def get(self):
        return self.key_panel
    
    
    def test(self):
        print("test")
    
    
    def add_key(self):
        print("press")
        
        dialog = AddKeyDialog(self)
        dialog.exec()
    
    
    def edit_key(self):
        pass    
    
    
    def delete_key(self):   
        pass
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QLabel, QTableWidget, QComboBox,
    QPushButton, QButtonGroup
)


class Title(QWidget):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        
        self.title = QLabel(text)
        self.title.setStyleSheet("font-size: 13px")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
    def get(self):
        return self.title
    

class DTable(QWidget):
    def __init__(self, headers, parent=None):
        super().__init__(parent)
        
        self.table = QTableWidget(0, len(headers))
        self.table.setHorizontalHeaderLabels(headers)
        self.table.horizontalHeader().setHighlightSections(False)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        
    def get(self):
        return self.table
    

class ComboBox(QWidget):
    def __init__(self, text, items, parent=None):
        super().__init__(parent)
        
        self.layout = QHBoxLayout()
        
        self.label = QLabel(text)
        
        self.combo_box = QComboBox()
        self.combo_box.addItems(items)
        self.combo_box.setEditable(True)
        self.combo_box.lineEdit().setReadOnly(True)
        
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.combo_box)
        
    def get(self):
        return self.layout
    
    
class Button(QWidget):
    def __init__(self, text, callback, parent=None):
        super().__init__(parent)
        
        self.button = QPushButton(text)
        self.button.clicked.connect(callback)
        
    def get(self):
        return self.button
    
    
class ButtonGroup(QWidget):
    def __init__(self, buttons, parent=None):
        super().__init__(parent)
        
        self.layout = QHBoxLayout()
        self.button_group = QButtonGroup()
        
        for i, button in enumerate(buttons):
            self.layout.addWidget(button)
            self.button_group.addButton(button, i)
            
            
    def get(self):
        return self.layout
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QLabel, QTableWidget, QComboBox,
    QPushButton, QButtonGroup, QDialog, QHeaderView
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

        metrics = self.table.fontMetrics()
        min_widths = []
        for header in headers:
            text_width = metrics.horizontalAdvance(header)
            min_widths.append(text_width)
        
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        
        def _resize_table():
            for i, width in enumerate(min_widths):
                self.table.setColumnWidth(
                    i,
                    width + (self.table.viewport().width() - sum(min_widths)) // len(headers)
                )
            
        QTimer.singleShot(0, _resize_table)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)

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
    
    
class OCButton(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.layout = QHBoxLayout()
        
        button_ok = QPushButton("確定")
        button_ok.clicked.connect(self._accept)
        button_ok.setDefault(True)
        self.layout.addWidget(button_ok)
        
        button_cancel = QPushButton("取消")
        button_cancel.clicked.connect(self._reject)
        self.layout.addWidget(button_cancel)
        
    def _accept(self):
        if isinstance(self.parent(), QDialog):
            self.parent().accept()   

    def _reject(self):
        if isinstance(self.parent(), QDialog):
            self.parent().reject()

    def get(self):
        return self.layout
    
    
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
    
    def get_buttons(self):
        return self.button_group.buttons()
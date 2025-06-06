import json
import time

from PyQt6.QtWidgets import (
    QDialog, QMessageBox, QFrame, QHBoxLayout, QLabel, QLineEdit,
    QRadioButton, QSpinBox, QTableWidgetItem, QVBoxLayout, QWidget
)

from library.common.path import realpath
from UI.basic import Title, DTable, Button, OCButton, ButtonGroup


class AddKeyDialog(QDialog):
    def __init__(self, default=None):
        super().__init__()
        
        self.setWindowTitle("新增按鍵")
        layout = QVBoxLayout()
        
        key_layout = QVBoxLayout()
        key_label = QLabel("按鍵:")
        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("請輸入按鍵名稱 ( 以逗號分隔 )")
        
        if default is not None:
            self.key_input.setText(", ".join(default[0]))
        
        key_layout.addWidget(key_label)
        key_layout.addWidget(self.key_input)
        layout.addLayout(key_layout)
        
        interval_layout = QVBoxLayout()
        interval_label = QLabel("間隔時間:")
        self.interval_input = QLineEdit()
        self.interval_input.setPlaceholderText("請輸入間隔時間 ( 秒 )")
        
        if default is not None:
            self.interval_input.setText(default[1])
        
        interval_layout.addWidget(interval_label)
        interval_layout.addWidget(self.interval_input)
        layout.addLayout(interval_layout)
        
        repeat_layout = QVBoxLayout()
        repeat_label = QLabel("重複方式:")
        
        repeat_opt1 = QHBoxLayout()
        self.repeat_opt1_radio = QRadioButton("重複:")
        self.repeat_opt1_radio.toggled.connect(self.update_enable_repeat_field)
        self.repeat_opt1_spin = QSpinBox()
        self.repeat_opt1_spin.setSuffix(" 次")
        self.repeat_opt1_spin.setRange(1, 10 ** 5)
        self.repeat_opt1_spin.setEnabled(False)
        
        if default is not None and default[2][1] == 1:
            self.repeat_opt1_radio.setChecked(True)
            self.repeat_opt1_spin.setValue(default[2][0])
            
        repeat_opt1.addWidget(self.repeat_opt1_radio)
        repeat_opt1.addWidget(self.repeat_opt1_spin)
        repeat_layout.addLayout(repeat_opt1)
        
        repeat_opt2 = QHBoxLayout()
        self.repeat_opt2_radio = QRadioButton("重複直到停止")
        
        if default is not None and default[2][1] == 0:
            self.repeat_opt2_radio.setChecked(True)
            
        repeat_opt1.addWidget(self.repeat_opt2_radio)
        repeat_layout.addLayout(repeat_opt2)
        
        layout.addWidget(repeat_label)
        layout.addLayout(repeat_layout)

        OCbutton = OCButton(self).get()
        layout.addLayout(OCbutton)
        
        self.setLayout(layout)
        
        
    def update_enable_repeat_field(self):
        self.repeat_opt1_spin.setEnabled(
            self.repeat_opt1_radio.isChecked()
        )
                

    def get_value(self):
        key = self.key_input.text().replace(" ", "").split(",")
        interval = self.interval_input.text()
        
        if not key or not interval: 
            QMessageBox.warning(self, "輸入不得為空", "請輸入正確的值。")
            return
        
        if any([not (k.encode().isalpha() or k.isnumeric()) for k in key]):
            QMessageBox.warning(self, "輸入錯誤", "請輸入正確的按鍵名稱。")
            return
        
        def _isnumber(s):
            try:
                float(s)
                return True
                
            except ValueError:
                return False
                
                
        if not _isnumber(interval) or float(interval) <= 0:
            QMessageBox.warning(self, "輸入錯誤", "請輸入正確的間隔時間。")
            return
        
        if self.repeat_opt1_radio.isChecked():
            repeat = (round(self.repeat_opt1_spin.value(), 1), 1)
            
        elif self.repeat_opt2_radio.isChecked():
            repeat = (0, 0)
            
        else:
            QMessageBox.warning(self, "輸入不得為空", "請勾選重複方式。")
            return
        
        return key, interval, repeat
        

class KeySettingPanel(QWidget):
    def __init__(self):
        super().__init__()
        
        self.key_panel = QFrame()
        layout = QVBoxLayout()
        self.key_panel.setLayout(layout)
        
        title = Title("按鍵設定", self).get()
        layout.addWidget(title)
        
        self.table = DTable(["按鍵", "間隔時間", "重複方式"], self).get()
        layout.addWidget(self.table)
                
        button_group = ButtonGroup([
            Button("新增", lambda: self.add_key(), self).get(),
            Button("編輯", lambda: self.edit_key(), self).get(),
            Button("刪除", lambda: self.delete_key(), self).get()
        ], self).get()
        
        layout.addLayout(button_group)
      
        with open(realpath("keysets.json"), "r") as jf:
            if jf.read(1):
                jf.seek(0)
                keysets = json.load(jf)
                
            else:
                return
        
        for keyset in keysets:
            row = self.table.rowCount()
            self.table.insertRow(row)
            item = QTableWidgetItem(f"{", ".join(keyset["key"])}")
            item.setData(1001, keyset["id"])
            self.table.setItem(row, 0, item)
            self.table.setItem(row, 1, QTableWidgetItem(f"{keyset["interval"]} 秒"))
                
            if keyset["repeat"][1] == 1:
                self.table.setItem(row, 2, QTableWidgetItem(f"重複 {keyset["repeat"][0]} 次"))
                
            elif keyset["repeat"][1] == 0:
                self.table.setItem(row, 2, QTableWidgetItem("重複直到停止")) 


    def add_key(self):        
        self.dialog = AddKeyDialog()
        self.dialog.show()
        
        if self.dialog.exec() == QDialog.DialogCode.Accepted:
            if self.dialog.get_value() is None:
                return
            
            else:
                id = time.time_ns()
                key, interval, repeat = self.dialog.get_value()
            
            row = self.table.rowCount()
            self.table.insertRow(row)
            item = QTableWidgetItem(f"{", ".join(key)}")
            item.setData(1001, id)
            self.table.setItem(row, 0, item)
            self.table.setItem(row, 1, QTableWidgetItem(f"{interval} 秒"))
                
            if repeat[1] == 1:
                self.table.setItem(row, 2, QTableWidgetItem(f"重複 {repeat[0]} 次"))
                
            elif repeat[1] == 0:
                self.table.setItem(row, 2, QTableWidgetItem("重複直到停止"))
        
        elif self.dialog.exec() == QDialog.DialogCode.Rejected:
            return
                
        with open(realpath("keysets.json"), "r+") as jf:
            if jf.read(1):
                jf.seek(0)
                keysets = json.load(jf)
                
            else:
                keysets = []
            
            jf.truncate(0)
            jf.seek(0)
            keysets.append({
                "id": id,
                "key": key,
                "interval": interval,
                "repeat": repeat
            })
            json.dump(keysets, jf, indent=4)
        

    def edit_key(self):
        row = self.table.currentRow()
        
        if row < 0:
            QMessageBox.warning(self, "選擇錯誤", "請選擇要編輯的按鍵。")
            return
        
        item = self.table.item(row, 0)
        id = item.data(1001)
        
        with open(realpath("keysets.json"), "r+") as jf:
            keysets = json.load(jf)
            target_keyset = [keyset for keyset in keysets if keyset["id"] == id][0]
            keysets.remove(target_keyset)
        
            self.dialog = AddKeyDialog(
                default=[target_keyset["key"], target_keyset["interval"], target_keyset["repeat"]]
            )
            self.dialog.show()
            
            if self.dialog.exec() == QDialog.DialogCode.Accepted:
                if self.dialog.get_value() is None:
                    return
                
                else:
                    key, interval, repeat = self.dialog.get_value()
                    target_keyset["key"] = key
                    target_keyset["interval"] = interval
                    target_keyset["repeat"] = repeat
                    keysets.append(target_keyset)

                item = QTableWidgetItem(f"{", ".join(key)}")
                item.setData(1001, id)
                self.table.setItem(row, 0, item)
                self.table.setItem(row, 1, QTableWidgetItem(f"{interval} 秒"))
                    
                if repeat[1] == 1:
                    self.table.setItem(row, 2, QTableWidgetItem(f"重複 {repeat[0]} 次"))
                    
                elif repeat[1] == 0:
                    self.table.setItem(row, 2, QTableWidgetItem("重複直到停止"))
            
            jf.truncate(0)
            jf.seek(0)
            json.dump(keysets, jf, indent=4)


    def delete_key(self):   
        row = self.table.currentRow()
        
        if row < 0:
            QMessageBox.warning(self, "選擇錯誤", "請選擇要刪除的按鍵。")
            return
        
        item = self.table.item(row, 0)
        id = item.data(1001)
                
        with open(realpath("keysets.json"), "r+") as jf:
            keysets = json.load(jf)
            keysets = [keyset for keyset in keysets if keyset["id"] != id]
            
            jf.truncate(0)
            jf.seek(0)
            json.dump(keysets, jf, indent=4)
        
        self.table.removeRow(row)


    def get(self):
        return self.key_panel
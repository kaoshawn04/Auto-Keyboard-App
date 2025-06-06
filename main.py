import sys

from PyQt6.QtWidgets import QApplication

from app import AutoKeyboardApp


def main():
    app = QApplication(sys.argv)
    window = AutoKeyboardApp()
    window.show()
    
    sys.exit(app.exec())

        
if __name__ == "__main__":
    if True:
        import pyuac
        
        if not pyuac.isUserAdmin():
            pyuac.runAsAdmin()
    
        else:
            main()
            
    else:
        main()
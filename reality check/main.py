import sys
from PySide6.QtWidgets import QApplication
from views import MoneyManagementApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MoneyManagementApp()
    window.show()
    sys.exit(app.exec())

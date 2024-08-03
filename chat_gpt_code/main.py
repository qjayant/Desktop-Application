import sys
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt 
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QLineEdit, QListWidget, QListWidgetItem, QMessageBox, QFormLayout,
     QToolBar, QSizePolicy, QFontComboBox, QComboBox
)
from PySide6.QtCore import QDateTime, Qt


class MoneyManagementApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Money Management App")
        self.setGeometry(100, 100, 800, 600)
        
        self.persons = {}

        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()

        self.add_person_layout = QHBoxLayout()
        self.person_name_input = QLineEdit()
        self.person_name_input.setPlaceholderText("Enter person's name")
        self.add_person_button = QPushButton("Add Person")
        self.add_person_button.clicked.connect(self.add_person)

        self.person_name_input.returnPressed.connect(self.add_person)

        self.add_person_layout.addWidget(self.person_name_input)
        self.add_person_layout.addWidget(self.add_person_button)

        self.person_list = QListWidget()
        self.person_list.itemClicked.connect(self.show_transactions)

        self.summary_layout = QHBoxLayout()
        self.monthly_summary_button = QPushButton("Monthly Summary")
        self.monthly_summary_button.clicked.connect(self.show_monthly_summary)
        self.yearly_summary_button = QPushButton("Yearly Summary")
        self.yearly_summary_button.clicked.connect(self.show_yearly_summary)

        self.summary_layout.addWidget(self.monthly_summary_button)
        self.summary_layout.addWidget(self.yearly_summary_button)

        self.main_layout.addLayout(self.add_person_layout)
        self.main_layout.addWidget(self.person_list)
        self.main_layout.addLayout(self.summary_layout)

        self.person_buttons_layout = QHBoxLayout()  # Layout for person buttons
        self.main_layout.addLayout(self.person_buttons_layout)

        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
       
        

        self.create_toolbar()


    def create_toolbar(self):
        toolbar = QToolBar("Toolbar")
        self.addToolBar(toolbar)

        # Text Size Control
        text_size_label = QLabel("Text Size:")
        toolbar.addWidget(text_size_label)

        self.text_size_combo = QComboBox()
        self.text_size_combo.addItem("Small")
        self.text_size_combo.addItem("Medium")
        self.text_size_combo.addItem("Large")
        self.text_size_combo.currentIndexChanged.connect(self.change_text_size)
        toolbar.addWidget(self.text_size_combo)

        # Delete Person
        delete_person_action = QAction("Delete Person", self)
        delete_person_action.triggered.connect(self.delete_person)
        toolbar.addAction(delete_person_action)

        # Separator
        toolbar.addSeparator()

        # Other Actions (if any)

    def change_text_size(self, index):
       size = self.text_size_combo.currentText()
       font = self.font()

       if size == "Small":
          font.setPointSize(10)
       elif size == "Medium":
        font.setPointSize(12)
       elif size == "Large":
        font.setPointSize(14)

       self.setFont(font)


    def add_person(self):
        person_name = self.person_name_input.text().strip()
        if person_name:
            if person_name not in self.persons:
                self.persons[person_name] = []
                self.person_list.addItem(person_name)
                self.person_name_input.clear()

                # Add person name as a button
                person_button = QPushButton(person_name)
                person_button.clicked.connect(lambda _, name=person_name: self.person_button_clicked(name))
                self.person_buttons_layout.addWidget(person_button)
            else:
                QMessageBox.warning(self, "Warning", "Person already exists!")
        else:
            QMessageBox.warning(self, "Warning", "Please enter a name!")

    def person_button_clicked(self, person_name):
        # Implement any action when a person button is clicked
        QMessageBox.information(self, "Button Clicked", f"{person_name} button clicked!")


    def show_transactions(self, item):
        person_name = item.text()
        transactions = self.persons[person_name]

        self.transaction_widget = QWidget()
        self.transaction_layout = QVBoxLayout()

        self.transaction_form_layout = QFormLayout()
        self.amount_input = QLineEdit()
        self.date_time_input = QLineEdit()
        self.date_time_input.setText(QDateTime.currentDateTime().toString())
        self.payment_method_input = QLineEdit()
        self.cheque_number_input = QLineEdit()

        self.transaction_form_layout.addRow("Amount:", self.amount_input)
        self.transaction_form_layout.addRow("Date & Time:", self.date_time_input)
        self.transaction_form_layout.addRow("Payment Method:", self.payment_method_input)
        self.transaction_form_layout.addRow("Cheque Number (if applicable):", self.cheque_number_input)

        self.add_transaction_button = QPushButton("Add Transaction")
        self.add_transaction_button.clicked.connect(lambda: self.add_transaction(person_name))

        self.transaction_list = QListWidget()
        for transaction in transactions:
            self.transaction_list.addItem(f"{transaction['datetime']} - {transaction['amount']} - {transaction['method']} - {transaction.get('cheque', '')}")

        self.transaction_layout.addLayout(self.transaction_form_layout)
        self.transaction_layout.addWidget(self.add_transaction_button)
        self.transaction_layout.addWidget(self.transaction_list)

        self.transaction_widget.setLayout(self.transaction_layout)
        self.transaction_widget.setWindowTitle(person_name)
        self.transaction_widget.show()

    def add_transaction(self, person_name):
        amount = self.amount_input.text()
        date_time = self.date_time_input.text()
        method = self.payment_method_input.text()
        cheque_number = self.cheque_number_input.text()

        transaction = {
            "amount": amount,
            "datetime": date_time,
            "method": method,
        }

        if method.lower() == "cheque":
            transaction["cheque"] = cheque_number

        self.persons[person_name].append(transaction)
        self.transaction_list.addItem(f"{date_time} - {amount} - {method} - {transaction.get('cheque', '')}")

        self.amount_input.clear()
        self.payment_method_input.clear()
        self.cheque_number_input.clear()

    def show_monthly_summary(self):
        # Implementation for monthly summary
        pass

    def show_yearly_summary(self):
        # Implementation for yearly summary
        pass

    def delete_person(self):
        current_item = self.person_list.currentItem()
        if current_item:
            person_name = current_item.text()
            reply = QMessageBox.question(self, 'Delete Person', f"Are you sure you want to delete {person_name}?", 
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                del self.persons[person_name]
                self.person_list.takeItem(self.person_list.row(current_item))
                QMessageBox.information(self, "Deleted", f"{person_name} deleted successfully.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MoneyManagementApp()
    window.show()
    sys.exit(app.exec())
 
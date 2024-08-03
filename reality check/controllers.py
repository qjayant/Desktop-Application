from PySide6.QtWidgets import QMessageBox, QListWidgetItem, QLineEdit, QPushButton, QListWidget, QFormLayout, QVBoxLayout, QWidget
from PySide6.QtCore import QDateTime

class AppController:
    def __init__(self, view):
        self.view = view
        self.persons = {}

    def add_person(self):
        person_name = self.view.person_name_input.text().strip()
        if person_name:
            if person_name not in self.persons:
                self.persons[person_name] = []
                self.view.person_list.addItem(person_name)
                self.view.person_name_input.clear()

                self.view.add_person_button(person_name)
            else:
                QMessageBox.warning(self.view, "Warning", "Person already exists!")
        else:
            QMessageBox.warning(self.view, "Warning", "Please enter a name!")

    def person_button_clicked(self, person_name):
        QMessageBox.information(self.view, "Button Clicked", f"{person_name} button clicked!")

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
        pass

    def show_yearly_summary(self):
        pass

    def delete_person(self):
        current_item = self.view.person_list.currentItem()
        if current_item:
            person_name = current_item.text()
            reply = QMessageBox.question(self.view, 'Delete Person', f"Are you sure you want to delete {person_name}?", 
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                del self.persons[person_name]
                self.view.person_list.takeItem(self.view.person_list.row(current_item))
                QMessageBox.information(self.view, "Deleted", f"{person_name} deleted successfully.")

    def change_text_size(self):
        size = self.view.text_size_combo.currentText()
        font = self.view.font()

        if size == "Small":
            font.setPointSize(10)
        elif size == "Medium":
            font.setPointSize(12)
        elif size == "Large":
            font.setPointSize(14)

        self.view.setFont(font)

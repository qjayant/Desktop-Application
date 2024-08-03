from PySide6.QtGui import QAction
from PySide6.QtCore import QDateTime
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QLineEdit, QListWidget, QMessageBox, QFormLayout, QToolBar, QComboBox
)
from controllers import AppController

class MoneyManagementApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Money Management App")
        self.setGeometry(100, 100, 800, 600)
        
        self.controller = AppController(self)
        
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()

        self.add_person_layout = QHBoxLayout()
        self.person_name_input = QLineEdit()
        self.person_name_input.setPlaceholderText("Enter person's name")
        self.add_person_button = QPushButton("Add Person")
        self.add_person_button.clicked.connect(self.controller.add_person)

        self.person_name_input.returnPressed.connect(self.controller.add_person)

        self.add_person_layout.addWidget(self.person_name_input)
        self.add_person_layout.addWidget(self.add_person_button)

        self.person_list = QListWidget()
        self.person_list.itemClicked.connect(self.controller.show_transactions)

        self.summary_layout = QHBoxLayout()
        self.monthly_summary_button = QPushButton("Monthly Summary")
        self.monthly_summary_button.clicked.connect(self.controller.show_monthly_summary)
        self.yearly_summary_button = QPushButton("Yearly Summary")
        self.yearly_summary_button.clicked.connect(self.controller.show_yearly_summary)

        self.summary_layout.addWidget(self.monthly_summary_button)
        self.summary_layout.addWidget(self.yearly_summary_button)

        self.main_layout.addLayout(self.add_person_layout)
        self.main_layout.addWidget(self.person_list)
        self.main_layout.addLayout(self.summary_layout)

        self.person_buttons_layout = QHBoxLayout()
        self.main_layout.addLayout(self.person_buttons_layout)

        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

        self.create_toolbar()

    def create_toolbar(self):
        toolbar = QToolBar("Toolbar")
        self.addToolBar(toolbar)

        text_size_label = QLabel("Text Size:")
        toolbar.addWidget(text_size_label)

        self.text_size_combo = QComboBox()
        self.text_size_combo.addItem("Small")
        self.text_size_combo.addItem("Medium")
        self.text_size_combo.addItem("Large")
        self.text_size_combo.currentIndexChanged.connect(self.controller.change_text_size)
        toolbar.addWidget(self.text_size_combo)

        delete_person_action = QAction("Delete Person", self)
        delete_person_action.triggered.connect(self.controller.delete_person)
        toolbar.addAction(delete_person_action)

        toolbar.addSeparator()

    def add_person_button(self, person_name):
        person_button = QPushButton(person_name)
        person_button.clicked.connect(lambda _, name=person_name: self.controller.person_button_clicked(name))
        self.person_buttons_layout.addWidget(person_button)

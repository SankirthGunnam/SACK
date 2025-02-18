from PySide6.QtWidgets import (
    QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, 
    QGridLayout, QLineEdit, QSplitter, QTreeWidget, QTreeWidgetItem, QTableWidget, 
    QTableWidgetItem, QListWidget, QListWidgetItem, QGroupBox, QTextEdit, QDockWidget, 
    QRadioButton
)
from PySide6.QtCore import Qt
from your_package.style_manager import StyleManager  # Update with actual import

class TestStyleApp(QMainWindow):
    def __init__(self, style_manager_light, style_manager_dark):
        super().__init__()
        self.setWindowTitle("PySide6 Style Testing App")
        self.resize(800, 600)

        # Store style managers
        self.style_manager_light = style_manager_light
        self.style_manager_dark = style_manager_dark

        # Set initial style (light theme)
        self.set_stylesheet(self.style_manager_light)

        # Main central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layouts
        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        form_layout = QGridLayout()
        theme_layout = QHBoxLayout()

        # Theme Switch Radio Buttons
        self.radio_light = QRadioButton("Light Theme")
        self.radio_dark = QRadioButton("Dark Theme")
        self.radio_light.setChecked(True)  # Default theme
        self.radio_light.toggled.connect(self.switch_theme)
        self.radio_dark.toggled.connect(self.switch_theme)

        theme_layout.addWidget(self.radio_light)
        theme_layout.addWidget(self.radio_dark)

        # Buttons
        btn1 = QPushButton("Button 1")
        btn2 = QPushButton("Button 2")
        btn3 = QPushButton("Button 3")
        button_layout.addWidget(btn1)
        button_layout.addWidget(btn2)
        button_layout.addWidget(btn3)

        # Labels and LineEdits
        label1 = QLabel("Name:")
        label2 = QLabel("Email:")
        line_edit1 = QLineEdit()
        line_edit2 = QLineEdit()
        form_layout.addWidget(label1, 0, 0)
        form_layout.addWidget(line_edit1, 0, 1)
        form_layout.addWidget(label2, 1, 0)
        form_layout.addWidget(line_edit2, 1, 1)

        # Splitter with a Tree Widget and Text Edit
        splitter = QSplitter()
        tree_widget = QTreeWidget()
        tree_widget.setHeaderLabels(["Items"])
        parent_item = QTreeWidgetItem(tree_widget, ["Parent"])
        QTreeWidgetItem(parent_item, ["Child 1"])
        QTreeWidgetItem(parent_item, ["Child 2"])
        tree_widget.expandAll()

        text_edit = QTextEdit("Editable text area")
        splitter.addWidget(tree_widget)
        splitter.addWidget(text_edit)

        # Table Widget
        table_widget = QTableWidget(3, 3)
        table_widget.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])
        for row in range(3):
            for col in range(3):
                table_widget.setItem(row, col, QTableWidgetItem(f"Item {row+1},{col+1}"))

        # List Widget
        list_widget = QListWidget()
        for i in range(5):
            list_widget.addItem(QListWidgetItem(f"Item {i+1}"))

        # Group Box
        group_box = QGroupBox("Group Box")
        group_layout = QVBoxLayout()
        group_layout.addWidget(QPushButton("Inside Group"))
        group_box.setLayout(group_layout)

        # Dock Widget
        dock_widget = QDockWidget("Dock Widget", self)
        dock_content = QTextEdit("Dockable text area")
        dock_widget.setWidget(dock_content)
        self.addDockWidget(Qt.RightDockWidgetArea, dock_widget)

        # Add widgets to main layout
        main_layout.addLayout(theme_layout)  # Add theme switch buttons
        main_layout.addLayout(button_layout)
        main_layout.addLayout(form_layout)
        main_layout.addWidget(splitter)
        main_layout.addWidget(table_widget)
        main_layout.addWidget(list_widget)
        main_layout.addWidget(group_box)

        # Set layout
        central_widget.setLayout(main_layout)

    def set_stylesheet(self, style_manager):
        """Apply the selected theme stylesheet."""
        self.setStyleSheet(style_manager.generate_stylesheet())

    def switch_theme(self):
        """Change theme dynamically when radio button is clicked."""
        if self.radio_light.isChecked():
            self.set_stylesheet(self.style_manager_light)
        else:
            self.set_stylesheet(self.style_manager_dark)

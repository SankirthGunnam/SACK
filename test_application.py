import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, 
    QGridLayout, QLineEdit, QSplitter, QTreeWidget, QTreeWidgetItem, QTableWidget, 
    QTableWidgetItem, QListWidget, QListWidgetItem, QGroupBox, QTextEdit, QDockWidget
)
from PySide6.QtCore import Qt
from your_package.style_manager import StyleManager  # Replace with actual import


class TestStyleApp(QMainWindow):
    def __init__(self, style_manager):
        super().__init__()
        self.setWindowTitle("PySide6 Style Testing App")
        self.resize(800, 600)

        # Generate stylesheet using StyleManager
        stylesheet = style_manager.generate_stylesheet()
        self.setStyleSheet(stylesheet)

        # Main central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layouts
        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        form_layout = QGridLayout()

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
        main_layout.addLayout(button_layout)
        main_layout.addLayout(form_layout)
        main_layout.addWidget(splitter)
        main_layout.addWidget(table_widget)
        main_layout.addWidget(list_widget)
        main_layout.addWidget(group_box)

        # Set layout
        central_widget.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Define styles
    style_dict = {
        "background_color": "#F0F0F0",
        "text_color": "#333333",
        "button_color": "#007BFF",
    }

    base_template = """
    QWidget {
        background-color: {{ background_color }};
        color: {{ text_color }};
    }
    QPushButton {
        background-color: {{ button_color }};
        border: 1px solid #0056b3;
        padding: 5px;
    }
    QTableWidget, QTreeWidget {
        border: 1px solid #aaa;
        background-color: #ffffff;
    }
    QLineEdit {
        border: 1px solid #999;
        padding: 3px;
    }
    QSplitter::handle {
        background-color: #666;
    }
    QDockWidget {
        titlebar-close-icon: url(none);
        titlebar-normal-icon: url(none);
    }
    """

    theme_template = """
    QPushButton:hover {
        background-color: #0056b3;
        color: #ffffff;
    }
    """

    # Create and apply styles
    style_manager = StyleManager(style_dict, base_template, theme_template)
    window = TestStyleApp(style_manager)
    window.show()

    sys.exit(app.exec())

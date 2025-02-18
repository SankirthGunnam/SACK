from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys
from your_package.style_manager import StyleManager  # Update as needed

def test_pyqt_application():
    """Launch a PyQt app with the generated stylesheet."""
    app = QApplication(sys.argv)
    
    style_dict = {
        "background_color": "#F0F0F0",
        "text_color": "#333333",
        "button_color": "#FF5733",
    }

    base_template = """
    QWidget {
        background-color: {{ background_color }};
        color: {{ text_color }};
    }
    QPushButton {
        background-color: {{ button_color }};
    }
    """

    theme_template = """
    QPushButton {
        border-radius: 10px;
    }
    """

    # Generate stylesheet using StyleManager
    style_manager = StyleManager(style_dict, base_template, theme_template)
    stylesheet = style_manager.generate_stylesheet()

    # Create and style a PyQt widget
    window = QWidget()
    window.setStyleSheet(stylesheet)

    button = QPushButton("Click Me", window)
    button.move(50, 50)

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    test_pyqt_application()

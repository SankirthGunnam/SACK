import os

def create_pyqt_style_package(base_path=""):
    # Ensure base path is set correctly
    base_path = os.path.abspath(base_path) if base_path else os.getcwd()

    # Define the folder structure
    folders = [
        f"{base_path}/pyqt_styles",
        f"{base_path}/pyqt_styles/themes",
        f"{base_path}/pyqt_styles/styles"
    ]

    # Define the files and their content
    files = {
        f"{base_path}/pyqt_styles/__init__.py": """from PyQt5.QtCore import QResource
import pyqt_styles.resources_rc  # Ensure resources are registered

QResource.registerResource("pyqt_styles/resources_rc.py")
        """,

        f"{base_path}/pyqt_styles/style_manager.py": """from PyQt5.QtCore import QResource
from jinja2 import Template

class StyleManager:
    def __init__(self, theme="light"):
        self.theme = theme

    def _load_template(self, resource_path):
        \"\"\"Loads the Jinja template from Qt resources.\"\"\"
        file = QResource(resource_path)
        if not file.isValid():
            raise FileNotFoundError(f"Resource {resource_path} not found")

        data = bytes(file.data()).decode("utf-8")
        return Template(data)

    def get_stylesheet(self, style_dict):
        \"\"\"Generates a stylesheet using embedded Jinja templates.\"\"\"
        base_template = self._load_template(":/themes/base_template.qss.j2")
        theme_template = self._load_template(f":/themes/{self.theme}_theme.qss.j2")

        base_styles = base_template.render(style=style_dict)
        theme_styles = theme_template.render(style=style_dict)

        return base_styles + "\\n" + theme_styles
        """,

        f"{base_path}/pyqt_styles/themes/base_template.qss.j2": """QWidget {
    background-color: {{ style.background }};
    color: {{ style.text_color }};
    font-size: {{ style.font_size }}px;
}
QPushButton {
    background-color: {{ style.button_background }};
    color: {{ style.button_text }};
    border-radius: {{ style.button_radius }}px;
}
        """,

        f"{base_path}/pyqt_styles/themes/dark_theme.qss.j2": """QWidget {
    background-color: #333;
    color: #fff;
}
QPushButton {
    background-color: #555;
    color: #ddd;
}
        """,

        f"{base_path}/pyqt_styles/themes/light_theme.qss.j2": """QWidget {
    background-color: #fff;
    color: #000;
}
QPushButton {
    background-color: #ddd;
    color: #111;
}
        """,

        f"{base_path}/pyqt_styles/styles/__init__.py": "",

        f"{base_path}/pyqt_styles/styles/themes.py": """LIGHT_THEME = {
    "background": "#ffffff",
    "text_color": "#000000",
    "font_size": 12,
    "button_background": "#f0f0f0",
    "button_text": "#333",
    "button_radius": 5
}

DARK_THEME = {
    "background": "#222222",
    "text_color": "#ffffff",
    "font_size": 12,
    "button_background": "#444",
    "button_text": "#fff",
    "button_radius": 5
}
        """,

        f"{base_path}/pyqt_styles/resources.qrc": """<RCC>
    <qresource prefix="/themes">
        <file alias="base_template.qss.j2">themes/base_template.qss.j2</file>
        <file alias="dark_theme.qss.j2">themes/dark_theme.qss.j2</file>
        <file alias="light_theme.qss.j2">themes/light_theme.qss.j2</file>
    </qresource>
</RCC>
        """,
    }

    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    # Create files with content
    for file_path, content in files.items():
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

    # Convert .qrc to .py resource file
    print("\nGenerating resource file...")
    qrc_path = f"{base_path}/pyqt_styles/resources.qrc"
    py_rc_path = f"{base_path}/pyqt_styles/resources_rc.py"

    os.system(f"pyrcc5 {qrc_path} -o {py_rc_path}")
    
    print(f"\nPyQt Style package created successfully at: {base_path}")
    print(f"Run the following command if pyrcc5 is not found:\n")
    print(f"    pyrcc5 {qrc_path} -o {py_rc_path}")
    
# Run the function with a base path option
if __name__ == "__main__":
    base_path = input("Enter the base path (leave empty for current directory): ").strip()
    create_pyqt_style_package(base_path)

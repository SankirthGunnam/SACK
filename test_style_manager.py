import unittest
from your_package.style_manager import StyleManager  # Update the import as needed

class TestStyleManager(unittest.TestCase):

    def setUp(self):
        """Setup sample style data for testing."""
        self.style_dict = {
            "background_color": "#FFFFFF",
            "text_color": "#000000",
            "button_color": "#007BFF",
        }

        self.base_template = """
        QWidget {
            background-color: {{ background_color }};
            color: {{ text_color }};
        }
        QPushButton {
            background-color: {{ button_color }};
        }
        """

        self.theme_template = """
        QPushButton {
            border-radius: 5px;
        }
        """

        self.style_manager = StyleManager(self.style_dict, self.base_template, self.theme_template)

    def test_generate_stylesheet(self):
        """Test if StyleManager correctly generates a stylesheet."""
        generated_stylesheet = self.style_manager.generate_stylesheet()

        self.assertIn("background-color: #FFFFFF;", generated_stylesheet)
        self.assertIn("color: #000000;", generated_stylesheet)
        self.assertIn("background-color: #007BFF;", generated_stylesheet)
        self.assertIn("border-radius: 5px;", generated_stylesheet)

    def test_missing_keys(self):
        """Test if missing keys in the dictionary are handled properly."""
        incomplete_style_dict = {"background_color": "#F0F0F0"}  # Missing other keys
        style_manager = StyleManager(incomplete_style_dict, self.base_template, self.theme_template)
        generated_stylesheet = style_manager.generate_stylesheet()

        self.assertIn("background-color: #F0F0F0;", generated_stylesheet)
        self.assertNotIn("background-color: #007BFF;", generated_stylesheet)  # Should not appear

if __name__ == "__main__":
    unittest.main()

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import pyshorteners

'''
Use OOP to structure the application
- __init__ Method: Initializes the app window and calls the init_ui method.
- init_ui Method: Sets up the GUI components.
- shorten_url Method: Shortens the URL entered by the user.
- copy_to_clipboard Method: Copies the short URL to the clipboard.
'''

class URLShortenerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        pass

    def shorten_url(self):
        pass

    def copy_to_clipboard(self):
        pass

    # The GUI of the URL Shortener
    def init_ui(self):
        self.setWindowTitle("URL Shortener")
        self.setGeometry(100, 100, 400, 250)

        layout = QVBoxLayout()

        # Instruction label
        self.label = QLabel("Enter the URL you want to shorten:")
        layout.addWidget(self.label)

        # Input field
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter your URL here...")
        layout.addWidget(self.url_input)

        # Shorten button
        self.shorten_button = QPushButton("Shorten URL")
        self.shorten_button.clicked.connect(self.shorten_url)
        layout.addWidget(self.shorten_button)

        # Label to display the short URL
        self.short_url_label = QLabel()
        layout.addWidget(self.short_url_label)

        # Copy button
        self.copy_button = QPushButton("Copy to Clipboard")
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        self.copy_button.setEnabled(False)
        layout.addWidget(self.copy_button)

        self.setLayout(layout)

        # Styling the GUI
        self.setStyleSheet("""
            QWidget {
                background-color: #f7f9fc;
            }
            QLabel {
                color: #003366;
                font-size: 14px;
                font-weight: bold;
            }
            QLineEdit {
                border: 2px solid #007BFF;
                border-radius: 5px;
                padding: 8px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #007BFF;
                color: white;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)

    #Shortening the URL
    def shorten_url(self):
        long_url = self.url_input.text().strip()
        if not long_url:
            QMessageBox.warning(self, "Input Error", "Please enter a URL to shorten.")
            return

        try:
            # Create a Shortener object
            shortener = pyshorteners.Shortener()

            # Generate the short URL
            short_url = shortener.tinyurl.short(long_url)

            # Display the short URL
            self.short_url_label.setText(f"Short URL: <a href='{short_url}' style='color:#007BFF;'>{short_url}</a>")
            self.short_url_label.setOpenExternalLinks(True)

            # Enable the copy button
            self.copy_button.setEnabled(True)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to shorten URL: {str(e)}")
    
    # Copy-to-Clipboard
    def copy_to_clipboard(self):
        short_url = self.short_url_label.text().replace("Short URL: ", "").strip()
        if short_url:
            QApplication.clipboard().setText(short_url)
            QMessageBox.information(self, "Copied", "Short URL copied to clipboard!")

# Running the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = URLShortenerApp()
    window.show()
    sys.exit(app.exec_())

'''
URL Shortener Project Summary

What You Built:
---------------
- A working URL shortener using Python and PyQt5 — great job!
- Combined cool design with real functionality.
- Used pyshorteners to turn long URLs into short ones quickly and easily.

Ideas to Improve It:
--------------------
- Add a check to make sure users enter valid URLs.
- Support more URL shortening services using the pyshorteners library.
- Add a history feature to save and show past shortened links.

Keep building and having fun with Python!
'''
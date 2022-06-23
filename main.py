from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout
import sys

index = 1


# להוסיף לטעון קובץ או ליצור חדש
class Sentence:
    voiceRecPath = ""
    keywords = []

    def __init__(self, arabic, hebrew, transcription, id_):
        self.arabic = arabic
        self.hebrew = hebrew
        self.transcription = transcription
        self.id_ = id_


# GUI

class EditorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('New Conversation')
        self.setGeometry(500,300,350,300)
        self.label = QLabel("Please fill the following fields:", self)
        self.title_box = QLineEdit(self)
        self.title_box.setPlaceholderText('Title')
        self.description_box = QLineEdit(self)
        self.description_box.setPlaceholderText('Description')
        self.photo_box = QLineEdit(self)
        self.photo_box.setText("path/to/theme/photo.jpg")
        self.level_box = QLineEdit(self)
        self.level_box.setPlaceholderText('Level')
        self.category_box = QLineEdit(self)
        self.category_box.setPlaceholderText('Category')
        self.createdBy_box = QLineEdit(self)
        self.createdBy_box.setPlaceholderText('Created By')
        self.next_button = QPushButton("Next", self)

        grid = QGridLayout()
        grid.addWidget(self.label)
        grid.addWidget(self.title_box)
        grid.addWidget(self.description_box)
        grid.addWidget(self.photo_box)
        grid.addWidget(self.level_box)
        grid.addWidget(self.category_box)
        grid.addWidget(self.createdBy_box)
        grid.addWidget(self.next_button)

        self.setLayout(grid)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Madrasa Bot Editor')
        self.setWindowIcon(QIcon("madrasa.png"))
        self.setGeometry(500, 300, 550, 300)

        self.welcome_label = QLabel("Welcome to Madrasa Bot Editor!", self)
        self.welcome_label.move(190, 50)

        self.choose()

    def choose(self):
        new_btn = QPushButton("New Conversation", self)
        existing_btn = QPushButton("Existing Conversation", self)

        new_btn.setGeometry(50, 150, 200, 100)
        existing_btn.setGeometry(300, 150, 200, 100)

        new_btn.clicked.connect(self.clicked_new)
        # existing_btn.clicked.connect(self.clicked_existing)

    def clicked_new(self):
        editor.show()
        self.hide()

    # def clicked_existing(self):


app = QApplication(sys.argv)
editor = EditorWindow()
window = MainWindow()
window.show()
app.exec()

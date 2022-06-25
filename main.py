from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout
import sys
import json

index = 1
content = dict()


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

class SentenceWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sentence adder')
        self.setGeometry(500, 300, 350, 300)



class EditorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('New Conversation')
        self.setGeometry(500, 300, 350, 300)
        self.label = QLabel("Please fill the following fields:", self)
        self.title_box = QLineEdit(self)
        self.title_box.setPlaceholderText('Title')
        self.title_box.setText("שיחה")
        self.description_box = QLineEdit(self)
        self.description_box.setPlaceholderText('Description')
        self.description_box.setText("שיחה פשוטה בין בוט לתלמיד")
        self.photo_box = QLineEdit(self)
        self.photo_box.setText("path/to/theme/photo.jpg")
        self.level_box = QLineEdit(self)
        self.level_box.setPlaceholderText('Level')
        self.level_box.setText("1")
        self.category_box = QLineEdit(self)
        self.category_box.setPlaceholderText('Category')
        self.category_box.setText("Social")
        self.createdBy_box = QLineEdit(self)
        self.createdBy_box.setPlaceholderText('Created By')
        self.createdBy_box.setText("Teacher")
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

        self.next_button.clicked.connect(self.create_json)

    def create_json(self):
        self.hide()
        adder.show()
        content["id"] = "mock-script"
        content["title"] = self.title_box.text()
        content["description"] = self.description_box.text()
        print(self.description_box.text())
        content["photo"] = self.photo_box.text()
        content["level"] = int(self.level_box.text())
        content["category"] = self.category_box.text()
        content["createdBy"] = self.createdBy_box.text()
        content["start"] = str(index)
        content["flow"] = {}

        # json_object = json.dumps(content, indent=4, ensure_ascii=False)
        #
        # # Writing to sample.json
        # with open("conversation.json", "w") as outfile:
        #     outfile.write(json_object)


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
adder = SentenceWindow()
window = MainWindow()
window.show()
app.exec()

f = open("conversation.json", "w+")

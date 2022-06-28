import os.path
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from pydub import AudioSegment
from pydub.playback import play
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout
import sys
from record import Recorder

import json

index = 1000
content = dict()
flow = dict()
sentences = dict()


# class Tree:
#     def __init__(self):
#         self.

# GUI
class SentenceWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.recFile = None
        self.setWindowTitle('Sentence adder')
        self.setGeometry(500, 300, 350, 300)
        flow[str(index)] = []
        self.label = QLabel("Enter sentence ")
        self.parent_sound = "test_" + str(parent) + ".wav"
        self.parent_voice = QPushButton('Answer to this')
        self.parent_voice.hide()
        self.arabic = QLineEdit(self)
        self.arabic.setPlaceholderText('Arabic')
        self.hebrew = QLineEdit(self)
        self.hebrew.setPlaceholderText('Hebrew')
        self.transcription = QLineEdit(self)
        self.transcription.setPlaceholderText('תעתיק')
        self.record_btn = QPushButton(self)
        self.record_btn.setText('Record')
        self.voice = QPushButton(self)
        self.voice.setIcon(QIcon("play-button.png"))
        self.voice.setEnabled(False)
        self.keywords = QLineEdit(self)
        self.keywords.setPlaceholderText("Keywords (separated by comma and a space)")
        self.done = QPushButton(self)
        self.done.setText("Done")
        self.done.clicked.connect(self.finish)
        self.done.setEnabled(False)
        self.enter = QPushButton(self)
        self.enter.setText("Enter")
        self.enter.clicked.connect(self.create_sentence)
        self.add_response = QPushButton(self)
        self.add_response.setText("Add Response")
        self.add_response.setEnabled(False)
        # self.advance = QPushButton(self)
        # self.advance.setText("Advance")

        grid = QGridLayout()
        grid.addWidget(self.label, 0, 0)
        grid.addWidget(self.parent_voice, 0, 1)
        grid.addWidget(self.arabic, 1, 0, 1, 1)
        grid.addWidget(self.hebrew, 2, 0, 1, 1)
        grid.addWidget(self.transcription, 3, 0, 1, 1)
        grid.addWidget(self.record_btn, 4, 0, 1, 1)
        grid.addWidget(self.voice, 5, 0, 1, 1)
        grid.addWidget(self.keywords, 6, 0, 1, 1)
        grid.addWidget(self.done, 7, 1, 1, 1)
        grid.addWidget(self.enter, 7, 0, 1, 1)
        grid.addWidget(self.add_response, 8, 0, 1, 1)
        # grid.addWidget(self.advance,8,1,1,1)

        self.add_response.clicked.connect(self.continues_talking)

        self.setLayout(grid)
        self.keepRecording = True
        self.button_state = 'record'
        self.recorder = Recorder(channels=2, rate=16000, frames_per_buffer=1024)
        self.record_btn.clicked.connect(self.on_click)
        self.voice.clicked.connect(self.play_sound)

    def continues_talking(self):
        global index, window
        window = SentenceWindow(parent=index)
        index += 1
        window.parent_voice.show()
        window.show()

    def create_sentence(self):
        keyword = self.keywords.text().split(", ")
        keyword.remove("")
        sentences[str(index)] = {"id_": str(index), "arabic": self.arabic.text(),
                                 "arabicWithoutDiacritics": self.arabic.text()
            , "hebrew": self.hebrew.text(), "transcription": self.transcription.text(),
                                 "voiceRecPath": "test_" + str(index) + ".wav",
                                 "keywords": keyword}
        self.done.setEnabled(True)
        self.enter.setEnabled(False)
        self.record_btn.setEnabled(False)
        self.add_response.setEnabled(True)

    def finish(self):
        if self.parent is None:
            content["flow"] = flow
            content["sentences"] = sentences
            json_object = json.dumps(content, indent=4, ensure_ascii=False)

            with open("conversation.json", "w") as outfile:
                outfile.write(json_object)
            sys.exit()
        else:
            self.close()

    def play_sound(self):
        self.full_file_path = os.path.join(os.getcwd(), 'test.wav')
        self.url = QUrl.fromLocalFile(self.full_file_path)
        self.sound = AudioSegment.from_wav("test_" + str(index) + ".wav")
        play(self.sound)

    def on_click(self):
        if self.button_state == 'record':
            self.recFile = self.recorder.open('test_' + str(index) + '.wav', 'wb')
            self.recFile.start_recording()
            self.record_btn.setText("Stop")
            self.button_state = 'stop'
            self.voice.setEnabled(False)
        else:
            self.recFile.stop_recording()
            self.record_btn.setText("Record")
            self.button_state = 'record'
            self.voice.setEnabled(True)
            # self.clear_texts()


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
        self.next_button.clicked.connect(self.next_window)

    def next_window(self):
        adder.show()
        content["id"] = "mock-script"
        content["title"] = self.title_box.text()
        content["description"] = self.description_box.text()
        content["photo"] = self.photo_box.text()
        content["level"] = int(self.level_box.text())
        content["category"] = self.category_box.text()
        content["createdBy"] = self.createdBy_box.text()
        content["start"] = str(index)
        self.hide()
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
        self.close()

    # def clicked_existing(self):


app = QApplication(sys.argv)
editor = EditorWindow()
adder = SentenceWindow()
window = MainWindow()
window.show()
app.exec()

f = open("conversation.json", "w+")

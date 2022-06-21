from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
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
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Madrasa Editor')
        self.setWindowIcon(QIcon("madrasa.png"))
        self.setGeometry(500, 300, 550, 300)

        self.choose()

    def choose(self):
        btn_1 = QPushButton("New Conversation", self)
        btn_2 = QPushButton("Existing Conversation", self)

        btn_1.setGeometry(50, 150, 200, 100)
        btn_2.setGeometry(300, 150, 200, 100)


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()

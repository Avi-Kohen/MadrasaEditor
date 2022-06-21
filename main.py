from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget
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
        self.setGeometry(500, 300, 400, 300)


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()

from PyQt6.QtWidgets import QApplication, QWidget

# Only needed for access to command line arguments
import sys

id = 1
#להוסיף לטעון קובץ או ליצור חדש
class Sentence():
    id = id
    voiceRecPath = ""
    keyword = []
    def __init__(self,arabic,hebrew,transcription):
        self.arabic = arabic
        self.hebrew = hebrew
        self.transcription = transcription


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QWidget()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.
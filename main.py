import sys
#from PyQt5.QtWidgets import QApplication
#from .database import createConnection
#from .views import Window
def main():
    app = QApplication(sys.argv)
    if not createConnection('contacts.sqlite'):
        sys.exit(1)
    win = Window()
    win.show()
    #run the event loop
    sys.exit(app.exec())

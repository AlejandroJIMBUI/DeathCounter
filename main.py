import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow,QFileDialog, QMessageBox)
from views.death_counter import DeathCounter

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DeathCounter()
    window.show()
    sys.exit(app.exec())
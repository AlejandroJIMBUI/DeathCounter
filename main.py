import sys
import json
from pathlib import Path
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLabel, QWidget, QFileDialog, QMessageBox)
from PyQt6.QtGui import QPixmap, QIcon, QAction
from PyQt6.QtCore import Qt

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).parent
    return str(base_path / relative_path)

class CounterWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.count = 0
        self.init_ui()
        
    def init_ui(self):
        self.layout = QVBoxLayout()
        
        # Logo/Título
        self.title_image = QLabel()
        self.title_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(resource_path("images/elondied.png"))
        pixmap = pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio)
        self.title_image.setPixmap(pixmap)    
        
        # Texto debajo de la imagen
        self.subtitle_label = QLabel("pendejo no dura nada")
        self.subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subtitle_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: #e74c3c;
                margin-bottom: 20px;
            }
        """)
        
        # Contador
        self.counter_label = QLabel("0")
        self.counter_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.counter_label.setStyleSheet("""
            QLabel {
                font-size: 72px;
                font-weight: bold;
                color: #e74c3c;
                margin: 30px 0;
            }
        """)
        
        # Botones
        self.btn_layout = QHBoxLayout()
        
        self.decrement_btn = QPushButton("-")
        self.decrement_btn.clicked.connect(self.decrement)
        self.decrement_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 15px;
                border-radius: 10px;
                font-size: 24px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        
        self.increment_btn = QPushButton("+")
        self.increment_btn.clicked.connect(self.increment)
        self.increment_btn.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                border: none;
                padding: 15px;
                border-radius: 10px;
                font-size: 24px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        
        # Footer
        self.footer_label = QLabel("DeathCounter 2000™ by IngAlejandroJim")
        self.footer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.footer_label.setStyleSheet("font-size: 10px; margin-top: 20px;")
        
        # Añadir widgets al layout
        self.btn_layout.addWidget(self.decrement_btn)
        self.btn_layout.addWidget(self.increment_btn)
        
        self.layout.addWidget(self.title_image)
        self.layout.addWidget(self.subtitle_label)  # Añadir el nuevo texto aquí
        self.layout.addWidget(self.counter_label)
        self.layout.addLayout(self.btn_layout)
        self.layout.addWidget(self.footer_label)
        
        self.setLayout(self.layout)
    
    def increment(self):
        self.count += 1
        self.update_counter()
    
    def decrement(self):
        if self.count > 0:
            self.count -= 1
            self.update_counter()
    
    def update_counter(self):
        self.counter_label.setText(str(self.count))
    
    def get_count(self):
        return self.count
    
    def set_count(self, value):
        self.count = value
        self.update_counter()

class DeathCounter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DeathCounter 2000™")
        self.setGeometry(100, 100, 400, 500)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2c3e50;
                color: white;
            }
        """)
        self.setWindowIcon(QIcon(resource_path("images/DeathCounter_icon.ico")))
        
        self.counter_widget = CounterWidget()
        self.setCentralWidget(self.counter_widget)
        
        self.init_menu()
    
    def init_menu(self):
        menubar = self.menuBar()
        
        # Menú Archivo
        file_menu = menubar.addMenu("Archivo")
        
        save_action = QAction("Guardar sesión", self)
        save_action.triggered.connect(self.save_session)
        file_menu.addAction(save_action)
        
        load_action = QAction("Cargar sesión", self)
        load_action.triggered.connect(self.load_session)
        file_menu.addAction(load_action)
        
        exit_action = QAction("Salir", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
    
    def save_session(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self, 
            "Guardar Sesión", 
            "", 
            "JSON Files (*.json)"
        )
        
        if file_name:
            data = {"count": self.counter_widget.get_count()}
            try:
                with open(file_name, 'w') as f:
                    json.dump(data, f)
                QMessageBox.information(self, "melo", "tranquilo que eso esta guardao")
            except Exception as e:
                QMessageBox.critical(self, "F", f"preocupese por que no se guardo: {str(e)}")
    
    def load_session(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Cargar Sesión",
            "",
            "JSON Files (*.json)"
        )
        
        if file_name:
            try:
                with open(file_name, 'r') as f:
                    data = json.load(f)
                self.counter_widget.set_count(data.get("count", 0))
                QMessageBox.information(self, "melo", "tranquilo que eso se cargo")
            except Exception as e:
                QMessageBox.critical(self, "F", f"preocupese por que eso no se cargo: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DeathCounter()
    window.show()
    sys.exit(app.exec())
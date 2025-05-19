from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLabel, QWidget, QFileDialog, QMessageBox)
from PyQt6.QtGui import QPixmap, QIcon, QAction
from PyQt6.QtCore import Qt
from utils.helpers import resource_path

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
        pixmap = QPixmap("images/elondied.png")
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
        
        # Añadir widgets al layout
        self.btn_layout.addWidget(self.decrement_btn)
        self.btn_layout.addWidget(self.increment_btn)
        
        self.layout.addWidget(self.title_image)
        self.layout.addWidget(self.subtitle_label)  # Añadir el nuevo texto aquí
        self.layout.addWidget(self.counter_label)
        self.layout.addLayout(self.btn_layout)
        
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

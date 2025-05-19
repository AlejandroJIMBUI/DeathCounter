import json
from PyQt6.QtWidgets import (QMainWindow,QFileDialog, QMessageBox)
from PyQt6.QtGui import QIcon, QAction

from models.counter_widget import CounterWidget
from utils.helpers import resource_path

class DeathCounter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DeathCounter")
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
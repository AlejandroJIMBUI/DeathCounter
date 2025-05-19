import sys  
from pathlib import Path

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).parent.parent  # Subir un nivel más
    return str(base_path / relative_path)

import requests

from .layout import main_window_layout
r = requests.get("http://localhost:5000/notes")

class add_notes(main_window_layout):
    def __init__(self):
        super().__init__(None)
        

import json
import os

class FileManager:
    def __init__(self, filename="data.json"):
        self.filename = filename

    def load_data(self):
        if not os.path.exists(self.filename):
            return {"income": [], "expenses": []}

        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            # File exists but is empty or corrupted
            return {"income": [], "expenses": []}

    def save_data(self, data):
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

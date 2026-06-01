import json
import os

class PasswordVault:
    def __init__(self):
        # التعديل هنا: بنخلي البرنامج يعرف مكان فولدر data بالنسبة لمكان الملف ده
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(base_dir, "..", "data", "passwords.json")

        # التأكد إن الفولدر موجود، ولو مش موجود يعمله
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        # لو الملف مش موجود، يعمله ويحط فيه قائمة فاضية
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as file:
                json.dump([], file)

    def load_data(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_data(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def add_password(self, website, username, password):
        data = self.load_data()
        new_entry = {
            "website": website,
            "username": username,
            "password": password
        }
        data.append(new_entry)
        self.save_data(data)

    def view_passwords(self):
        return self.load_data()

    def search_password(self, website):
        data = self.load_data()
        return [entry for entry in data if entry["website"].lower() == website.lower()]

    def update_password(self, website, new_username=None, new_password=None):
        data = self.load_data()
        updated = False
        for entry in data:
            if entry["website"].lower() == website.lower():
                if new_username: entry["username"] = new_username
                if new_password: entry["password"] = new_password
                updated = True
        if updated:
            self.save_data(data)
        return updated

    def delete_password(self, website):
        data = self.load_data()
        new_data = [entry for entry in data if entry["website"].lower() != website.lower()]
        if len(new_data) < len(data):
            self.save_data(new_data)
            return True
        return False
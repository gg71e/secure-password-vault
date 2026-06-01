import tkinter as tk
from tkinter import messagebox
import random
import string

from storage import PasswordVault
from security_engine import SecurityEngine

class AddPasswordPage:

    def __init__(self, parent):

        self.parent = parent

        self.vault = PasswordVault()
        self.security = SecurityEngine()

        container = tk.Frame(parent, bg="#07111f")
        container.pack(fill="both", expand=True)

        tk.Label(
            container,
            text="Add New Password",
            font=("Arial", 26, "bold"),
            bg="#07111f",
            fg="#60a5fa"
        ).pack(pady=25)

        main_frame = tk.Frame(
            container,
            bg="#0f172a",
            width=650,
            height=600
        )
        main_frame.pack(pady=10)
        main_frame.pack_propagate(False)

        # Website
        tk.Label(main_frame, text="Website",
                 bg="#0f172a", fg="white").pack()

        self.website_entry = tk.Entry(main_frame)
        self.website_entry.pack(ipady=6)

        # Username
        tk.Label(main_frame, text="Username",
                 bg="#0f172a", fg="white").pack()

        self.username_entry = tk.Entry(main_frame)
        self.username_entry.pack(ipady=6)

        # Password
        tk.Label(main_frame, text="Password",
                 bg="#0f172a", fg="white").pack()

        self.password_entry = tk.Entry(main_frame, show="*")
        self.password_entry.pack(ipady=6)

        self.show_password = tk.BooleanVar()

        tk.Checkbutton(
            main_frame,
            text="Show Password",
            variable=self.show_password,
            command=self.toggle_password,
            bg="#0f172a",
            fg="white"
        ).pack()

        self.strength_label = tk.Label(main_frame, text="", bg="#0f172a", fg="white")
        self.strength_label.pack()

        btn_frame = tk.Frame(main_frame, bg="#0f172a")
        btn_frame.pack(pady=20)

        tk.Button(
            btn_frame,
            text="Save",
            command=self.save_password,
            bg="#2563eb",
            fg="white"
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            btn_frame,
            text="Generate",
            command=self.generate_password,
            bg="#0ea5e9",
            fg="white"
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            btn_frame,
            text="Clear",
            command=self.clear_fields,
            bg="#dc2626",
            fg="white"
        ).grid(row=0, column=2, padx=5)

    # ================= TOGGLE =================
    def toggle_password(self):

        if self.show_password.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    # ================= GENERATE =================
    def generate_password(self):

        chars = string.ascii_letters + string.digits + string.punctuation

        pwd = "".join(random.choice(chars) for _ in range(12))

        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, pwd)

    # ================= CLEAR =================
    def clear_fields(self):

        self.website_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    # ================= SAVE (IMPORTANT) =================
    def save_password(self):

        website = self.website_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not website or not username or not password:
            messagebox.showerror("Error", "Fill all fields")
            return

        # 🔐 ENCRYPT PASSWORD
        encrypted = self.security.encrypt_password(password)

        # 💾 SAVE TO JSON
        self.vault.add_password(
            website,
            username,
            encrypted
        )

        messagebox.showinfo("Success", "Saved successfully 🔐")

        self.clear_fields()
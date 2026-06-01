import tkinter as tk
from tkinter import messagebox
import random
import string


class GeneratePasswordPage:

    def __init__(self, parent):

        self.parent = parent

        container = tk.Frame(
            parent,
            bg="#07111f"
        )

        container.pack(fill="both", expand=True)

        title = tk.Label(
            container,
            text="Strong Password Generator",
            font=("Arial", 26, "bold"),
            bg="#07111f",
            fg="#60a5fa"
        )

        title.pack(pady=25)

        main_frame = tk.Frame(
            container,
            bg="#0f172a",
            width=600,
            height=600
        )

        main_frame.pack(pady=20)

        main_frame.pack_propagate(False)
        length_label = tk.Label(
            main_frame,
            text="Password Length",
            font=("Arial", 13, "bold"),
            bg="#0f172a",
            fg="white"
        )

        length_label.pack(pady=(30, 10))

        self.length_spinbox = tk.Spinbox(
            main_frame,
            from_=6,
            to=32,
            width=10,
            font=("Arial", 13),
            bg="#1e293b",
            fg="white",
            buttonbackground="#2563eb"
        )

        self.length_spinbox.pack(ipady=5)
        options_frame = tk.Frame(
            main_frame,
            bg="#0f172a"
        )

        options_frame.pack(pady=20)

        self.uppercase_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)

        uppercase_check = tk.Checkbutton(
            options_frame,
            text="Uppercase",
            variable=self.uppercase_var,
            bg="#0f172a",
            fg="white",
            selectcolor="#0f172a",
            activebackground="#0f172a",
            activeforeground="white",
            font=("Arial", 11)
        )

        uppercase_check.grid(row=0, column=0, padx=10)

        numbers_check = tk.Checkbutton(
            options_frame,
            text="Numbers",
            variable=self.numbers_var,
            bg="#0f172a",
            fg="white",
            selectcolor="#0f172a",
            activebackground="#0f172a",
            activeforeground="white",
            font=("Arial", 11)
        )

        numbers_check.grid(row=0, column=1, padx=10)

        symbols_check = tk.Checkbutton(
            options_frame,
            text="Symbols",
            variable=self.symbols_var,
            bg="#0f172a",
            fg="white",
            selectcolor="#0f172a",
            activebackground="#0f172a",
            activeforeground="white",
            font=("Arial", 11)
        )

        symbols_check.grid(row=0, column=2, padx=10)
        output_label = tk.Label(
            main_frame,
            text="Generated Password",
            font=("Arial", 13, "bold"),
            bg="#0f172a",
            fg="white"
        )

        output_label.pack(pady=(20, 10))

        self.password_entry = tk.Entry(
            main_frame,
            width=35,
            font=("Arial", 15),
            bg="#1e293b",
            fg="#60a5fa",
            insertbackground="white",
            relief="flat",
            justify="center"
        )

        self.password_entry.pack(ipady=8)
        self.strength_label = tk.Label(
            main_frame,
            text="",
            font=("Arial", 13, "bold"),
            bg="#0f172a",
            fg="white"
        )

        self.strength_label.pack(pady=15)
        buttons_frame = tk.Frame(
            main_frame,
            bg="#0f172a"
        )

        buttons_frame.pack(pady=20)

        # GENERATE BUTTON
        generate_btn = tk.Button(
            buttons_frame,
            text="Generate",
            font=("Arial", 12, "bold"),
            bg="#2563eb",
            fg="white",
            relief="flat",
            width=15,
            cursor="hand2",
            command=self.generate_password
        )

        generate_btn.grid(row=0, column=0, padx=10, ipady=6)
        copy_btn = tk.Button(
            buttons_frame,
            text="Copy",
            font=("Arial", 12, "bold"),
            bg="#22c55e",
            fg="white",
            relief="flat",
            width=15,
            cursor="hand2",
            command=self.copy_password
        )

        copy_btn.grid(row=0, column=1, padx=10, ipady=6)
        clear_btn = tk.Button(
            buttons_frame,
            text="Clear",
            font=("Arial", 12, "bold"),
            bg="#dc2626",
            fg="white",
            relief="flat",
            width=15,
            cursor="hand2",
            command=self.clear_password
        )

        clear_btn.grid(row=0, column=2, padx=10, ipady=6)
    def generate_password(self):

        length = int(self.length_spinbox.get())

        characters = string.ascii_lowercase

        if self.uppercase_var.get():

            characters += string.ascii_uppercase

        if self.numbers_var.get():

            characters += string.digits

        if self.symbols_var.get():

            characters += string.punctuation

        password = "".join(
            random.choice(characters)
            for _ in range(length)
        )

        self.password_entry.delete(0, tk.END)

        self.password_entry.insert(0, password)

        self.check_strength(password)
    def check_strength(self, password):

        score = 0

        if len(password) >= 8:
            score += 1

        if any(char.isupper() for char in password):
            score += 1

        if any(char.isdigit() for char in password):
            score += 1

        if any(char in string.punctuation for char in password):
            score += 1

        # RESULT
        if score <= 2:

            self.strength_label.config(
                text="Weak Password",
                fg="#dc2626"
            )

        elif score == 3:

            self.strength_label.config(
                text="Medium Password",
                fg="#f59e0b"
            )

        else:

            self.strength_label.config(
                text="Strong Password",
                fg="#22c55e"
            )
    def copy_password(self):

        password = self.password_entry.get()

        if password == "":

            messagebox.showerror(
                "Error",
                "Generate password first"
            )

        else:

            self.parent.clipboard_clear()

            self.parent.clipboard_append(password)

            messagebox.showinfo(
                "Copied",
                "Password copied successfully"
            )
    def clear_password(self):

        self.password_entry.delete(0, tk.END)

        self.strength_label.config(text="")
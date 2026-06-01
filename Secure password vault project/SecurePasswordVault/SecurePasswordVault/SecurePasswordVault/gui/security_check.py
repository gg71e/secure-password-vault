import tkinter as tk
from tkinter import messagebox
import string


class SecurityCheckPage:

    def __init__(self, parent):

        self.parent = parent

        container = tk.Frame(
            parent,
            bg="#07111f"
        )

        container.pack(fill="both", expand=True)
        title = tk.Label(
            container,
            text="Password Security Analyzer",
            font=("Arial", 26, "bold"),
            bg="#07111f",
            fg="#60a5fa"
        )

        title.pack(pady=25)
        main_frame = tk.Frame(
            container,
            bg="#0f172a",
            width=650,
            height=520
        )

        main_frame.pack(pady=10)

        main_frame.pack_propagate(False)
        password_label = tk.Label(
            main_frame,
            text="Enter Password",
            font=("Arial", 13, "bold"),
            bg="#0f172a",
            fg="white"
        )

        password_label.pack(pady=(35, 10))
        self.password_entry = tk.Entry(
            main_frame,
            width=35,
            font=("Arial", 15),
            bg="#1e293b",
            fg="white",
            insertbackground="white",
            relief="flat",
            show="*"
        )

        self.password_entry.pack(ipady=8)
        self.show_password = tk.BooleanVar()

        show_btn = tk.Checkbutton(
            main_frame,
            text="Show Password",
            variable=self.show_password,
            command=self.toggle_password,
            bg="#0f172a",
            fg="white",
            activebackground="#0f172a",
            activeforeground="white",
            selectcolor="#0f172a",
            font=("Arial", 11)
        )

        show_btn.pack(pady=12)
        check_btn = tk.Button(
            main_frame,
            text="Analyze Password",
            font=("Arial", 12, "bold"),
            bg="#2563eb",
            fg="white",
            relief="flat",
            width=20,
            cursor="hand2",
            command=self.check_strength
        )

        check_btn.pack(ipady=6)
        self.result_label = tk.Label(
            main_frame,
            text="",
            font=("Arial", 20, "bold"),
            bg="#0f172a",
            fg="white"
        )

        self.result_label.pack(pady=(25, 10))
        self.score_label = tk.Label(
            main_frame,
            text="Security Score: 0 / 5",
            font=("Arial", 13, "bold"),
            bg="#0f172a",
            fg="#cbd5e1"
        )

        self.score_label.pack(pady=(0, 20))
        tips_frame = tk.Frame(
            main_frame,
            bg="#1e293b",
            width=500,
            height=150
        )

        tips_frame.pack(pady=10)

        tips_frame.pack_propagate(False)

        tips_title = tk.Label(
            tips_frame,
            text="Security Recommendations",
            font=("Arial", 13, "bold"),
            bg="#1e293b",
            fg="#60a5fa"
        )

        tips_title.pack(pady=(15, 10))

        self.tips_label = tk.Label(
            tips_frame,
            text=(
                "• Use uppercase letters\n"
                "• Use numbers and symbols\n"
                "• Use at least 12 characters"
            ),
            font=("Arial", 11),
            bg="#1e293b",
            fg="white",
            justify="left"
        )

        self.tips_label.pack()
    def toggle_password(self):

        if self.show_password.get():

            self.password_entry.config(show="")

        else:

            self.password_entry.config(show="*")
    def check_strength(self):

        password = self.password_entry.get()

        score = 0

        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)
        has_number = any(char.isdigit() for char in password)
        has_symbol = any(char in string.punctuation for char in password)

        if len(password) >= 8:
            score += 1

        if has_upper:
            score += 1

        if has_lower:
            score += 1

        if has_number:
            score += 1

        if has_symbol:
            score += 1
        self.score_label.config(
            text=f"Security Score: {score} / 5"
        )
        if score <= 2:

            self.result_label.config(
                text="Weak Password",
                fg="#dc2626"
            )

        elif score == 3 or score == 4:

            self.result_label.config(
                text="Medium Password",
                fg="#f59e0b"
            )

        else:

            self.result_label.config(
                text="Strong Password",
                fg="#22c55e"
            )
        tips = []

        if len(password) < 12:
            tips.append("• Use at least 12 characters")

        if not has_upper:
            tips.append("• Add uppercase letters")

        if not has_number:
            tips.append("• Add numbers")

        if not has_symbol:
            tips.append("• Add symbols")

        if len(tips) == 0:
            tips.append("• Excellent password security")

        self.tips_label.config(
            text="\n".join(tips)
        )
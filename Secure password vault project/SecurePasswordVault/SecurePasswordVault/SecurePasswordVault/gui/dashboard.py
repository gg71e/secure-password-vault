import tkinter as tk
from storage import PasswordVault

from gui.add_password import AddPasswordPage
from gui.view_passwords import ViewPasswordsPage
from gui.generate_password import GeneratePasswordPage
from gui.security_check import SecurityCheckPage


class DashboardWindow:

    def __init__(self, root):

        self.root = root

        self.root.title("Dashboard")
        self.root.geometry("1200x650")
        self.root.resizable(False, False)
        self.root.config(bg="#07111f")
        sidebar = tk.Frame(
            root,
            bg="#0f172a",
            width=240
        )

        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        logo = tk.Label(
            sidebar,
            text="PASSWORD\nVAULT",
            font=("Arial", 24, "bold"),
            bg="#0f172a",
            fg="#60a5fa",
            justify="center"
        )

        logo.pack(pady=40)

        self.create_sidebar_button(sidebar, "Add Password", self.open_add_password)
        self.create_sidebar_button(sidebar, "View Passwords", self.open_view_passwords)
        self.create_sidebar_button(sidebar, "Generate Password", self.open_generate_password)
        self.create_sidebar_button(sidebar, "Security Check", self.open_security_check)
        self.create_sidebar_button(sidebar, "Logout", self.logout)
        self.content = tk.Frame(root, bg="#07111f")
        self.content.pack(fill="both", expand=True)

        self.show_home()
    def show_home(self):

        self.clear_content()

        vault = PasswordVault()
        data = vault.view_passwords()
        count = len(data)

        welcome = tk.Label(
            self.content,
            text="Welcome Back",
            font=("Arial", 32, "bold"),
            bg="#07111f",
            fg="white"
        )
        welcome.pack(pady=(60, 10))

        subtitle = tk.Label(
            self.content,
            text="Your cybersecurity dashboard is active and secure.",
            font=("Arial", 15),
            bg="#07111f",
            fg="#94a3b8"
        )
        subtitle.pack()

        cards_frame = tk.Frame(self.content, bg="#07111f")
        cards_frame.pack(pady=50)

        self.create_card(cards_frame, "Stored Passwords", str(count))
        self.create_card(cards_frame, "Security Level", "HIGH")
        self.create_card(cards_frame, "Encryption", "AES")

    def create_sidebar_button(self, parent, text, command):

        btn = tk.Button(
            parent,
            text=text,
            font=("Arial", 12, "bold"),
            bg="#1e293b",
            fg="white",
            relief="flat",
            activebackground="#2563eb",
            activeforeground="white",
            width=18,
            pady=10,
            cursor="hand2",
            command=command
        )

        btn.pack(pady=10)

        btn.bind("<Enter>", lambda e: btn.config(bg="#2563eb"))
        btn.bind("<Leave>", lambda e: btn.config(bg="#1e293b"))
    def create_card(self, parent, title, value):

        card = tk.Frame(
            parent,
            bg="#0f172a",
            width=200,
            height=160
        )

        card.pack(side="left", padx=20)
        card.pack_propagate(False)

        title_label = tk.Label(
            card,
            text=title,
            font=("Arial", 14, "bold"),
            bg="#0f172a",
            fg="#94a3b8"
        )
        title_label.pack(pady=(35, 15))

        value_label = tk.Label(
            card,
            text=value,
            font=("Arial", 28, "bold"),
            bg="#0f172a",
            fg="#60a5fa"
        )
        value_label.pack()
    def clear_content(self):

        for widget in self.content.winfo_children():
            widget.destroy()
    def open_add_password(self):
        self.clear_content()
        AddPasswordPage(self.content)

    def open_view_passwords(self):
        self.clear_content()
        ViewPasswordsPage(self.content)

    def open_generate_password(self):
        self.clear_content()
        GeneratePasswordPage(self.content)

    def open_security_check(self):
        self.clear_content()
        SecurityCheckPage(self.content)

    def logout(self):
        self.root.destroy()
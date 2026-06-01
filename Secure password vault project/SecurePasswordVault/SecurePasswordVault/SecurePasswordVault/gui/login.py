import tkinter as tk
from tkinter import messagebox

from gui.dashboard import DashboardWindow


class LoginWindow:

    def __init__(self, root):

        self.root = root

        self.root.title("Secure Password Vault")
        self.root.geometry("950x600")
        self.root.config(bg="#07111f")
        self.root.resizable(False, False)


        left_frame = tk.Frame(
            root,
            bg="#0f172a",
            width=400
        )

        left_frame.pack(side="left", fill="y")

        # Logo
        logo = tk.Label(
            left_frame,
            text="PASSWORD\nVAULT",
            font=("Arial", 30, "bold"),
            bg="#0f172a",
            fg="#60a5fa",
            justify="center"
        )

        logo.pack(pady=(180, 20))

        # Description
        description = tk.Label(
            left_frame,
            text=(
                "Secure your digital accounts\n"
                "with advanced password protection\n"
                "and cybersecurity tools."
            ),
            font=("Arial", 13),
            bg="#0f172a",
            fg="#cbd5e1",
            justify="center"
        )

        description.pack()


        right_frame = tk.Frame(
            root,
            bg="#07111f"
        )

        right_frame.pack(expand=True)

        # Welcome
        welcome = tk.Label(
            right_frame,
            text="Welcome Back",
            font=("Arial", 28, "bold"),
            bg="#07111f",
            fg="white"
        )

        welcome.pack(pady=(120, 10))

        subtitle = tk.Label(
            right_frame,
            text="Login to access your secure vault",
            font=("Arial", 13),
            bg="#07111f",
            fg="#94a3b8"
        )

        subtitle.pack(pady=(0, 40))


        password_label = tk.Label(
            right_frame,
            text="Master Password :",
            font=("Arial", 14, "bold"),
            bg="#07111f",
            fg="white"
        )

        password_label.pack(pady=(10, 10))


        self.password_entry = tk.Entry(
            right_frame,
            width=34,
            font=("Arial", 14),
            bg="#1e293b",
            fg="white",
            insertbackground="white",
            relief="flat",
            show="*"
        )

        self.password_entry.pack(ipady=8)

        # ENTER KEY
        self.password_entry.bind(
            "<Return>",
            lambda event: self.login()
        )


        self.show_password = tk.BooleanVar()

        show_btn = tk.Checkbutton(
            right_frame,
            text="Show Password",
            variable=self.show_password,
            command=self.toggle_password,
            bg="#07111f",
            fg="white",
            activebackground="#07111f",
            activeforeground="white",
            selectcolor="#07111f",
            font=("Arial", 11)
        )

        show_btn.pack(pady=15)


        self.error_label = tk.Label(
            right_frame,
            text="",
            font=("Arial", 11, "bold"),
            bg="#07111f",
            fg="#dc2626"
        )

        self.error_label.pack()


        login_btn = tk.Button(
            right_frame,
            text="LOGIN",
            font=("Arial", 13, "bold"),
            bg="#2563eb",
            fg="white",
            relief="flat",
            width=20,
            cursor="hand2",
            command=self.login
        )

        login_btn.pack(pady=25, ipady=8)

        # Hover Effect
        login_btn.bind(
            "<Enter>",
            lambda e: login_btn.config(bg="#3b82f6")
        )

        login_btn.bind(
            "<Leave>",
            lambda e: login_btn.config(bg="#2563eb")
        )


        footer = tk.Label(
            right_frame,
            text="Secure Password Vault © 2026",
            font=("Arial", 10),
            bg="#07111f",
            fg="#64748b"
        )

        footer.pack(side="bottom", pady=20)


    def toggle_password(self):

        if self.show_password.get():

            self.password_entry.config(show="")

        else:

            self.password_entry.config(show="*")


    def login(self):

        password = self.password_entry.get()

        # TEMP PASSWORD
        if password == "admin123":

            self.root.destroy()

            dashboard_root = tk.Tk()

            DashboardWindow(dashboard_root)

            dashboard_root.mainloop()

        else:

            self.error_label.config(
                text="Incorrect Master Password"
            )

            self.password_entry.delete(0, tk.END)
import tkinter as tk
from tkinter import ttk, messagebox

from storage import PasswordVault
from security.security_engine import SecurityEngine


class ViewPasswordsPage:

    def __init__(self, parent):

        self.parent = parent

        # ================= BACKEND =================
        self.vault = PasswordVault()
        self.security = SecurityEngine()

        # ================= UI =================
        container = tk.Frame(parent, bg="#07111f")
        container.pack(fill="both", expand=True)

        tk.Label(
            container,
            text="Stored Passwords",
            font=("Arial", 26, "bold"),
            bg="#07111f",
            fg="#60a5fa"
        ).pack(pady=20)

        # ================= SEARCH =================
        search_frame = tk.Frame(container, bg="#07111f")
        search_frame.pack(pady=10)

        self.search_entry = tk.Entry(
            search_frame,
            width=40,
            font=("Arial", 12),
            bg="#1e293b",
            fg="white",
            insertbackground="white",
            relief="flat"
        )
        self.search_entry.grid(row=0, column=0, padx=10, ipady=7)

        tk.Button(
            search_frame,
            text="Search",
            bg="#2563eb",
            fg="white",
            command=self.search_password
        ).grid(row=0, column=1, padx=10)

        tk.Button(
            search_frame,
            text="Refresh",
            bg="#0ea5e9",
            fg="white",
            command=self.load_passwords
        ).grid(row=0, column=2, padx=10)

        # ================= TABLE =================
        table_frame = tk.Frame(container, bg="#07111f")
        table_frame.pack(pady=20)

        self.password_table = ttk.Treeview(
            table_frame,
            columns=("Website", "Username", "Password"),
            show="headings",
            height=12
        )

        self.password_table.heading("Website", text="Website")
        self.password_table.heading("Username", text="Username")
        self.password_table.heading("Password", text="Password")

        self.password_table.column("Website", width=220)
        self.password_table.column("Username", width=240)
        self.password_table.column("Password", width=220)

        self.password_table.pack()

        # ================= BUTTONS =================
        btn_frame = tk.Frame(container, bg="#07111f")
        btn_frame.pack(pady=25)

        tk.Button(
            btn_frame,
            text="View",
            bg="#2563eb",
            fg="white",
            width=12,
            command=self.view_password
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            btn_frame,
            text="Delete",
            bg="#dc2626",
            fg="white",
            width=12,
            command=self.delete_password
        ).grid(row=0, column=1, padx=10)

        tk.Button(
            btn_frame,
            text="Copy",
            bg="#22c55e",
            fg="white",
            width=12,
            command=self.copy_password
        ).grid(row=0, column=2, padx=10)

        # ================= LOAD DATA =================
        self.load_passwords()

    # ================= LOAD FROM JSON =================
    def load_passwords(self):

        for item in self.password_table.get_children():
            self.password_table.delete(item)

        data = self.vault.view_passwords()

        for entry in data:
            self.password_table.insert(
                "",
                "end",
                values=(
                    entry["website"],
                    entry["username"],
                    "********"
                )
            )

    # ================= VIEW =================
    def view_password(self):

        selected = self.password_table.focus()

        if not selected:
            messagebox.showerror("Error", "Select a password first")
            return

        values = self.password_table.item(selected)["values"]
        website = values[0]

        data = self.vault.search_password(website)

        if not data:
            messagebox.showerror("Error", "Not found")
            return

        decrypted = self.security.decrypt_password(data[0]["password"])

        messagebox.showinfo(
            "Password Details",
            f"Website: {data[0]['website']}\n"
            f"Username: {data[0]['username']}\n"
            f"Password: {decrypted}"
        )

    # ================= DELETE =================
    def delete_password(self):

        selected = self.password_table.focus()

        if not selected:
            messagebox.showerror("Error", "Select a password first")
            return

        values = self.password_table.item(selected)["values"]
        website = values[0]

        self.vault.delete_password(website)
        self.load_passwords()

        messagebox.showinfo("Deleted", "Password deleted successfully")

    # ================= COPY =================
    def copy_password(self):

        selected = self.password_table.focus()

        if not selected:
            messagebox.showerror("Error", "Select a password first")
            return

        values = self.password_table.item(selected)["values"]
        website = values[0]

        data = self.vault.search_password(website)

        if not data:
            return

        decrypted = self.security.decrypt_password(data[0]["password"])

        self.parent.clipboard_clear()
        self.parent.clipboard_append(decrypted)

        messagebox.showinfo("Copied", "Password copied successfully")

    # ================= SEARCH =================
    def search_password(self):

        text = self.search_entry.get().lower()

        for item in self.password_table.get_children():

            values = self.password_table.item(item)["values"]
            website = values[0].lower()

            if text in website:
                self.password_table.selection_set(item)
                self.password_table.focus(item)
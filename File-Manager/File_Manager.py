import os
import shutil
import customtkinter as ctk
from tkinter import filedialog, messagebox

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")

class FileManager(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("File Manager")
        self.geometry("700x500")

        self.selected_file = None  

        self.search_entry = ctk.CTkEntry(self, placeholder_text="Suchbegriff eingeben...")
        self.search_entry.pack(pady=10, padx=20, fill="x")

        self.search_button = ctk.CTkButton(self, text="Suchen", command=self.search_files)
        self.search_button.pack(pady=5)

        self.result_listbox = ctk.CTkTextbox(self, height=15)
        self.result_listbox.pack(pady=10, padx=20, fill="both", expand=True)
        self.result_listbox.bind("<ButtonRelease-1>", self.select_file)

        self.delete_button = ctk.CTkButton(self, text="Löschen", fg_color="red", command=self.delete_file)
        self.delete_button.pack(pady=5)

        self.move_button = ctk.CTkButton(self, text="Verschieben", command=self.move_file)
        self.move_button.pack(pady=5)

        self.selected_file_label = ctk.CTkLabel(self, text="Ausgewählt: Keine")
        self.selected_file_label.pack(pady=5)

    def search_files(self):
        search_query = self.search_entry.get().strip()
        if not search_query:
            messagebox.showwarning("Fehler", "Bitte Suchbegriff eingeben!")
            return

        folder = filedialog.askdirectory(title="Ordner auswählen", initialdir=os.path.expanduser("~"))
        if not folder:
            return

        self.result_listbox.delete("0.0", "end")

        found_items = []
        for root, dirs, files in os.walk(folder):
            for name in files + dirs:
                if search_query.lower() in name.lower():
                    found_items.append(os.path.join(root, name))

        if found_items:
            for item in found_items:
                self.result_listbox.insert("end", f"{item}\n")
        else:
            self.result_listbox.insert("end", "Keine Ergebnisse gefunden.\n")

    def select_file(self, event=None):
        try:
            selected_line = self.result_listbox.get("insert linestart", "insert lineend").strip()
            if selected_line and "Keine Ergebnisse" not in selected_line:
                self.selected_file = selected_line
                self.selected_file_label.configure(text=f"Ausgewählt: {os.path.basename(self.selected_file)}")
        except Exception as e:
            print("Fehler bei der Auswahl:", e)

    def delete_file(self):
        if not self.selected_file:
            messagebox.showwarning("Fehler", "Bitte wählen Sie eine Datei aus!")
            return

        confirm = messagebox.askyesno("Löschen bestätigen", f"{os.path.basename(self.selected_file)} wirklich löschen?")
        if not confirm:
            return

        try:
            if os.path.isdir(self.selected_file):
                shutil.rmtree(self.selected_file)
            else:
                os.remove(self.selected_file)
            messagebox.showinfo("Erfolg", "Gelöscht!")
            self.selected_file_label.configure(text="Ausgewählt: Keine")
            self.result_listbox.delete("0.0", "end")
            self.selected_file = None
        except Exception as e:
            messagebox.showerror("Fehler", f"Löschen fehlgeschlagen: {e}")

    def move_file(self):
        if not self.selected_file:
            messagebox.showwarning("Fehler", "Bitte wählen Sie eine Datei aus!")
            return

        dest_folder = filedialog.askdirectory(title="Zielordner auswählen")
        if not dest_folder:
            return

        try:
            new_path = os.path.join(dest_folder, os.path.basename(self.selected_file))
            shutil.move(self.selected_file, new_path)
            messagebox.showinfo("Erfolg", "Verschoben!")
            self.selected_file_label.configure(text="Ausgewählt: Keine")
            self.result_listbox.delete("0.0", "end")
            self.selected_file = None
        except Exception as e:
            messagebox.showerror("Fehler", f"Verschieben fehlgeschlagen: {e}")

if __name__ == "__main__":
    app = FileManager()
    app.mainloop()

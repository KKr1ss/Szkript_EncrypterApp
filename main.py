import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

import EncryptionFileHandler

encryptionFileHandler = EncryptionFileHandler


def select_file():
    filetypes = (
        ('Minden fájl', '*.*'),
        ('Szöveges fájl', '*.txt')
    )

    filename = askopenfilename(
        title='Válassz egy fájlt',
        initialdir='/',
        filetypes=filetypes)

    if filename == "":
        if lbl_filePath["text"] == "":
            messagebox.showerror(title="Hiba", message="Válassz fájlt!")
        return

    encryptionFileHandler.setFile(filename)
    lbl_filePath.config(text=filename)

    ntr_key.delete(0, tk.END)
    ntr_key.insert(0, encryptionFileHandler.key)

    btn_setKey.config(state="normal")


def set_key():
    key = ntr_key.get()
    if key == "":
        ntr_key.delete(0, tk.END)
        ntr_key.insert(0, encryptionFileHandler.key)
        messagebox.showerror(title="Hiba", message="Nem lehet üres a kulcs!")
        return

    encryptionFileHandler.key = ntr_key.get()

    btn_encryptFile.config(state="normal")
    btn_decryptFile.config(state="normal")


def encrypt_file():
    try:
        newFilePath = encryptionFileHandler.createFile(False)
        messagebox.showinfo(title="Siker", message=f"A titkosított dokumentum sikeresen elkészült!\n{newFilePath}")
    except:
        messagebox.showerror(title="Hiba", message="A titkosítás sikertelen!")


def decrypt_file():
    try:
        newFilePath = encryptionFileHandler.createFile(True)
        messagebox.showinfo(title="Siker", message=f"A titkosított dokumentum sikeresen visszafejtve!\n{newFilePath}")
    except:
        messagebox.showerror(title="Hiba", message="A visszafejtés sikertelen!")


window = tk.Tk()
window.title("EncrypterApp")
window.resizable(False,False)
# FAJL UI ELEMENTEK

lbl_fileTitle = tk.Label(
    text='Aktuális fájl:'
)

lbl_filePath = tk.Label()

btn_openFileDialog = tk.Button(
    text='Fájl választás',
    command=select_file
)

# KULCS UI ELEMENTEK
lbl_key = tk.Label(
    text='Titkos kulcs:'
)

ntr_key = tk.Entry(
    width=50
)

btn_setKey = tk.Button(
    text='Kulcs beállítása',
    command=set_key,
    state="disable"
)

# TITKOSITAS UI ELEMENTEK
frm_encryptions = tk.Frame(
    master=window,
)

btn_encryptFile = tk.Button(
    master=frm_encryptions,
    text='Titkosítás',
    command=encrypt_file,
    state="disable",
    width=30
)

btn_decryptFile = tk.Button(
    master=frm_encryptions,
    text='Visszafejtés',
    command=decrypt_file,
    state="disable",
    width=30
)

lbl_fileTitle.grid(row=0, column=0, padx=5, pady=5, sticky="w")
lbl_filePath.grid(row=0, column=1, padx=5, pady=5, sticky="w")

btn_openFileDialog.grid(row=0, column=2, padx=5, pady=5, sticky="w")

lbl_key.grid(row=1, column=0, padx=5, pady=5)
ntr_key.grid(row=1, column=1, padx=5, pady=5)
btn_setKey.grid(row=1, column=2, padx=5, pady=5)

frm_encryptions.grid(row=2, column=0, padx=5, pady=5, columnspan=3)
btn_encryptFile.grid(row=0, column=0, padx=5, pady=5)
btn_decryptFile.grid(row=0, column=1, padx=5, pady=5)

window.mainloop()

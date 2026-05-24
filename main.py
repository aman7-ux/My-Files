import itertools
import string

import zipfile
import tkinter as tk
from tkinter import ttk
import threading

# إنشاء النافذة
root = tk.Tk()
root.title("Zip Password Cracker")
root.geometry("500x300")
root.resizable(False, False)
root.configure(bg="#1e1e1e")
root.eval('tk::PlaceWindow . center')

# إدخال اسم الملف
file_label = tk.Label(root, text="Enter ZIP file name:", font=("Arial", 12), fg="white", bg="#1e1e1e")
file_label.pack(pady=5)

file_entry = tk.Entry(root, font=("Arial", 12), width=30)
file_entry.pack(pady=5)

# نص التجربة
label = tk.Label(root, text="", font=("Arial", 14), fg="white", bg="#1e1e1e")
label.pack(pady=10)

# نص كلمة المرور عند العثور عليها
password_label = tk.Label(root, text="", font=("Arial", 18, "bold"), fg="green", bg="#1e1e1e")
password_label.pack()

# شريط التقدم
progress = ttk.Progressbar(root, length=300, mode="determinate")
progress.pack(pady=10)

# توقيع
footer = tk.Label(root, text="AMAN TestP0 | @AMAN XIT", font=("Arial", 10), fg="gray", bg="#1e1e1e")
footer.pack(side="bottom", pady=10)


# دالة البحث عن كلمة المرور
# دالة البحث عن كلمة المرور
def crack_zip(zip_filename):
    try:
        with zipfile.ZipFile(zip_filename, "r") as zip_file:
            chars = string.ascii_lowercase + string.digits
            
            for length in range(1, 13):
                for guess in itertools.product(chars, repeat=length):
                    password_str = "".join(guess)
                    
                    label.config(text=f"Trying: {password_str}")
                    root.update_idletasks()
                    
                    try:
                        zip_file.extractall(pwd=password_str.encode("utf-8"))
                        password_label.config(text=f"Password Found: {password_str}", fg="green")
                        return
                    except:
                        continue
            
            password_label.config(text="Password not found", fg="red")
            
    except FileNotFoundError:
        label.config(text="File not found!", fg="red")

# دالة البحث عن كلمة المرور
def crack_zip(zip_filename):
    try:
        with zipfile.ZipFile(zip_filename, "r") as zip_file:
            chars = string.ascii_lowercase + string.digits
            
            for guess in itertools.product(chars, repeat=4):
                password_str = "".join(guess)
                
                label.config(text=f"Trying: {password_str}")
                root.update_idletasks()
                
                try:
                    zip_file.extractall(pwd=password_str.encode("utf-8"))
                    password_label.config(text=f"Password Found: {password_str}", fg="green")
                    return
                except:
                    continue
            
            password_label.config(text="Password not found", fg="red")
            
    except FileNotFoundError:
        label.config(text="File not found!", fg="red")

# تشغيل عند الضغط على الزر
def start_cracking():
    zip_filename = file_entry.get().strip()
    if zip_filename == "":
        label.config(text="Please enter ZIP filename!", fg="red")
        return

    label.config(text="Starting...", fg="white")
    threading.Thread(target=crack_zip, args=(zip_filename,), daemon=True).start()


# زر البدء
start_button = tk.Button(root, text="Start", font=("Arial", 12), command=start_cracking, bg="#333", fg="white")
start_button.pack(pady=10)

root.mainloop()
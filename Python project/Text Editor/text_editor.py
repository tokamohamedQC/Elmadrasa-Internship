import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    file_path = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not file_path:
        return
    
    txt_edit.delete(1.0, tk.END)
    with open(file_path, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    
    window.title(f"Almadrasa Editor - {file_path}")

def save_file():
    file_path = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    
    if not file_path:
        return
    
    with open(file_path, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    
    window.title(f"Almadrasa Editor - {file_path}")
    
window = tk.Tk()
window.title("Almadrase editor")
window.rowconfigure(0, minsize=600)
window.columnconfigure(1,minsize=600)

txt_edit = tk.Text(window)
frame_buttons = tk.Frame(window, relief=tk.RAISED)
open_btn = tk.Button(frame_buttons, text="Open File", command=open_file)
save_btn = tk.Button(frame_buttons, text="Save File", command=save_file)

open_btn.grid(column=0 , row=0, sticky="ew", padx=5, pady=5)
save_btn.grid(column=0 , row=1, sticky="ew", padx=5)

frame_buttons.grid(column=0, row=0, sticky="ns")
txt_edit.grid(column=1, row=0, sticky="nsew")
window.mainloop()

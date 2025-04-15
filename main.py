from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Генератор пороля")
root.geometry("800x500")
position = {"padx":6, "pady":6, "anchor":NW}
 
spinbox = ttk.Spinbox(from_=1.0, to=100.0) # выбор длины пороля
spinbox.pack(anchor=NW)
print(spinbox)

numbers_var_enabled = IntVar()
special_var_enabled = IntVar()
spaces_var_enabled = IntVar()
  
numbers_var = ttk.Checkbutton(text="numbers_var", variable=numbers_var_enabled)
numbers_var.pack(padx=6, pady=6, anchor=NW)

special_var = ttk.Checkbutton(text="special_var", variable=special_var_enabled)
special_var.pack(padx=6, pady=6, anchor=NW)

spaces_var = ttk.Checkbutton(text="spaces_var", variable=spaces_var_enabled)
spaces_var.pack(padx=6, pady=6, anchor=NW)

# enabled_label = ttk.Label(textvariable=spaces_var_enabled) достать значения из пукчекбаттон
# enabled_label.pack(padx=6, pady=6, anchor=NW)

root.mainloop()

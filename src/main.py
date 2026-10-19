import tkinter as tk
from UI import construir_interfaz

def main():
    root = tk.Tk()
    construir_interfaz(root)
    root.mainloop()

if __name__ == "__main__":
    main()
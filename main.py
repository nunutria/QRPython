import tkinter as tk
from controlador.controladorQR import ControladorQR

if __name__ == '__main__':
    root = tk.Tk()
    app = ControladorQR(root)
    root.mainloop()
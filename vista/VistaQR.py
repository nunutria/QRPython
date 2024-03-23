import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk

class VistaQR:
    def __init__(self, master, controlador):
        self.master = master
        self.controlador = controlador
        self.frame = tk.Frame(self.master)
        
        self.etiqueta = tk.Label(self.frame, text="Ingresa la información para generar el código QR")
        self.etiqueta.pack(pady=10)
        
        self.caja_texto = tk.Entry(self.frame)
        self.caja_texto.pack(pady=10)
        
        self.boton_generar = tk.Button(self.frame, text="Generar", command=self.generar_qr)
        self.boton_generar.pack(pady=10)
        
        self.imagen_qr = tk.Label(self.frame)
        self.imagen_qr.pack(pady=10)
        
        self.frame.pack()
        
    def generar_qr(self):
        data = self.caja_texto.get()
        self.controlador.generar_qr(data)
        img = self.controlador.obtener_imagen()
        self.mostrar_imagen(img)
        
    def mostrar_imagen(self, img):
        img_tk = ImageTk.PhotoImage(img)
        self.imagen_qr.configure(image=img_tk)
        self.imagen_qr.image = img_tk
        
    def obtener_data(self):
        return self.caja_texto.get()
    
    def mostrar_error(self, mensaje):
        messagebox.showerror("Error", mensaje)
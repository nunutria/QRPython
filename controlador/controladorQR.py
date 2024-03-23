from modelo.modelo import ModeloQR
from vista.VistaQR import VistaQR

class ControladorQR:
    def __init__(self, master):
        self.master = master
        self.modelo = ModeloQR()
        self.vista = VistaQR(self.master, self)
        
    def generar_qr(self, data):
        try:
            self.modelo.generar_qr(data)
        except Exception as e:
            self.vista.mostrar_error(str(e))
            
    def obtener_imagen(self):
        return self.modelo.obtener_imagen()
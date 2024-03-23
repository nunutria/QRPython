import qrcode
from PIL import Image

class ModeloQR:
    def __init__(self):
        self.imagen = None
        
    def generar_qr(self, data):
        try:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            self.imagen = img
        except Exception as e:
            raise Exception("Error al generar el código QR: " + str(e))
            
    def obtener_imagen(self):
        return self.imagen
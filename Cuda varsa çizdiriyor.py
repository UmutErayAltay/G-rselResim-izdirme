from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
import sys
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
import torch
model_id1 = "stabilityai/stable-diffusion-2-1-base"
scheduler1 = EulerDiscreteScheduler.from_pretrained(model_id1, subfolder="scheduler")
pipe1 = StableDiffusionPipeline.from_pretrained(model_id1, scheduler=scheduler1, torch_dtype=torch.float32)
pipe1 = pipe1.to("cuda")
from diffusers import StableDiffusionPipeline
import torch
model_id2 = "prompthero/openjourney"
pipe2 = StableDiffusionPipeline.from_pretrained(model_id2, torch_dtype=torch.float32)
pipe2 = pipe2.to("cuda")
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Artemis'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 1000, 800)

        # Input alanı oluşturma
        self.input_alani = QLineEdit(self)
        self.input_alani.move(100, 50)
        self.input_alani.resize(900, 32)

        # Buton oluşturma
        buton = QPushButton('Çizdir', self)
        buton.move(100, 100)

        # Butona tıklandığında çalışacak fonksiyon
        buton.clicked.connect(self.on_click)
         # Buton oluşturma
        buton = QPushButton('Resim Değiş', self)
        buton.move(200, 100)

        # Butona tıklandığında çalışacak fonksiyon
        buton.clicked.connect(self.change_image)

        # İlk resim
        self.label1 = QLabel(self)
        pixmap1 = QPixmap('resim1.jpg')
        self.label1.setPixmap(pixmap1.scaled(400, 400))
        self.label1.move(50, 200)
        self.label1.setFixedSize(400,400)
        # İkinci resim
        self.label2 = QLabel(self)
        pixmap2 = QPixmap('resim2.jpg')
        self.label2.setPixmap(pixmap2.scaled(400, 400))
        self.label2.move(500, 200)
        self.label2.setFixedSize(400,400)
        

        self.show()
    def on_click(self):
        #resim 2
        prompt = self.input_alani.text()
        image2 = pipe2(prompt).images[0]
        image2.save("yeniresim2.jpg")

        #resim 1
        prompt1 = self.input_alani.text()
        image1 = pipe1(prompt1).images[0]  
        image1.save("yeniresim1.jpg")


    def change_image(self):
        # Yeni pixmap oluşturma
        yeni_pixmap1 = QPixmap('yeniresim1.jpg')
        yeni_pixmap2 = QPixmap('yeniresim2.jpg')
        # İlk QLabel nesnesinin pixmap özelliğini güncelleme
        self.label1.setPixmap(yeni_pixmap1.scaled(400, 400))
        
        # İkinci QLabel nesnesinin pixmap özelliğini güncelleme
        self.label2.setPixmap(yeni_pixmap2.scaled(400, 400))
app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())

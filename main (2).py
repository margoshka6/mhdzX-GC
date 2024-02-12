from PyQt5. QtWidgets import( QApplication, QWidget,
QFileDialog,
QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout)


from PyQt5 import QtGui
from PyQt5.QtCore import Qt
import os
from PIL import Image
from PIL.ImageFilter import SHARPEN

app = QApplication([])
win = QWidget()

win.setStyleSheet('background-color:#e38193; font-size:24px; padding: 5px')
win.setWindowIcon(QtGui.QIcon('free-icon-diamonds-5904357.png'))
win.resize(1200,700)
win.setWindowTitle("Easy Editor")

lb_image=QLabel("картинка")


btn_dir = QPushButton("папка")
btn_dir.setStyleSheet("border:2px solid #708899;border-radius:20px; background-color:#b30219")
btn_dir.setCursor(Qt.PointingHandCursor)

lw_files=QListWidget()
lw_files.setStyleSheet("border:2px solid #708899;border-radius:20px; background-color:#b30219")

btn_left = QPushButton ("Вліво")
btn_left.setStyleSheet( 'border:2px solid #102738; border-radius:20px; background-color:#b30219')
btn_left.setCursor(Qt.PointingHandCursor)

btn_right = QPushButton ("Вправо")
btn_right.setStyleSheet( 'border:2px solid #102738; border-radius:20px; background-color:#b30219')
btn_right.setCursor(Qt.PointingHandCursor)

btn_flip = QPushButton ("Дзеркально")
btn_flip.setStyleSheet('border:2px solid #102738; border-radius:20px; background-color:#b30219')
btn_flip.setCursor(Qt.PointingHandCursor)

btn_sharp = QPushButton ("Різкість")
btn_sharp.setStyleSheet('border:2px solid #102738; border-radius:20px; background-color:#b30219')
btn_sharp.setCursor(Qt.PointingHandCursor)

btn_bw = QPushButton("Ч/б")
btn_bw.setStyleSheet ('border:2px solid #102738; border-radius:20px; background-color:#b30219')
btn_bw.setCursor(Qt.PointingHandCursor)

row = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()
col3 = QVBoxLayout()

col1.addWidget(btn_dir)
col1.addWidget(lw_files)

col2.addWidget(lb_image, 95)

col3.addWidget(btn_left)
col3.addWidget(btn_right)
col3.addWidget(btn_flip)
col3.addWidget(btn_sharp)
col3.addWidget(btn_bw)

row.addLayout(col1,20)
row. addLayout(col2,60)
row. addLayout(col3,20)
win.setLayout(row)

win.show()
workdir =""
def filter(files, extensions) :
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append (filename)
    return result
def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
def showFilenamesList():
    extensions = ['.jpg', '.jpeg', '.png', '.gif']
    chooseWorkdir ()
    filenames = filter(os.listdir(workdir), extensions)
    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)
btn_dir.clicked.connect(showFilenamesList)
class ImageProcessor:
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = 'Modified/'
    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)
    def saveImage(self):
        path = os.path.join(self.dir, self. save_dir)
        if not (os.path.exists(path) and os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self. filename)
        self.image.save(image_path)
    def showImage(self, path):
        lb_image.hide()
        pixmapimage = QPixmap(path)
        pixmapimage = pixmapimage.scaled(600,650,Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()
def showChosenImage():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(workdir, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(image_path)
workimage = ImageProcessor()
lw_files.currentRowChanged.connect(showChosenImage)
app.exec()

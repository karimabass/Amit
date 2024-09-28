



import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
import cv2
import numpy as np
from PyQt5 import Qt, uic, QtWidgets
class ImageViewer(QtWidgets.QDialog):
    def __init__(self) -> None:
        """Initialize"""
        # Loading UI form
        super(ImageViewer , self).__init__()
 
        # self.setWindowTitle('Image Viewer')
        uic.loadUi(r'E:\machine learning course\Lec 39 3 visual George\new.ui', self)
        self.layout = QVBoxLayout()

        self.originview = QLabel(self)
        self.originview.setFixedSize(331, 331)


        self.button_open.clicked.connect(self.openFileDialog)
        

        self.img = None
    
    def openFileDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Image File", "",
                                                  "Images (*.png *.xpm *.jpg *.jpeg *.bmp *.gif);;All Files (*)", options=options)
        if fileName:
            self.img = cv2.imread(fileName)
            self.displayImage(self.img, self.originview)
    
    def displayImage(self, img, label):
        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        label.setPixmap(QPixmap.fromImage(qImg))
   

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec_())

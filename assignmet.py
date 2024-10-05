
# this program is a GUI for filtering image using QT5
# by kareem AbbaS Omar, Eng.


# insert required libraries 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog , QMainWindow,QUndoView,QLineEdit
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMessageBox

import cv2
import numpy as np
from PyQt5 import Qt, uic, QtWidgets


# the main program
class ImageViewer(QtWidgets.QDialog):
    def __init__(self) -> None:
        """Initialize"""
        # Loading UI form
        super(ImageViewer , self).__init__()
        # self.setWindowTitle('Image Viewer')
        uic.loadUi(r'E:\machine learning course\visual studio assignments\assig.ui', self)
        self.originview = self.findChild(QLabel, 'originview')
        self.windowview = self.findChild(QLabel, 'windowview')
        self.harris_display = self.findChild(QLabel,'harris_display')

       
        self.lineEdit = self.findChild(QLineEdit, 'lineEdit')
        self.lineEdit_2 = self.findChild(QLineEdit, 'lineEdit_2')
        self.lineEdit_3 = self.findChild(QLineEdit, 'lineEdit_3')
        # click button setup

        self.button_open.clicked.connect(self.openFileDialog) # to open the image
        self.filterbutton.clicked.connect(self.cannyfiltering)# filtercanny
        self.filterbutton_2.clicked.connect(self.median_blur)# filtermedianblur
        self.filterbutton_3.clicked.connect(self.resizing)# resizing
        self.filterbutton_4.clicked.connect(self.harris)# harris detection

        # Connect the QLineEdit's textChanged signal to a method
        self.lineEdit.textChanged.connect(self.threshold1)
        self.lineEdit_2.textChanged.connect(self.threshold2)
        self.lineEdit_3.textChanged.connect(self.threshold3)


        self.img = None
        self.thred1=1   # default value
        self.thred2=2   # default value
        self.thred3=0.5 # default value


    def threshold1(self):
        # This function is called whenever the text in QLineEdit changes
        self.thred1 = int(self.lineEdit.text())
       
   
    def threshold2(self):
        # This function is called whenever the text in QLineEdit changes
        self.thred2 = int(self.lineEdit_2.text())

    def threshold3(self):
        # This function is called whenever the text in QLineEdit changes
        self.thred3 = float(self.lineEdit_3.text())
    
    # Harris Detection
    def harris(self):
        self.img_harris =self.img
        self.gray = cv2.cvtColor(self.img_harris,cv2.COLOR_BGR2GRAY)
        self.gray = np.float32(self.gray)
        self.corner_img = cv2.cornerHarris(self.gray,2,3,self.thred3)
        self.displayharris(self.corner_img, self.harris_display)


    
    # median_blur

    def median_blur(self):
        self.img_median =self.img
        self.img_median=cv2.medianBlur(self.img_median, 5)
        self.displaymedian(self.img_median, self.windowview)

    # canny filter

    def cannyfiltering(self):
        self.img_canny=self.img
        self.img_canny=cv2.Canny(self.img_canny,self.thred1,self.thred2)
        print(self.thred1)
        print(self.thred2)
        self.displaycanny(self.img_canny, self.windowview)

    # resizing
    def resizing(self):
        self.img_resizing=self.img
        self.img_resizing=self.img_resizing[::1, ::1]
        self.displayreszing(self.img_resizing, self.windowview)

    def openFileDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Image File", "",
                                                  "Images (*.png *.xpm *.jpg *.jpeg *.bmp *.gif);;All Files (*)", options=options)
        if fileName:
            self.img = cv2.imread(fileName)
            self.displayImage(self.img, self.originview)
    
    def displaycanny(self, img, label):
        height, width = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        label.setPixmap(QPixmap.fromImage(qImg))
    
    def displayImage(self, img, label):
        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        label.setPixmap(QPixmap.fromImage(qImg))

    def displaymedian(self, img, label):
        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        label.setPixmap(QPixmap.fromImage(qImg))

    def displayreszing(self, img, label):
        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        label.setPixmap(QPixmap.fromImage(qImg))

# Harris display
    def displayharris(self, img, label):
        height, width= img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        label.setPixmap(QPixmap.fromImage(qImg))
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore,QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFileDialog,QLabel,QAction,QMainWindow,QApplication
from PyQt5.uic import loadUiType
import Encrypter as E 
import Decrypter as D
from PIL import Image as Img
from PIL import ImageTk as ImgTk
#from tkinter import *
import base64
from Crypto.Cipher import AES
import os
import sys
import string
#import tkinter
#import tkinter.filedialog as tkFileDialog
Qt = QtCore.Qt



# master = Tk()
# master.wm_title("Image Encryption using AES")
# l2=Label(master, text="Key")

# l2.pack()
# e2 = Entry(master)
# e2.pack()
# e2.focus_set()

# label = Label (master, text="")
# label.pack()
# def callback():
#     file = tkFileDialog.askopenfile(parent=master,mode='rb',title='Choose a file')
#     print(type(file))
#     print(file)
#     if file != None:
#         data = file.read()
#         print(data)
#         print(type(data))
#         stri = base64.b64encode(data)     
#     myKey=e2.get()
#     x = Encrypter(stri, myKey)
#     cipher = x.encrypt_image()
#     x = Decrypter(cipher)
#     x.decrypt_image(myKey)
#     label.configure(text= "Cipher: " + cipher.decode('utf-8'),font=("Helvetica", 8))
# b = Button(master, text="Encrypt", width=10, command=callback)
# b.pack()
# master.mainloop()
ui, _ = loadUiType('ui.ui')
def start():
    global m
    m = Main_Window()
    m.show()

filename = ""
filename2 = ""
format = "PNG"    
    
class encrypt_page():
    def __init__(self):
        self.file={}
        self.stri=""
        self.Handel_Buttons()
        self.pushButton_3.clicked.connect(self.chooseFile)
        self.pushButton_4.clicked.connect(self.onClickEncrypt)
        self.pushButton_5.clicked.connect(self.onclickgotoD)
    def Handel_Buttons(self):
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        
    def chooseFile(self):
        self.file = QFileDialog.getOpenFileName(self, 'Open File')
        global filename
        filename = os.path.basename(os.path.normpath(self.file[0])) 
        #print(filename)
        pixmap = QtGui.QPixmap(self.file[0])
        self.lbl.setPixmap(pixmap.scaledToHeight(271))
        """
        if self.file != None:
            ba = QtCore.QByteArray()
            buff = QtCore.QBuffer(ba)
            buff.open(QtCore.QIODevice.WriteOnly) 
            ok = pixmap.save(buff, "PNG")
            assert ok
            pixmap_bytes = ba.data()
            #print(type(pixmap_bytes))
            #data = self.file[0]
            self.stri = base64.b64encode(pixmap_bytes)
        """
    def onclickgotoD(self):
        #print("hi")
        self.file = 'Encrypted_ecb.png'
        pixmap = QtGui.QPixmap(self.file)
        self.lbl_8.setPixmap(pixmap.scaledToHeight(221))
        
        self.file = 'Encrypted_cbc.png'
        pixmap = QtGui.QPixmap(self.file)
        self.lbl_11.setPixmap(pixmap.scaledToHeight(221))
        
        self.stackedWidget.setCurrentIndex(2)
        
    def onClickEncrypt(self):
        #global E.Key
        E.key=self.lineEdit.text()
        E.keylen=len(E.key)
        # print(type(myKey))
        
        global filename
        E.encrypt_image_cbc(filename)
        E.encrypt_image_ecb(filename)
         
        self.file = 'Encrypted_ecb.png'
        pixmap = QtGui.QPixmap(self.file)
        self.lbl_5.setPixmap(pixmap.scaledToHeight(271))
        
        self.file = 'Encrypted_cbc.png'
        pixmap = QtGui.QPixmap(self.file)
        self.lbl_6.setPixmap(pixmap.scaledToHeight(271))

        """x = Encrypter(self.stri, myKey)
        cipher = x.encrypt_image()
        # print(type(cipher))
        # name = QFileDialog.getSaveFileName(self, 'Save File')
        # file = open(name,'w')
        # text = cipher
        # file.write(text)
        # file.close()
        #fh.write(base64_decoded.decode('base64'))
        fh = open("cipher.txt", "wb")
        fh.write(cipher)
        fh.close()"""
        # cipherd = base64.b64decode(cipher.decode('utf-8'))
        # ba = QtCore.QByteArray(cipherd)
        # pixmap = QtGui.QPixmap()
        # ok = pixmap.loadFromData(ba, "PNG")
        #assert ok
        #self.lbl.setPixmap(pixmap.scaledToHeight(201))
        #x = Decrypter(cipher)
        #x.decrypt_image(myKey)
        
class decrypt_page():
    def __init__(self):
        #self.cipher={}
        self.Handel_Buttons()
        #self.pushButton_5.clicked.connect(self.chooseFile1)
        self.pushButton_6.clicked.connect(self.onClickDecrypt)
    def Handel_Buttons(self):
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
    """
    def chooseFile1(self):
        file = QFileDialog.getOpenFileName(self, 'Open File')
        text=open(file[0]).read()
        #print(text.encode('utf-8'))
        self.cipher= base64.b64decode(text)
        self.file = QFileDialog.getOpenFileName(self, 'Open File')
        global filename2
        filename2 = os.path.basename(os.path.normpath(self.file[0])) 
        pixmap = QtGui.QPixmap(self.file[0])
        self.lbl_2.setPixmap(pixmap.scaledToHeight(201))
       """ 
    def onClickDecrypt(self):
        D.key=self.lineEdit_2.text()
        global filename2
        D.decrypt_image_ecb("Encrypted_ecb.png")
        D.decrypt_image_cbc("Encrypted_cbc.png")
        #x = Decrypter(self.cipher)
        #image=x.decrypt_image(myKey)
        
        self.file = 'decryptfile4.png'
        pixmap = QtGui.QPixmap(self.file)       
        self.lbl_9.setPixmap(pixmap.scaledToHeight(221))
        
        self.file = 'decryptfile3.png'
        pixmap = QtGui.QPixmap(self.file)       
        self.lbl_10.setPixmap(pixmap.scaledToHeight(221))
        # if image!=None:
        #     ba = QtCore.QByteArray()
        #     buff = QtCore.QBuffer(ba)
        #     buff.open(QtCore.QIODevice.WriteOnly) 
        #     ok = pixmap.save(buff, "PNG")
        #     assert ok
        #     pixmap_bytes = ba.data()
        #     #print(type(pixmap_bytes))
        #     #data = self.file[0]
        #     self.stri = base64.b64encode(pixmap_bytes)            
        
class Main_Window(QMainWindow, QWidget, ui,encrypt_page,decrypt_page):
    def __init__(self):
        QMainWindow.__init__(self)
        QWidget.__init__(self)
        self.setupUi(self)
        encrypt_page.__init__(self)
        decrypt_page.__init__(self)

        self.Handel_Buttons() 
        self.stackedWidget.setCurrentIndex(0)
    def Handel_Buttons(self):
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        
        self.pushButton_8.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButton_7.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    #connect()
    window = start()
    app.exec_()
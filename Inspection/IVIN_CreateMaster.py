
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QInputDialog
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer


import os
import shutil
import cv2

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1119, 659)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.cameraPreview = QtWidgets.QLabel(Form)
        self.cameraPreview.setAlignment(QtCore.Qt.AlignCenter)
        self.cameraPreview.setObjectName("cameraPreview")
        self.verticalLayout.addWidget(self.cameraPreview)
        self.coordinates_preview = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coordinates_preview.sizePolicy().hasHeightForWidth())
        self.coordinates_preview.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.coordinates_preview.setFont(font)
        self.coordinates_preview.setAlignment(QtCore.Qt.AlignCenter)
        self.coordinates_preview.setObjectName("coordinates_preview")
        self.verticalLayout.addWidget(self.coordinates_preview)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout.addWidget(self.line_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_2.addWidget(self.line_6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.imageNo = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageNo.sizePolicy().hasHeightForWidth())
        self.imageNo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.imageNo.setFont(font)
        self.imageNo.setText("")
        self.imageNo.setAlignment(QtCore.Qt.AlignCenter)
        self.imageNo.setObjectName("imageNo")
        self.verticalLayout_3.addWidget(self.imageNo)
        self.capturedImage = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.capturedImage.setFont(font)
        self.capturedImage.setAlignment(QtCore.Qt.AlignCenter)
        self.capturedImage.setObjectName("capturedImage")
        self.verticalLayout_3.addWidget(self.capturedImage)
        self.coordinates_captured = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coordinates_captured.sizePolicy().hasHeightForWidth())
        self.coordinates_captured.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.coordinates_captured.setFont(font)
        self.coordinates_captured.setAlignment(QtCore.Qt.AlignCenter)
        self.coordinates_captured.setObjectName("coordinates_captured")
        self.verticalLayout_3.addWidget(self.coordinates_captured)
        self.line_9 = QtWidgets.QFrame(Form)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_3.addWidget(self.line_9)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_2.addWidget(self.line_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.modelNo = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modelNo.sizePolicy().hasHeightForWidth())
        self.modelNo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.modelNo.setFont(font)
        self.modelNo.setText("")
        self.modelNo.setObjectName("modelNo")
        self.verticalLayout_4.addWidget(self.modelNo)
        self.setModel = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.setModel.setFont(font)
        self.setModel.setObjectName("setModel")
        self.verticalLayout_4.addWidget(self.setModel)
        self.captureBt = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.captureBt.sizePolicy().hasHeightForWidth())
        self.captureBt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.captureBt.setFont(font)
        self.captureBt.setObjectName("captureBt")
        self.verticalLayout_4.addWidget(self.captureBt)
        self.retakeBt = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.retakeBt.sizePolicy().hasHeightForWidth())
        self.retakeBt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.retakeBt.setFont(font)
        self.retakeBt.setObjectName("retakeBt")
        self.verticalLayout_4.addWidget(self.retakeBt)
        self.saveBt = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveBt.sizePolicy().hasHeightForWidth())
        self.saveBt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.saveBt.setFont(font)
        self.saveBt.setObjectName("saveBt")
        self.verticalLayout_4.addWidget(self.saveBt)
        self.closeBt = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeBt.sizePolicy().hasHeightForWidth())
        self.closeBt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.closeBt.setFont(font)
        self.closeBt.setObjectName("closeBt")
        self.verticalLayout_4.addWidget(self.closeBt)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line_7 = QtWidgets.QFrame(Form)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout.addWidget(self.line_7)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ZF Create Master"))
        self.cameraPreview.setText(_translate("Form", "Camera Preview"))
        self.coordinates_preview.setText(_translate("Form", "X :          Y :          Z :          A :          B :          C :"))
        self.capturedImage.setText(_translate("Form", "captured Image"))
        self.coordinates_captured.setText(_translate("Form", "X :          Y :          Z :          A :          B :          C :."))
        self.setModel.setText(_translate("Form", "Set Model"))
        self.captureBt.setText(_translate("Form", "Capture"))
        self.retakeBt.setText(_translate("Form", "Re Capture"))
        self.saveBt.setText(_translate("Form", "Save and next"))
        self.closeBt.setText(_translate("Form", "Close"))


class MainWindow(QWidget):
    i = 1
    base=os.path.basename(__file__)
    path = __file__[:-len(base)]
    isCaptured = False
    app = QApplication([])
    screen_resolution = app.desktop().screenGeometry()
    screenWidth, screenHeight = screen_resolution.width(), screen_resolution.height()

    model = None

    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.viewCam)
        self.controlTimer()
        
        self.ui.imageNo.setText("Image no : " + str(self.i))
        
        self.ui.modelNo.setVisible(False)
        self.ui.captureBt.setVisible(False)
        self.ui.retakeBt.setVisible(False)
        self.ui.saveBt.setVisible(False)
        self.ui.closeBt.setVisible(False)
        
        self.ui.setModel.clicked.connect(self.showDialogModel)
        self.ui.saveBt.clicked.connect(self.save)
        self.ui.retakeBt.clicked.connect(self.retake)
        self.ui.captureBt.clicked.connect(self.capture)
        self.ui.closeBt.clicked.connect(self.close)


    def viewCam(self):
        _, self.image = self.cap.read()
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        self.imageV = cv2.resize(self.image,(int(self.screenWidth/2)-50,int(self.screenHeight/2)))
        height, width, channel = self.imageV.shape
        step = channel * width

        qImg = QImage(self.imageV.data, int(self.screenWidth/2)-50, int(self.screenHeight/2), step, QImage.Format_RGB888)
        self.ui.cameraPreview.setPixmap(QPixmap.fromImage(qImg))
    
    
    def close(self):
        exit(0)
    
    
    def showDialogModel(self):
        self.model, result = QInputDialog.getText(
            self, "Model", "Enter model : ")
        if(result == True):
            if(len(self.model) > 0):
                self.ui.setModel.setVisible(False)
                self.ui.modelNo.setText("Model : " + self.model)
                self.ui.modelNo.setVisible(True)
                if(self.model != None):
                    self.ui.captureBt.setVisible(True)
                    self.ui.retakeBt.setVisible(True)
                    self.ui.saveBt.setVisible(True)
                    self.ui.closeBt.setVisible(True)
            else:
                self.showDialogModel()

    def controlTimer(self):
        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)
            # self.ui.captureBt.setText("Stop")
        else:
            self.timer.stop()
            self.cap.release()
            self.ui.captureBt.setText("Start")

    def save(self):
        if self.isCaptured:
            if(self.i == 1 and os.path.exists(
                    self.path+"Master_DB\\"+self.model+"\\")):
                    shutil.rmtree(self.path+"Master_DB\\"+self.model+"\\")
            if(os.path.exists(
                    self.path+"Master_DB\\"+self.model+"\\")):
                pass
                # cv2.imwrite(self.path+"Master_DB\\" + time + "_" + str(self.i)+".jpg", self.image)
            elif(os.path.exists(
                    self.path+"Master_DB\\")):
                    os.mkdir(self.path+"Master_DB\\"+self.model+"\\")
            else:
                os.mkdir(self.path+"Master_DB\\")
                os.mkdir(self.path+"Master_DB\\"+self.model+"\\")
            cv2.imwrite(self.path+"Master_DB\\"+self.model+"\\" + str(self.i)+".jpg", self.capturedImage)
            self.i += 1
            self.ui.imageNo.setText("Image no : " + str(self.i))
            self.ui.capturedImage.setText("Captured Image will appear here.")
            self.isCaptured = False

    def capture(self):
        height, width, channel = self.imageV.shape
        step = channel * width
        qImg = QImage(self.imageV.data, int(self.screenWidth/3), int(self.screenHeight/3), step, QImage.Format_RGB888)
        self.ui.capturedImage.setPixmap(QPixmap.fromImage(qImg))
        self.isCaptured = True
        self.capturedImage = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
        # self.capturedImage = self.image

    def retake(self):
        self.ui.capturedImage.setText("Captured Image will appear here.")
        self.isCaptured = False


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())

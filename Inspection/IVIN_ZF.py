
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QInputDialog
from PyQt5.QtWidgets import QWidget, QMessageBox, QMenu, QAction
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

from datetime import datetime
import os

import cv2
import pandas as pd
import shutil
import sqlite3

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1132, 710)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)

        self.menubar = QtWidgets.QMenuBar(Form)
        self.FileMenu = self.menubar.addMenu("File")
        self.downloadExcel = QAction("Download Excel")
        self.FileMenu.addAction(self.downloadExcel)

        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label_2 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.capturedImage = QtWidgets.QLabel(Form)
        self.capturedImage.setText("")
        self.capturedImage.setAlignment(QtCore.Qt.AlignCenter)
        self.capturedImage.setObjectName("capturedImage")
        self.verticalLayout.addWidget(self.capturedImage)
        self.line_8 = QtWidgets.QFrame(Form)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout.addWidget(self.line_8)
        self.cameraPreview = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.cameraPreview.setFont(font)
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
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_3.addWidget(self.line_6)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.imageNo = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.imageNo.setFont(font)
        self.imageNo.setText("")
        self.imageNo.setAlignment(QtCore.Qt.AlignCenter)
        self.imageNo.setObjectName("imageNo")
        self.verticalLayout_3.addWidget(self.imageNo)
        self.line_9 = QtWidgets.QFrame(Form)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_3.addWidget(self.line_9)
        self.actualImage = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actualImage.sizePolicy().hasHeightForWidth())
        self.actualImage.setSizePolicy(sizePolicy)
        self.actualImage.setText("")
        self.actualImage.setAlignment(QtCore.Qt.AlignCenter)
        self.actualImage.setObjectName("actualImage")
        self.verticalLayout_3.addWidget(self.actualImage)
        self.coordinates_master = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.coordinates_master.setFont(font)
        self.coordinates_master.setAlignment(QtCore.Qt.AlignCenter)
        self.coordinates_master.setObjectName("coordinates_master")
        self.verticalLayout_3.addWidget(self.coordinates_master)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_2.addWidget(self.line_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.orderNo = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.orderNo.setFont(font)
        self.orderNo.setText("")
        self.orderNo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.orderNo.setObjectName("orderNo")
        self.verticalLayout_4.addWidget(self.orderNo)
        self.setOrder = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.setOrder.setFont(font)
        self.setOrder.setObjectName("setOrder")
        self.verticalLayout_4.addWidget(self.setOrder)
        self.serialNo = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serialNo.sizePolicy().hasHeightForWidth())
        self.serialNo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.serialNo.setFont(font)
        self.serialNo.setText("")
        self.serialNo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.serialNo.setObjectName("serialNo")
        self.verticalLayout_4.addWidget(self.serialNo)
        self.setSerial = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.setSerial.setFont(font)
        self.setSerial.setObjectName("setSerial")
        self.verticalLayout_4.addWidget(self.setSerial)
        self.model = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.model.setFont(font)
        self.model.setText("")
        self.model.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.model.setObjectName("model")
        self.verticalLayout_4.addWidget(self.model)
        self.setModel = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.setModel.setFont(font)
        self.setModel.setObjectName("setModel")
        self.verticalLayout_4.addWidget(self.setModel)
        self.inspectorId = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.inspectorId.setFont(font)
        self.inspectorId.setText("")
        self.inspectorId.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.inspectorId.setObjectName("inspectorId")
        self.verticalLayout_4.addWidget(self.inspectorId)
        self.setInspector = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.setInspector.setFont(font)
        self.setInspector.setObjectName("setInspector")
        self.verticalLayout_4.addWidget(self.setInspector)
        self.captureBt = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
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
        self.errorBt = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.errorBt.sizePolicy().hasHeightForWidth())
        self.errorBt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.errorBt.setFont(font)
        self.errorBt.setObjectName("errorBt")
        self.verticalLayout_4.addWidget(self.errorBt)
        self.saveBt = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
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
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ZF Inspection"))
        self.label_2.setText(_translate("Form", "Captured Image"))
        self.cameraPreview.setText(_translate("Form", "Camera Preview"))
        self.coordinates_preview.setText(_translate("Form", "X :          Y :          Z :          A :          B :          C :"))
        self.label.setText(_translate("Form", "Actual Image"))
        self.coordinates_master.setText(_translate("Form", "X :          Y :          Z :          A :          B :          C :"))
        self.setOrder.setText(_translate("Form", "Set Order number"))
        self.setSerial.setText(_translate("Form", "Set Serial number"))
        self.setModel.setText(_translate("Form", "Set Model"))
        self.setInspector.setText(_translate("Form", "Set Inspector Id"))
        self.captureBt.setText(_translate("Form", "Capture"))
        self.retakeBt.setText(_translate("Form", "Re Capture"))
        self.errorBt.setText(_translate("Form", "Wrong Image"))
        self.saveBt.setText(_translate("Form", "Save and next"))


class MainWindow(QWidget):

    i = 1
    isInit = True
    date = datetime.today().strftime("%b-%d-%Y")
    base = os.path.basename(__file__)
    path = __file__[:-len(base)]
    isCaptured = False
    serialNo = None
    inspectorId = None
    model = None
    orderNo = None
    correctCount = 0
    wrongCount = 0

    app = QApplication([])
    screen_resolution = app.desktop().screenGeometry()
    screenWidth, screenHeight = screen_resolution.width(), screen_resolution.height()

    models = []

    attempt = 1

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.viewCam)
        self.controlTimer()
        self.ui.captureBt.setVisible(False)
        self.ui.retakeBt.setVisible(False)
        self.ui.saveBt.setVisible(False)
        self.ui.errorBt.setVisible(False)
        self.ui.serialNo.setVisible(False)
        self.ui.imageNo.setVisible(False)
        self.ui.inspectorId.setVisible(False)
        self.ui.orderNo.setVisible(False)
        self.ui.model.setVisible(False)

        

        self.ui.saveBt.clicked.connect(self.save)
        self.ui.errorBt.clicked.connect(self.wrong)
        self.ui.retakeBt.clicked.connect(self.retake)
        self.ui.captureBt.clicked.connect(self.capture)
        self.ui.captureBt.clicked.connect(self.capture)

        self.ui.setSerial.clicked.connect(self.showDialogSerial)
        self.ui.setInspector.clicked.connect(self.showDialogInspector)
        self.ui.setModel.clicked.connect(self.showDialogModel)
        self.ui.setOrder.clicked.connect(self.showDialogOrder)
        self.ui.downloadExcel.triggered.connect(self.downloadExcel)

        self.ui.setSerial.setVisible(False)
        self.ui.setModel.setVisible(False)
        self.ui.setInspector.setVisible(False)

    def showDialogOrder(self):
        if(os.path.exists(
                self.path+"Master_DB/")):
            models = [x[0] for x in os.walk(self.path+"Master_DB/")]
            # print(self.path)
            for i in range(len(models)):
                if(i!=0):
                    self.models.append(models[i][len(self.path)+10:])
        else:
            QMessageBox.about(
                self, "Error", "Create master first !!!")
            exit()
        self.orderNo, result = QInputDialog.getText(
            self, "Order No", "Enter Order No : ")
        if(result == True):
            if(len(self.orderNo) > 0):
                self.ui.setOrder.setVisible(False)
                self.ui.orderNo.setText("Order No : " + self.orderNo)
                self.ui.orderNo.setVisible(True)
                self.showDialogSerial()
                # if(self.serialNo != None and self.inspectorId != None and self.model != None and self.orderNo != None):
                #     self.ui.captureBt.setVisible(True)
                #     self.ui.retakeBt.setVisible(True)
                #     self.ui.saveBt.setVisible(True)
                #     self.ui.errorBt.setVisible(True)
                #     self.ui.imageNo.setVisible(True)
                #     self.ui.imageNo.setText("Image no : " + str(self.i))
                #     try:
                #         self.actualImage = cv2.imread(
                #             self.path+"Master_DB\\" + str(self.i)+".jpg")
                #         self.actualImage = cv2.cvtColor(
                #             self.actualImage, cv2.COLOR_BGR2RGB)
                #         height, width, channel = self.actualImage.shape
                #         step = channel * width
                #         qImg = QImage(self.actualImage.data, 500,
                #                       300, step, QImage.Format_RGB888)
                #         self.ui.actualImage.setPixmap(QPixmap.fromImage(qImg))
                        
                #     except:
                #         QMessageBox.about(
                #             self, "Error", "Create master first !!!")
                #         exit()
            else:
                self.showDialogOrder()

    def showDialogSerial(self):
        self.serialNo, result = QInputDialog.getText(
            self, "Serial No", "Enter Serial number : ")
        if(result == True):
            if(len(self.serialNo) > 0):
                self.ui.setSerial.setVisible(False)
                self.ui.serialNo.setText("Serail no : " + self.serialNo)
                self.ui.serialNo.setVisible(True)
                self.showDialogModel()
                # if(self.serialNo != None and self.inspectorId != None and self.model != None and self.orderNo != None):
                #     self.ui.captureBt.setVisible(True)
                #     self.ui.retakeBt.setVisible(True)
                #     self.ui.saveBt.setVisible(True)
                #     self.ui.errorBt.setVisible(True)
                #     self.ui.imageNo.setVisible(True)
                #     self.ui.imageNo.setText("Image no : " + str(self.i))
                #     try:
                #         self.actualImage = cv2.imread(
                #             self.path+"Master_DB\\" + str(self.i)+".jpg")
                #         self.actualImage = cv2.cvtColor(
                #             self.actualImage, cv2.COLOR_BGR2RGB)
                #         height, width, channel = self.actualImage.shape
                #         step = channel * width
                #         qImg = QImage(self.actualImage.data, 500,
                #                       300, step, QImage.Format_RGB888)
                #         self.ui.actualImage.setPixmap(QPixmap.fromImage(qImg))
                        
                #     except:
                #         QMessageBox.about(
                #             self, "Error", "Create master first !!!")
                #         exit()
            else:
                self.showDialogSerial()
        else:
            self.showDialogSerial()

    def showDialogModel(self):
        
        self.model, result = QInputDialog.getItem(
            self, "Choose model", "Model",self.models,0,False)
        if(result == True):
            if(len(self.model) > 0):
                self.ui.setModel.setVisible(False)
                self.ui.model.setText("Model : " + self.model)
                self.ui.model.setVisible(True)
                self.showDialogInspector()
                # if(self.serialNo != None and self.inspectorId != None and self.model != None and self.orderNo != None):
                #     self.ui.captureBt.setVisible(True)
                #     self.ui.retakeBt.setVisible(True)
                #     self.ui.saveBt.setVisible(True)
                #     self.ui.errorBt.setVisible(True)
                #     self.ui.imageNo.setVisible(True)
                #     self.ui.imageNo.setText("Image no : " + str(self.i))
                #     try:
                #         self.actualImage = cv2.imread(
                #             self.path+"Master_DB\\" + str(self.i)+".jpg")
                #         self.actualImage = cv2.cvtColor(
                #             self.actualImage, cv2.COLOR_BGR2RGB)
                #         height, width, channel = self.actualImage.shape
                #         step = channel * width
                #         qImg = QImage(self.actualImage.data, 500,
                #                       300, step, QImage.Format_RGB888)
                #         self.ui.actualImage.setPixmap(QPixmap.fromImage(qImg))
                        
                #     except:
                #         QMessageBox.about(
                #             self, "Error", "Create master first !!!")
                #         exit()
            else:
                self.showDialogModel()
        else:
            self.showDialogModel()

    def showDialogInspector(self):
        self.inspectorId, result = QInputDialog.getText(
            self, "Inspector Id", "Enter Inspector Id : ")
        if(result == True):
            if(len(self.inspectorId) > 0):
                self.ui.setInspector.setVisible(False)
                self.ui.inspectorId.setText(
                    "Inspector Id : " + self.inspectorId)
                self.ui.inspectorId.setVisible(True)
                if(self.serialNo != None and self.inspectorId != None and self.model != None and self.orderNo != None):
                    self.ui.captureBt.setVisible(True)
                    self.ui.retakeBt.setVisible(True)
                    self.ui.saveBt.setVisible(True)
                    self.ui.errorBt.setVisible(True)
                    self.ui.imageNo.setVisible(True)
                    self.ui.imageNo.setText("Image no : " + str(self.i))
                    try:
                        self.actualImage = cv2.imread(
                            self.path+"Master_DB\\"+self.model+"\\" + str(self.i)+".jpg")
                        self.actualImage = cv2.cvtColor(
                            self.actualImage, cv2.COLOR_BGR2RGB)
                        height, width, channel = self.actualImage.shape
                        step = channel * width
                        qImg = QImage(self.actualImage.data, 500,
                                      300, step, QImage.Format_RGB888)
                        self.ui.actualImage.setPixmap(QPixmap.fromImage(qImg))
                    except:
                        QMessageBox.about(
                            self, "Error", "Create master first !!!")
                        exit()
            else:
                self.showDialogInspector()
        else:
            self.showDialogInspector()

    def downloadExcel(self):
        if(self.attempt < 4):
            password, result = QInputDialog.getText(
                self, "Password", "Enter Password : (attempt : {})".format(self.attempt))
            if(result == True ):
                self.attempt +=1
                if(password == "surya"):
                    connection = sqlite3.connect(self.path+"ZF_Inspection.db")
                    try:
                        cursor = list(connection.execute('SELECT * FROM ZFInspection'))
                        cursor.reverse()
                    except:
                        QMessageBox.about(self, "Error", "No Inspection has been done till now.")
                        exit()
                    
                    data = {'Date': [],
                        'Model': [],
                        'Order No': [],
                        'Serial No': [],
                        'Inspector Id': [],
                        'Correct': [],
                        'Wrong': []}
                    for row in cursor:
                        data['Date'].append(str(row[0])[:10])
                        data['Model'].append(row[1])
                        data['Order No'].append(row[2])
                        data['Serial No'].append(row[3])
                        data['Inspector Id'].append(row[4])
                        data['Correct'].append(row[5])
                        data['Wrong'].append(row[6])
                    
                    # excel = pd.ExcelWriter('ZF_Inspection_{}.xlsx'.format(self.date))
                    df = pd.DataFrame(data)
                    try:
                        df.to_excel(self.path+'ZF_Inspection_{}.xlsx'.format(self.date),index=False)
                    except:
                        QMessageBox.about(self, "Error", "Please close the excel file and try again.")
                        exit()

                    QMessageBox.about(self, "Download", "The Report has been downloaded successfully.")
                    exit()
                else:
                    self.downloadExcel()
        else:
            QMessageBox.about(self, "Error", "Password Attempt Exceeded!!!")
            exit() 

    def viewCam(self):
        _, self.image = self.cap.read()
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        self.image = cv2.resize(self.image,(int(self.screenWidth/2)-50,int(self.screenHeight/2)))
        height, width, channel = self.image.shape
        step = channel * width
        qImg = QImage(self.image.data, 500, 300, step, QImage.Format_RGB888)
        self.ui.cameraPreview.setPixmap(QPixmap.fromImage(qImg))
        if(self.isInit  == True):
            self.showDialogOrder()
            self.isInit = False

    def controlTimer(self):
        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)
            # self.ui.captureBt.setText("Stop")
        else:
            self.timer.stop()
            self.cap.release()
            self.ui.captureBt.setText("Start")

    def wrong(self):
        if self.isCaptured:
            if(self.i == 1 and os.path.exists(
                    self.path+"DB\\{date}\\{serialNo}\\".format(date=self.model, serialNo=self.serialNo))):
                shutil.rmtree(
                    self.path+"DB\\{date}\\{serialNo}\\".format(date=self.model, serialNo=self.serialNo))
            if(os.path.exists(
                    self.path+"DB\\{date}\\{serialNo}\\Wrong\\".format(date=self.model, serialNo=self.serialNo))):
                pass
            elif(os.path.exists(
                    self.path+"DB\\{date}\\{serialNo}\\".format(date=self.model, serialNo=self.serialNo))):
                os.mkdir(
                    self.path+"DB\\{date}\\{serialNo}\\Wrong\\".format(date=self.model, serialNo=self.serialNo))
            elif(os.path.exists(
                    self.path+"DB\\{date}\\".format(date=self.model))):
                os.mkdir(
                    self.path+"DB\\{date}\\{serialNo}\\".format(date=self.model, serialNo=self.serialNo))
                os.mkdir(
                    self.path+"DB\\{date}\\{serialNo}\\Wrong\\".format(date=self.model, serialNo=self.serialNo))
                
            elif(os.path.exists(
                    self.path+"DB\\")):
                os.mkdir(self.path+"DB\\{date}\\".format(date=self.model))
                os.mkdir(
                    self.path+"DB\\{date}\\{serialNo}\\".format(date=self.model, serialNo=self.serialNo))
                os.mkdir(
                    self.path+"DB\\{date}\\{serialNo}\\Wrong\\".format(date=self.model, serialNo=self.serialNo))
            else:
                os.mkdir(self.path+"DB\\")
                os.mkdir(self.path+"DB\\{date}\\".format(date=self.model))
                os.mkdir(
                    self.path+"DB\\{date}\\{serialNo}\\".format(date=self.model, serialNo=self.serialNo))
                os.mkdir(
                    self.path+"DB\\{date}\\{serialNo}\\Wrong\\".format(date=self.model, serialNo=self.serialNo))
            cv2.imwrite(self.path+"DB\\{date}\\{serialNo}\\Wrong\\".format(
                date=self.model, serialNo=self.serialNo) + str(self.i)+".jpg", self.capturedImage)
            self.i += 1
            self.ui.imageNo.setText("Image no : " + str(self.i))
            self.ui.capturedImage.setText(" ")
            self.isCaptured = False
            self.wrongCount += 1
            try:
                self.actualImage = cv2.imread(
                    self.path+"Master_DB\\"+self.model+"\\" + str(self.i)+".jpg")
                self.actualImage = cv2.cvtColor(
                    self.actualImage, cv2.COLOR_BGR2RGB)
                height, width, channel = self.actualImage.shape
                step = channel * width
                qImg = QImage(self.actualImage.data, 500,
                              300, step, QImage.Format_RGB888)
                self.ui.actualImage.setPixmap(QPixmap.fromImage(qImg))
            except:
                # data = {'Date': [self.date],
                #         'Model': [self.model],
                #         'Order No': [self.orderNo],
                #         'Serial No': [self.serialNo],
                #         'Inspector Id': [self.inspectorId],
                #         'Correct': [self.correctCount],
                #         'Wrong': [self.wrongCount]}
                # readData = {}
                connection = sqlite3.connect(self.path+"ZF_Inspection.db")
                try:
                    connection.execute('INSERT INTO ZFInspection VALUES(?,?,?,?,?,?,?)',(datetime.now(),self.model,self.orderNo,self.serialNo,self.inspectorId,self.correctCount,self.wrongCount))
                except:
                    connection.execute('CREATE TABLE ZFInspection (Date timestamp,Model text,Order_No text,Serial_No text,Inspector_Id text,Correct int,Wrong int)')
                    connection.execute('INSERT INTO ZFInspection VALUES(?,?,?,?,?,?,?)',(datetime.now(),self.model,self.orderNo,self.serialNo,self.inspectorId,self.correctCount,self.wrongCount))
                connection.commit()
                connection.close()
                # try:
                #     excel = pd.read_excel('ZF.xlsx')
                #     dic = excel.to_dict()
                #     for key in dic.keys():
                #         temp = []
                #         for i in range(len(dic['Model'].keys())):
                #             temp.append(dic[key][i])
                #         readData[key] = temp
                #         data[key] += readData[key]
                #     # print(readData)

                # except:
                #     pass
                # df = pd.DataFrame(data)

                # writer = pd.ExcelWriter('ZF.xlsx', engine="openpyxl")
                # df.to_excel(writer, index=False, sheet_name='ZF')
                # writer.close()
                QMessageBox.about(self, "Finish", "Inspection done.")
                exit()

    def save(self):
        if self.isCaptured:
            # cv2.imwrite(self.path+"DB\\{date}\\{serialNo}\\".format(date=self.date, serialNo=self.serialNo) + time + "_" + str(self.i)+".jpg", self.image)
            if(self.i == 1 and os.path.exists(
                    self.path+"DB\\{date}\\{serialNo}\\".format(date=self.model, serialNo=self.serialNo))):
                shutil.rmtree(
                    self.path+"DB\\{date}\\{serialNo}\\".format(date=self.model, serialNo=self.serialNo))
            if(os.path.exists(
                    self.path+"DB\\{date}\\{serialNo}\\".format(date=self.model, serialNo=self.serialNo))):
                pass
            elif(os.path.exists(
                    self.path+"DB\\{date}\\".format(date=self.model))):
                os.mkdir(
                    self.path+"DB\\{date}\\{serialNo}\\".format(date=self.model, serialNo=self.serialNo))
            elif(os.path.exists(
                    self.path+"DB\\")):
                os.mkdir(self.path+"DB\\{date}\\".format(date=self.model))
                os.mkdir(
                    self.path+"DB\\{date}\\{serialNo}\\".format(date=self.model, serialNo=self.serialNo))
            else:
                os.mkdir(self.path+"DB\\")
                os.mkdir(self.path+"DB\\{date}\\".format(date=self.model))
                os.mkdir(
                    self.path+"DB\\{date}\\{serialNo}\\".format(date=self.model, serialNo=self.serialNo))
            cv2.imwrite(self.path+"DB\\{date}\\{serialNo}\\".format(
                date=self.model, serialNo=self.serialNo) + str(self.i)+".jpg", self.capturedImage)
            self.i += 1
            self.ui.imageNo.setText("Image no : " + str(self.i))
            self.ui.capturedImage.setText(" ")
            self.isCaptured = False
            self.correctCount += 1
            try:
                self.actualImage = cv2.imread(
                    self.path+"Master_DB\\"+self.model+"\\" + str(self.i)+".jpg")
                self.actualImage = cv2.cvtColor(
                    self.actualImage, cv2.COLOR_BGR2RGB)
                height, width, channel = self.actualImage.shape
                step = channel * width
                qImg = QImage(self.actualImage.data, 500,
                              300, step, QImage.Format_RGB888)
                self.ui.actualImage.setPixmap(QPixmap.fromImage(qImg))
            except:
                # data = {'Date': [self.date],
                #         'Model': [self.model],
                #         'Order No': [self.orderNo],
                #         'Serial No': [self.serialNo],
                #         'Inspector Id': [self.inspectorId],
                #         'Correct': [self.correctCount],
                #         'Wrong': [self.wrongCount]}
                # readData = {}
                connection = sqlite3.connect(self.path+"ZF_Inspection.db")
                try:
                    connection.execute('INSERT INTO ZFInspection VALUES(?,?,?,?,?,?,?)',(datetime.now(),self.model,self.orderNo,self.serialNo,self.inspectorId,self.correctCount,self.wrongCount))
                except:
                    connection.execute('CREATE TABLE ZFInspection (Date timestamp,Model text,Order_No text,Serial_No text,Inspector_Id text,Correct int,Wrong int)')
                    connection.execute('INSERT INTO ZFInspection VALUES(?,?,?,?,?,?,?)',(datetime.now(),self.model,self.orderNo,self.serialNo,self.inspectorId,self.correctCount,self.wrongCount))
                connection.commit()
                connection.close()
                # try:
                #     excel = pd.read_excel('ZF.xlsx')
                #     dic = excel.to_dict()
                #     for key in dic.keys():
                #         temp = []
                #         for i in range(len(dic['Model'].keys())):
                #             temp.append(dic[key][i])
                #         readData[key] = temp
                #         data[key] += readData[key]
                #     # print(readData)

                # except:
                #     pass
                # df = pd.DataFrame(data)

                # writer = pd.ExcelWriter('ZF.xlsx', engine="openpyxl")
                # df.to_excel(writer, index=False, sheet_name='ZF')
                # writer.close()
                QMessageBox.about(self, "Finish", "Inspection done.")
                exit()

    def capture(self):
        height, width, channel = self.image.shape
        step = channel * width
        qImg = QImage(self.image.data, 500, 300, step, QImage.Format_RGB888)
        self.ui.capturedImage.setPixmap(QPixmap.fromImage(qImg))
        self.isCaptured = True
        self.capturedImage = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)

    def retake(self):
        self.ui.capturedImage.setText(" ")
        self.isCaptured = False


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())

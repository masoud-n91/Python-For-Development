# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weatherGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(453, 554)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_cityName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cityName.setObjectName("lineEdit_cityName")
        self.horizontalLayout.addWidget(self.lineEdit_cityName)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.pushButton_select = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_select.setObjectName("pushButton_select")
        self.horizontalLayout_7.addWidget(self.pushButton_select)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_weatherImage = QtWidgets.QLabel(self.groupBox)
        self.label_weatherImage.setMinimumSize(QtCore.QSize(200, 200))
        self.label_weatherImage.setMaximumSize(QtCore.QSize(200, 200))
        self.label_weatherImage.setText("")
        self.label_weatherImage.setObjectName("label_weatherImage")
        self.horizontalLayout_2.addWidget(self.label_weatherImage)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.label_Description = QtWidgets.QLabel(self.groupBox)
        self.label_Description.setText("")
        self.label_Description.setObjectName("label_Description")
        self.horizontalLayout_6.addWidget(self.label_Description)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_temperature = QtWidgets.QLabel(self.groupBox)
        self.label_temperature.setText("")
        self.label_temperature.setObjectName("label_temperature")
        self.horizontalLayout_5.addWidget(self.label_temperature)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.label_wind = QtWidgets.QLabel(self.groupBox)
        self.label_wind.setText("")
        self.label_wind.setObjectName("label_wind")
        self.horizontalLayout_5.addWidget(self.label_wind)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_weather1 = QtWidgets.QLabel(self.groupBox_2)
        self.label_weather1.setText("")
        self.label_weather1.setObjectName("label_weather1")
        self.verticalLayout_6.addWidget(self.label_weather1)
        self.label_temp1 = QtWidgets.QLabel(self.groupBox_2)
        self.label_temp1.setText("")
        self.label_temp1.setObjectName("label_temp1")
        self.verticalLayout_6.addWidget(self.label_temp1)
        self.label_wind1 = QtWidgets.QLabel(self.groupBox_2)
        self.label_wind1.setText("")
        self.label_wind1.setObjectName("label_wind1")
        self.verticalLayout_6.addWidget(self.label_wind1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_weather2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_weather2.setText("")
        self.label_weather2.setObjectName("label_weather2")
        self.verticalLayout_5.addWidget(self.label_weather2)
        self.label_temp2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_temp2.setText("")
        self.label_temp2.setObjectName("label_temp2")
        self.verticalLayout_5.addWidget(self.label_temp2)
        self.label_wind2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_wind2.setText("")
        self.label_wind2.setObjectName("label_wind2")
        self.verticalLayout_5.addWidget(self.label_wind2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_weather3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_weather3.setText("")
        self.label_weather3.setObjectName("label_weather3")
        self.verticalLayout_4.addWidget(self.label_weather3)
        self.label_temp3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_temp3.setText("")
        self.label_temp3.setObjectName("label_temp3")
        self.verticalLayout_4.addWidget(self.label_temp3)
        self.label_wind3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_wind3.setText("")
        self.label_wind3.setObjectName("label_wind3")
        self.verticalLayout_4.addWidget(self.label_wind3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 453, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Select your city:"))
        self.lineEdit_cityName.setText(_translate("MainWindow", "Mashhad"))
        self.pushButton_select.setText(_translate("MainWindow", "Select"))
        self.groupBox.setTitle(_translate("MainWindow", "Today"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Forecast"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


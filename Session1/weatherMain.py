import sys
from datetime import datetime, timedelta

# API handler
from requests import get as getWeather
import json

# pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap

# GUI
from weatherGUI import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.getForecast("Mashhad")

        self.ui.pushButton_select.clicked.connect(self.getCity)

    
    def getCity(self):
        cityName = self.ui.lineEdit_cityName.text()
        self.getForecast(cityName)


    def getForecast(self, cityName):
        now = datetime.now()
        today = now.strftime("%A")
        day2 = now + timedelta(days=2)
        day3 = now + timedelta(days=3)

        self.ui.label_weather1.setText("Tommorow")
        self.ui.label_weather2.setText(day2.strftime("%A"))
        self.ui.label_weather3.setText(day3.strftime("%A"))

        response = getWeather("https://goweather.herokuapp.com/weather/" + cityName)
        print(type(response.status_code))
        if response.status_code == 200:
            weather = json.loads(response.text)
            print(weather)
            description = weather.get("description", "Sunny")
            temperature = weather.get("temperature", "11 °C")
            wind = weather.get("wind", "7 km/h")

            self.ui.label_Description.setText("Weather: " + description)
            self.ui.label_temperature.setText("Real Feel: " + temperature)
            self.ui.label_wind.setText("Wind: " + wind)
            self.loadImage(description)

            temp = weather.get("forecast")
            weather1 = temp[0]
            weather2 = temp[1]
            weather3 = temp[2]
            self.ui.label_temp1.setText(weather1.get("temperature"))
            self.ui.label_wind1.setText(weather1.get("wind"))
            self.ui.label_temp2.setText(weather2.get("temperature"))
            self.ui.label_wind2.setText(weather2.get("wind"))
            self.ui.label_temp3.setText(weather3.get("temperature"))
            self.ui.label_wind3.setText(weather3.get("wind"))

        else:
            self.ui.label_Description.setText("No response from server. Try again later or check the name of the city!")


    def loadImage(self, description):

        imagePath = self.createImagePath(description)

        pixmap = QPixmap(imagePath)  
        self.ui.label_weatherImage.setPixmap(pixmap)
        self.ui.label_weatherImage.setScaledContents(True)  

    
    def createImagePath(self, description):
        
        if description == "Sunny":
            imagePath = "images/sunny.png"
        elif description == "Cloudy":
            imagePath = "images/Cloudy.png"
        elif description == "Partly cloudy":
            imagePath = "images/partlyCloudy.png"
        elif description == "Rainny":
            imagePath = "images/lightRain.png"
        else:
            imagePath = "images/sunny.png"

        return imagePath


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())

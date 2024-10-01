import cv2
import pytesseract
from picamera import PiCamera
from time import sleep, strftime
import RPi.GPIO as GPIO
import time
import mysql.connector

mydb = mysql.connector.connect(

  host="34.88.92.247",
  user="root",
  password="balet",
  database="test"

)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Incercare")
myresult = mycursor.fetchall()

# Inițializarea camerei

camera = PiCamera()

#Initializare buton si LED-uri

BUTTON_PIN = 24
LED_PIN_V = 17
LED_PIN_V_IESIRE = 16
LED_PIN_R = 26
LED_PIN_A = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_A, GPIO.OUT)
GPIO.setup(LED_PIN_R, GPIO.OUT)
GPIO.setup(LED_PIN_V, GPIO.OUT)
GPIO.setup(LED_PIN_V_IESIRE, GPIO.OUT)
GPIO.output(LED_PIN_A, GPIO.HIGH)
GPIO.output(LED_PIN_R, GPIO.LOW)
GPIO.output(LED_PIN_V, GPIO.LOW)
GPIO.output(LED_PIN_V_IESIRE, GPIO.LOW)
GPIO.setup(LED_PIN_V, GPIO.OUT)  # Pinul LED-ului este setat ca ieșire
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Pinul butonului este setat ca intrare cu rezistență pull-up

# Setările camerei

camera.resolution = (640, 480)  # Setează rezoluția camerei
camera.framerate = 40  # Setează numărul de cadre pe secundă

# Funcție pentru detectarea textului într-o imagine

def detect_text(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convertirea imaginii la scală de gri
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]  # Aplicarea unui prag pentru binarizare
    text = pytesseract.image_to_string(gray)  # Extrage textul din imagine utilizând Tesseract OCR
    return text

# Funcție pentru capturarea unei imagini și detectarea textului

def capture_and_detect_text():

    camera.start_preview()  # Deschide previzualizarea camerei
    sleep(2)  # Așteaptă 2 secunde pentru stabilizarea camerei
    camera.capture('NumberPlate.png')  # Captură imagine și salvează-o în fișierul 'image.jpg'
    camera.stop_preview()  # Închide previzualizarea camerei
    # Încarcă imaginea capturată
    image = cv2.imread('NumberPlate.png')
    # Detectează textul în imagine
    text = detect_text(image)  
    if text:

        auxx = text.replace(" ", "")
        # Inserează data, ora și numarul de locuri ocupate în baza de date
        if(str(auxx[:-2]) == "AR90NSN"):

            sql = "SELECT * FROM Incercare WHERE numar = %s"
            adr=(auxx[:-2],)
            mycursor.execute(sql,adr)
            myresult = mycursor.fetchall()

            for x in myresult:

                if x[0] and x[1]>0:
                   
                    GPIO.output(LED_PIN_A, GPIO.LOW)
                    GPIO.output(LED_PIN_V, GPIO.HIGH)
                    time.sleep(7)
                    GPIO.output(LED_PIN_V, GPIO.LOW)
                    GPIO.output(LED_PIN_A, GPIO.HIGH)
                    sql2 = "UPDATE Incercare SET numar_locuri = numar_locuri - 1"
                    mycursor.execute(sql2)
                    mydb.commit()
                    current_date = strftime("%Y-%m-%d")
                    current_time = strftime("%H:%M:%S")
                    sql1 = "UPDATE Incercare SET data = %s,ora = %s"
                    val=(current_date,current_time)
                    mycursor.execute(sql1,val)
                    mydb.commit()
                    break
                   
        else:

            print('Nu s-a detectat text în imagine.')
            GPIO.output(LED_PIN_A, GPIO.LOW)
            GPIO.output(LED_PIN_R, GPIO.HIGH)
            time.sleep(7)
            GPIO.output(LED_PIN_R, GPIO.LOW)    
            GPIO.output(LED_PIN_A, GPIO.HIGH)

# Execută funcția principală

capture_and_detect_text()

while True:

    # Verifică starea butonului
    if GPIO.input(BUTTON_PIN) == GPIO.LOW:
       
        #Stinge LED-ul
        GPIO.output(LED_PIN_V_IESIRE, GPIO.LOW)
    else:

        #Butonul se apasa
        #Aprinde LED-ul
        sql1 = "UPDATE Incercare SET numar_locuri = numar_locuri + 1 WHERE numar_locuri < 90"
        mycursor.execute(sql1)
        mydb.commit()
        current_time1 = strftime("%H:%M:%S")
        current_date1 = strftime("%Y-%m-%d")
        sql3 = "UPDATE Incercare SET data_i = %s,ore_i = %s"
        val_i=(current_date1,current_time1)
        mycursor.execute(sql3,val_i)
        mydb.commit()      
        GPIO.output(LED_PIN_A, GPIO.LOW)
        GPIO.output(LED_PIN_V_IESIRE, GPIO.HIGH)
        time.sleep(7)
        GPIO.output(LED_PIN_V_IESIRE, GPIO.LOW)
        GPIO.output(LED_PIN_A, GPIO.HIGH)
License Plate Recognition

Project Description:

The Smart View Access system enables license plate recognition for managing access to a company’s parking lot. By using cameras connected to a Raspberry Pi, the project delivers a comprehensive solution for parking and office access control.

Technologies Used:

Hardware:

Raspberry Pi 4 Model B
Arduino Uno R3
Raspberry Pi Camera Module Version 2
LEDs and buttons for signaling

Software:

Python for image processing and API communication
MySQL for database management
React for the web interface
Android Studio for the mobile application

Technologies Used:

Python:
Core programming language used for image processing, database communication, and hardware interaction.

OpenCV:
For image preprocessing (grayscale conversion, thresholding) and license plate detection.

PyTesseract:
Optical Character Recognition (OCR) tool for extracting text from images.

MySQL:
Database used to store and manage vehicle details, access logs, and parking availability.

Raspberry Pi:
Hardware platform for running the system and interfacing with peripherals like cameras and GPIO components.

GPIO (General Purpose Input/Output):
Used to control LEDs and read button inputs for physical interaction.

PiCamera:
Captures real-time images of license plates for recognition.

Parking Lot Access:

License plate recognition using a camera connected to Raspberry Pi.
Real-time data sent to a cloud server via APIs.
Grant or deny access based on the license plate and parking slot availability.
Visual feedback with LEDs:
Green for authorized access.
Red for denied access.

Setup Instructions

Hardware Requirements:

Raspberry Pi 4 Model B.
Camera Module (compatible with Raspberry Pi).
LEDs and breadboard for signaling.
Internet connection for cloud communication.

Software Requirements:

Python 3.9+ installed on Raspberry Pi.
MySQL database (cloud-hosted or local).

![image](https://github.com/user-attachments/assets/b865e13f-a3b6-4614-989d-1b58df599a2d)

RaspberryPi Application for Access Validation in the Company Parking Lot

![image](https://github.com/user-attachments/assets/54c8acb8-af47-4df8-9e1a-9fed1492fee2)

In the diagram shown in the figure, it is presented the technical use case of the RaspberryPi system. The system is powered on when a continuously lit blue LED is observed. Turning off the system corresponds to the blue LED turning off and the inability of a person to scan a license plate. The system can be started by selecting a specific port for the hardware configuration. 
When a person enters the parking lot, after scanning their license plate, the system will search for them in the database. If the person is found in the database, they will be granted access to the parking lot, indicated by a green LED that lights up for 7 seconds. Simultaneously, the license plate number, time, and date of entry into the premises will be recorded in the database. Conversely, if the person is not found in the database or if the parking lot has reached its maximum capacity, access will be denied. This will be signaled by a red LED lighting up for 5 seconds. 
One case of system malfunction would be attempting validation without having scanned the license plate beforehand. This will be treated as an exception and will be indicated by an appropriate message, without affecting the access LEDs or making any changes to the database.
Upon leaving the premises, the person will need to press a button. If the person is found in the database, access will be granted, and the number of occupied parking spaces will automatically decrease, indicated by the green LED lighting up for 7 seconds. During access approval, the system will also calculate the number of minutes the person spent on the premises based on the recorded entry time.
Additionally, when inserting or updating the database, we can address an issue caused by a lack of internet connection. In this case, a possible solution would be to locally save the data for 24 hours.

![image](https://github.com/user-attachments/assets/ff0b8233-2343-4ec8-90fa-5b00850c2df2)

The figure above shows the architecture of the license plate authentication component.

![image](https://github.com/user-attachments/assets/5d0ae0c0-09e0-491d-b24a-eea46160b0eb)

The figure above presents a simplified visual diagram of the component for displaying available parking spaces and checking the existence of the car's license plate.

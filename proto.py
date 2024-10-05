import serial
import matplotlib.pyplot as plt
from collections import deque
import time

# Configuration du port série
port = '/dev/tty.usbmodem142103' 
baudrate = 115200  
timeout = 1  

# Ouverture du port série
ser = serial.Serial(port, baudrate, timeout=timeout)

# Send character 'S' to start the program
ser.write(bytearray('S','ascii'))

# Initialisation du timer
start_time = time.time()

# Read line   
try:
    while True:
        # Lecture des données depuis le port série
        bs = ser.readline().decode().strip()
        
        # Affichage de la mesure
        print(bs)

        # Calcul du temps écoulé depuis le dernier affichage
        elapsed_time = time.time() - start_time
        print("Temps écoulé depuis la dernière mesure :", elapsed_time, "secondes")
        
        # Réinitialisation du timer
        start_time = time.time()

except KeyboardInterrupt:
    # Fermeture du port série en cas d'interruption (Ctrl+C)
    ser.close()

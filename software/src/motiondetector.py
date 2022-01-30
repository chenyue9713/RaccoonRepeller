from periphery import GPIO
import time

pir = GPIO("/dev/gpiochip0", 6, "in")

print ("Sensor initializing . . .")
time.sleep(2) #Give sensor time to startup
print ("Active")
print ("Press Ctrl+c to end program")

try:
    while True:
        if pir.read() == True:
            print("Motion Detection!")
            time.sleep(3) #minimum time-delay after a detection is 3 sec

except KeyboardInterrupt:
    pass

finally:
    pir.close()
    print("Program end")
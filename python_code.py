import serial #Serial imported for Serial communication
import time #Required to use delay functions
import pyautogui

from directkeys import PressKey, ReleaseKey, DIK_UP,DIK_DOWN,DIK_RIGHT,DIK_LEFT, KEY_E, KEY_S, KEY_D, KEY_F


ArduinoSerial = serial.Serial('com4',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 seconds for the communication to get established

prev_1 = time.time()
prev_incoming_1 = 0

prev_2 = time.time()
prev_incoming_2 = 0

sleep_time = 0.3 # Macro for determining time in presskey

while 1:
    incoming = ArduinoSerial.readline() #read the serial data and print it as line
    #print incoming

    pres = time.time()
    #print "timeDist: " + pres - prev_1
    #print "timeDist: " + pres - prev_2
    
    if 'Forward_1' in incoming:
        PressKey(DIK_UP)
    
        
    elif 'Release_1' in incoming:
        ReleaseKey(DIK_UP)

    elif 'Forward_2' in incoming:
        PressKey(KEY_E) #up 2
        
    elif 'Release_2' in incoming:
        ReleaseKey(KEY_E)

        
    #for left right movement
    else :
        a = incoming.split('/')
        print(a)
        #temp_incoming = int(a[0])
        if len(a)==1 :
            continue
        player = a[1]
        if pres-prev_1 >= 0.8 :
        
            if player == "one\r\n":
                temp_incoming = int(a[0])
                if temp_incoming >= -25 and temp_incoming <= 25 :
                    ReleaseKey(DIK_LEFT)
                    ReleaseKey(DIK_RIGHT)

                elif temp_incoming <= -125 :
                    PressKey(DIK_RIGHT)
                    time.sleep(sleep_time)
                    ReleaseKey(DIK_RIGHT);

                elif temp_incoming >= 125 :
                    PressKey(DIK_LEFT)
                    time.sleep(sleep_time)
                    ReleaseKey(DIK_LEFT);
                
                #print 'curent Incoming_1 ' , temp_incoming
                #print 'Prev_incoming_1 ' , prev_incoming_1
                
                if temp_incoming - prev_incoming_1 >10 :
                    PressKey(DIK_LEFT)
                    time.sleep(sleep_time)
                    ReleaseKey(DIK_LEFT);
                    
                if temp_incoming - prev_incoming_1 < -10 :
                    PressKey(DIK_RIGHT)
                    time.sleep(sleep_time)
                    ReleaseKey(DIK_RIGHT);
                
                #print("1 sec passed")
                prev_1 = pres
                prev_incoming_1 = temp_incoming
            else:
                print 'player1 missed'
        if pres-prev_2 >= 0.8 :            
            if player == "two\r\n":
                temp_incoming = int(a[0])
                if temp_incoming >= -25 and temp_incoming <= 25 :
                    ReleaseKey(KEY_F)
                    ReleaseKey(KEY_S)

                elif temp_incoming <= -125 :
                    PressKey(KEY_F)
                    time.sleep(sleep_time)
                    ReleaseKey(KEY_F);

                elif temp_incoming >= 125 :
                    PressKey(KEY_S)
                    time.sleep(sleep_time)
                    ReleaseKey(KEY_S);
                
                #print 'curent Incoming_2 ' , temp_incoming
                #print 'Prev_incoming_2 ' , prev_incoming_2
                
                if temp_incoming - prev_incoming_2 >10 :
                    PressKey(KEY_S)
                    time.sleep(sleep_time)
                    ReleaseKey(KEY_S);
                    
                if temp_incoming - prev_incoming_2 < -10 :
                    PressKey(KEY_F)
                    time.sleep(sleep_time)
                    ReleaseKey(KEY_F);
                
                #print("1 sec passed")
                prev_2 = pres
                prev_incoming_2 = temp_incoming
            else:
                print 'player1 missed'    
    
    
incoming = "";

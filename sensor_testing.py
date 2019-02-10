#!/usr/bin/python
# Author: Vicente Ruben Del Pino Ruiz <https://ie.linkedin.com/in/vrdelpino>

# Test LCD libraries


from __future__ import print_function
import time, sys

#UPM library for the lcd
import pyupm_i2clcd as lcdObj
#UPM library for the buttons
import mraa as mraaL


#Define the buttons PINs
BUTTON_A = 47               
BUTTON_B = 32

#Define the joystick buttons PINs
BUTTON_UP = 46
BUTTON_DOWN = 31
BUTTON_RIGHT = 45
BUTTON_LEFT = 15
BUTTON_JT = 33


#Listen the value of the button A 
#Returns once the button has been pressed

def listenButton(buttonToRead):
 
 # Create the button object using GPIO pin 
 button = mraaL.Gpio(buttonToRead);
 #Will read the information from this button
 button.dir(mraaL.DIR_IN); 

 #Listen until be pressed
 while 1:
  value = button.read();
  if value==0:
   print("Button was pressed!");
   return

 
 

#Prints a text in a rolling way in the LCD screen
#Splits the string by /t and roll the message in the screen (two lines)

def printLCD (text):
 
 lcd = lcdObj.EBOLED();
 
 lines = text.split("/t");
 
 lastWord ="";
 
 for word in lines:
  
  lcd.setCursor(10,15);
  
  lcd.write(word);
  
  lcd.setCursor(30,15);
  
  lcd.write(lastWord);
  
  lcd.refresh();
  
  time.sleep(1);
  
  lcd.clearScreenBuffer();
  
  lastWord=word;
  
 print("Sleeping for 5 seconds...")
  
 time.sleep(5);
  


def main():
 
 #Testing LCD
 printLCD ("Hello World!! Testing LCD")
 
 #Testing Button A and B
 listenButton(BUTTON_A);
 listenButton(BUTTON_B);
 

if __name__ == '__main__':
    main()
# IOT Experiments

IOT Experiments is a test project using Intel Edison IOT, AWS and Python.

### Intel Edison IOT

What is [Intel Edison IOT]? 

Intel Edison IOT is a compute module that helps creatint prototypes and get to market faster. Bring your ideas to life with this cutting edge, adaptive technology made for a range of prototyping projects and commercial ventures.

Where find it?

I bought different components to stack to my Intel Edison IOT from [SparkFun] 
I bought the following components for my tests:
  - [SparkFun Inventors Kit]
  - [SparkFun Starter Kit]
  - [9 degrees of freedom]
  - [Battery]
  - [Oled]
 
### Setup of the components

First of all I have to assemble all the components bought.
For the first test I will assemble:
  - Intel Edison IOT
  - 9 Degrees of Freedom
  - Battery
  - OLED

What I will get with this setup is the following:
  - Access to the Movement sensors in 9 Degrees of Freedom component.
  - Access to two buttons, one joystick and OLED screen.
  - 2 Hours of battery for my device.
  
For assembling the components I followed one of the [Assemble Tutorial] in SparkFun. All the components are easy to stack and attach. The most important thing to keep in mind when assembling it is the battery component, you must be very carefull to not have a short circuit. But following the instructions of the [Battery Tutorial] shouldn't be any problem.

#### Flashing linux on the component

For flashing and configuring the component I have used the [Intel Edison Setup tool].
It should be easy enough to follow the instructions and flash the last version of linux image on the stack and configure it with ssh and internet connection to wifi.


#### Install necessary libraries

There are two libraries for Intel Edison that will help us in use the different sensors and components attached to the stack.

  - [MRAA]
    >Libmraa is a C/C++ library with bindings to Java, Python and JavaScript to interface with the IO on Galileo, Edison & other platforms, with a structured and sane API where port names/numbering matches the board that you are on. Use of libmraa does not tie you to specific hardware with board detection done at runtime you can create portable code that will work across the supported platforms.

    >The intent is to make it easier for developers and sensor manufacturers to map their sensors & actuators on top of supported hardware and to allow control of low level communication protocol by high level languages & constructs.
    
  - [UPM]
    >The UPM repository provides software drivers for a wide variety of commonly used sensors and actuators. These software drivers interact with the underlying hardware platform (or microcontroller), as well as with the attached sensors, through calls to MRAA APIs.


We''ll start installing the necesaries libraries with the MRAA.

  - First we clone the MRAA repository, build the libraries and install them:
    ```sh
    $ git clone https://github.com/intel-iot-devkit/mraa.git
    $ cd mraa
    $ mkdir build
    $ cd build
    $ cmake ..
    $ make 
    $ sudo make install
    ```

  - Once the MRAA libraries are installed we do the same with the UPM ones:
    ```sh
    $ git clone https://github.com/intel-iot-devkit/upm.git
    $ cd mraa
    $ mkdir build
    $ cd build
    $ cmake ..
    $ make 
    $ sudo make install
    ```
 ### First program in Python 

First component I will test is the [Oled], for this little program I will create a python module that will write text to the OLED screen in a rolling approach.

For this program I will use [UPM] libraries, specifically pyupm_i2clcd. The lcd screen I'm using is the ssd1306, so for the testing program the class to use in the library is the EBOLED.


  - First test is to print Hello World!! to the screen :
  ```sh
 
    from __future__ import print_function
    import time, sys

    import pyupm_i2clcd as lcdObj

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
 
      printLCD ("Hello World!! Testing LCD")


    if __name__ == '__main__':
      main()
  ```

For testing the buttons in the [Oled] component, I will use [MRAA] libraries.
Something important when using the MRAA library to read inputs from the buttons is to know exactly which is the PIN mapped to each one.

The mapping of the buttons against the PINs is the following:

  - Button A = 47
  - Button B = 32
  - Joystick Up = 46
  - Joystick Down = 31
  - Joystick Left = 15
  - Joystick Right = 45
  - Joystick Button = 33
  
  
The little module I have created will read ad-infinitum the button until is pressed. Once that is pressed it ends.

  ```sh
 
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
   
  ```




   [Intel Edison IOT]: https://software.intel.com/en-us/iot/hardware/edison
   [SparkFun]: https://www.sparkfun.com/
   [SparkFun Inventors Kit]: https://www.sparkfun.com/products/13742
   [SparkFun Starter Kit]: https://www.sparkfun.com/products/13276
   [9 degrees of freedom]: https://www.sparkfun.com/products/13033
   [Battery]: https://www.sparkfun.com/products/13037
   [Oled]: https://www.sparkfun.com/products/13035
   [Assemble Tutorial]: https://learn.sparkfun.com/tutorials/general-guide-to-sparkfun-blocks-for-intel-edison
   [Battery Tutorial]: https://www.sparkfun.com/products/13037
   [Intel Edison Setup Tool]: https://software.intel.com/es-es/get-started-edison-osx-step2
   [UPM]: https://github.com/intel-iot-devkit/upm
   [MRAA]: https://github.com/intel-iot-devkit/mraa

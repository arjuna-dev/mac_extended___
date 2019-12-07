#include <CapacitiveSensor.h>
#include "Adafruit_VL53L0X.h"

//Laser distance sensor
Adafruit_VL53L0X lox = Adafruit_VL53L0X();
int old_distance = 0;
int new_distance;
int movement;
int dir;
int measure_interval = 7;
int do_measure;
int i;

//Capacitor
CapacitiveSensor   cs_2_4 = CapacitiveSensor(2,4);

//Rotary detection
const int PinCLK   = 5; //Detect turn
const int PinDT    = 6; //Detect direction
const int PinSW    = 7; //Detect click

void setup()                    
{
    // wait until serial port opens for native USB devices
    while (! Serial) {
      delay(1);
    }
 
    if (!lox.begin()) {
      Serial.println(F("Failed to boot VL53L0X"));
      while(1);
    }
   
   Serial.begin(9600);
   pinMode(PinCLK,INPUT);
   pinMode(PinDT,INPUT);  
   pinMode(PinSW,INPUT);
   digitalWrite(PinSW, HIGH); // Pull-Up resistor for switch
}

void loop()                    
{
/*-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-*/
/*_-_-_-_-_-_-_-_-_-_-Distance sensor_-_-_-_-_-_-_-_-_-_-*/
/*-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-*/

      VL53L0X_RangingMeasurementData_t measure;
      lox.rangingTest(&measure, false);

      do_measure = i % measure_interval;
      i++;

      if (measure.RangeStatus != 4)
      {
          new_distance = measure.RangeMilliMeter;
          movement = new_distance - old_distance;
    
          if (movement > 0)
          {
            dir = 1;
          } else if (movement < 0)
          {
            dir = 0;
          }
          
          movement = abs(movement);        
      
      if (new_distance < 300 && movement > 5 && movement < 20 && !do_measure)
      {
          if (dir == 0)
          {
              Serial.println("You moved closer");
          } else if (dir == 1)
          {
              Serial.println("You moved away");
          }
      }

      old_distance = new_distance;
      }
      
//      if (measure.RangeStatus != 4) 
//      {
//        Serial.println(new_distance);
////        Serial.println(measure.RangeMilliMeter);
//      } 
//      else 
//      {
//        Serial.println("out of range");
//      }

/*-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-*/
/*_-_-_-_-_-_-_-_-_-_-Capacitive Sensor_-_-_-_-_-_-_-_-_-*/
/*-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-*/
    
    long total =  cs_2_4.capacitiveSensor(30);
//    Serial.println(total);
    if (total>40) 
    {
        Serial.println("touch");
    } else {
        Serial.println("notouch");
    }
//    delay(150);   

/*-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-*/
/*_-_-_-_-_-_-_-_-_-_-Rotary Sensor-_-_-_-_-_-_-_-_-_-_-_*/
/*-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-*/

    if (!digitalRead(PinCLK))
    {
      if (digitalRead(PinDT))
      {
        Serial.println("left");
      } else 
      {
        Serial.println("right");
      }
      delay(200);
    }
}

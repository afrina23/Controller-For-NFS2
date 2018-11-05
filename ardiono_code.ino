#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

int count=0;

//var for sonar

const int trigger1 = 6; //Trigger pin of 1st Sesnor
const int echo1 = 3; //Echo pin of 1st Sesnor
const int trigger2 = 4; //Trigger pin of 2nd Sesnor
const int echo2 = 5;//Echo pin of 2nd Sesnor

const int decoderPin = 8;

long time_taken;
int dist,distL,distR;

 

void setup() {
Serial.begin(9600); 

  count=0;
  Serial.println ("Ashchi");
  mpu.calibrateGyro();
  mpu.setThreshold(3);
  Serial.println ("Done setup");

pinMode(trigger1, OUTPUT); 
pinMode(echo1, INPUT); 
pinMode(trigger2, OUTPUT); 
pinMode(echo2, INPUT); 
pinMode (decoderPin, OUTPUT);  
}



/*###Function to calculate distance###*/
void calculate_distance(int trigger, int echo)
{
digitalWrite(trigger, LOW);
delayMicroseconds(2);
digitalWrite(trigger, HIGH);
delayMicroseconds(10);
digitalWrite(trigger, LOW);

time_taken = pulseIn(echo, HIGH);
dist= time_taken*0.034/2;
if (dist>50)
dist = 50;
}

void loop() { //infinite loopy
    calculate_distance(trigger1,echo1);
    distL =dist; //get distance of left sensor
    
    calculate_distance(trigger2,echo2);
    distR =dist; //get distance of right sensor
    
    //Uncomment for debudding
    Serial.print("L=");
    Serial.println(distL);
    //Serial.print("R=");
   // Serial.println(distR);
 
    if( distL>=0 && distL<=9 ){
    
        Serial.println("Forward_1"); //delay (50);
      
    }
    
    /*
    if(distR>=0 && distR<=30  && distR == 50 )
    {
      Serial.println("Forward_2"); delay (500);
      
    }
    */
    //backward
    
    if(distL>9 && distL<=15 ){
    
        Serial.println("Backward_1"); //delay (500);
      
    }
// release all
    if(distL>15){
    
        Serial.println("Release"); //delay (500);
      
    }
    /*
    if (distR>30 && distR<50) //Detect both hands
    {
      Serial.println("Backward_2"); delay (500);
      
    }

    */
//    accelShow();
    //delay(1000); 
}


void accelShow()
{
//  Vector rawAccel = mpu.readRawAccel();

  digitalWrite(decoderPin, LOW); // accel 1 activated
  Serial.println ("Accelerometer 1");
  Vector normAccel = mpu.readNormalizeAccel();
  Serial.print(" X = ");
  Serial.print(normAccel.XAxis);

  Serial.print(" Y = ");
  Serial.print(normAccel.YAxis);

  Serial.print(" Z = ");
  Serial.println(normAccel.ZAxis);


  if (normAccel.YAxis > -2 && normAccel.YAxis < 2) Serial.println ("Straight");
  if (normAccel.YAxis >= 2) Serial.println ("Left");
  if (normAccel.YAxis <= -2) Serial.println ("Right");
  delay(1000);


  digitalWrite(decoderPin, HIGH); // accel 2 activated
  normAccel = mpu.readNormalizeAccel();
  Serial.println ("Accelerometer 2");
  Serial.print(" X = ");
  Serial.print(normAccel.XAxis);

  Serial.print(" Y = ");
  Serial.print(normAccel.YAxis);

  Serial.print(" Z = ");
  Serial.println(normAccel.ZAxis);


  if (normAccel.YAxis > -2 && normAccel.YAxis < 2) Serial.println ("Straight");
  if (normAccel.YAxis >= 2) Serial.println ("Left");
  if (normAccel.YAxis <= -2) Serial.println ("Right");
}

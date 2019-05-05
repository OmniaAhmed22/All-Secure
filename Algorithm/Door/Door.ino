#include<Servo.h>

Servo Door;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
  Door.attach(5); //Attach Vertical Servo to Pin 5
  Door.write(0);
}

void loop() {
  // put your main code here, to run repeatedly:
if(Serial.available() > 0) {
       char data = Serial.parseInt();
        Serial.print("py");
    if (data == 0){
     Serial.print("0");
      Door.write (0);
    }
    else{
    //if (data == 1) {
       Serial.print("1");
      Door.write (90);
    }
}
}

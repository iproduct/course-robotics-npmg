/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
 
  This example code is in the public domain.
 */
 
// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
#define LED 1
#define BUTTON 0

int buttonState;
int light = LOW;
// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode(LED, OUTPUT);     
  pinMode(BUTTON, INPUT);   
  Serial.begin (115200);  
}

// the loop routine runs over and over again forever:
void loop() {
  buttonState = digitalRead(BUTTON);
  if(buttonState == HIGH) {
    light = light == LOW ? HIGH: LOW;
    digitalWrite(LED, light);   // turn the LED on (HIGH is the voltage level)
    delay(300);               // wait for a second     
  } else {
    digitalWrite(LED, LOW);  
  }
  delay(20);
}

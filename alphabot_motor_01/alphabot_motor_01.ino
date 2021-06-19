// Motor A
#define motor1Pin1 1
#define motor1Pin2 2
#define enable1Pin 3

// Setting PWM properties
const int freq = 30000;
const int pwmChannel = 0;
const int resolution = 8;
int dutyCycle = 200;

void setup() {
  // sets the pins as outputs:
  pinMode(motor1Pin1, OUTPUT);
  pinMode(motor1Pin2, OUTPUT);
  pinMode(enable1Pin, OUTPUT);
  Serial.begin(115200);
  delay(500);
}

void loop() {
  Serial.println("Motor Test");

  // Move the DC motor forward at maximum speed
  Serial.println("Moving Forward");
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, HIGH);
  for (int i = 0; i < 255; i++) {
    analogWrite(enable1Pin, i);
    delay(10);
  }
  for (int i = 255; i >= 0; i--) {
    analogWrite(enable1Pin, i);
    delay(10);
  }
  //  digitalWrite(enable1Pin, HIGH);
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, LOW);
  analogWrite(enable1Pin, 0);
  delay(2000);

}

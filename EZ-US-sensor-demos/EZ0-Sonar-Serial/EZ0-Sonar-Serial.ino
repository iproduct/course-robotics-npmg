// Connect Tx....D8
// Connect Rx ....D9
#define RXD2 16
#define TXD2 17
#define TRIG 5

char reading[3];

void setup() {
  // put your setup code here, to run once:
  // set the data rate for the SoftwareSerial port
  Serial.begin(115200);
  Serial2.begin(9600, SERIAL_8N1, RXD2, TXD2, true);
  Serial.println("Serial Txd is on pin: " + String(TXD2));
  Serial.println("Serial Rxd is on pin: " + String(RXD2));
  delay(250);
  Serial.println("Calibrartion Cycle ");
  delay(150);
  pinMode(TRIG, OUTPUT);
  digitalWrite(TRIG, LOW);
}

void read_distance() {
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(30);
  while (Serial2.available()) {
    if (Serial2.read() == 0x52) {
      Serial2.readBytes(reading, 3);
    }
  }
  digitalWrite(TRIG, LOW);
}

void loop() {
  //  while (Serial2.available()) {
  //    Serial.print(char(Serial2.read()));
  //  }

  read_distance();
  int Final_inch = (reading[0] - 48) * 100 + (reading[1] - 48) * 10 + (reading[2] - 48) ;
  float Final_cm = Final_inch * 2.54;
  Serial.print(Final_inch);
  Serial.println(" Inch ");
  Serial.print(Final_cm);
  Serial.println(" cm ");
  delay(200);
}

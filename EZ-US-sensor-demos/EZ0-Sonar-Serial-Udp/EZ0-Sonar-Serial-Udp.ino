#include <WiFi.h>
#include <WiFiUdp.h>
#include "arduino_secrets.h"

// Connect Tx....D8
// Connect Rx ....D9
#define RXD2 16
#define TXD2 17
#define TRIG 5

const char* ssid = SECRET_SSID;
const char* pass = SECRET_PASS;
const char* udp_server_ip = "192.168.1.100";
unsigned int udp_server_port = 4210;
unsigned int localUdpPort = 4210; 
const int period = 200;
boolean connected = false; //Are we currently connected?
 // local port to listen on
char incomingPacket[255];  // buffer for incoming packets
char eventString[256];
WiFiUDP Udp;

long timestamp;
const int LED = 23;

char reading[3];

void setup() {
  //Initialize serial and wait for port to open:
  Serial.begin(115200);
  Serial.setDebugOutput(true);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  // attempt to connect to Wifi network:
  Serial.println();
  Serial.println();

  Serial.printf("Connecting to %s ", ssid);
  WiFi.mode(WIFI_STA);
  //register event handler
  WiFi.onEvent(WiFiEvent);
  WiFi.begin(ssid, pass);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
//  printWifiStatus();
  
//  Udp.begin(localUdpPort);
//  Serial.printf("Now listening at IP %s, UDP port %d\n", WiFi.localIP().toString().c_str(), localUdpPort);

  pinMode(LED, OUTPUT);     // set the LED pin mode

  // put your setup code here, to run once:
  // set the data rate for the SoftwareSerial port
  Serial2.begin(9600, SERIAL_8N1, RXD2, TXD2, true); // second arg true = invert the signals
  Serial.println("Serial Txd is on pin: " + String(TXD2));
  Serial.println("Serial Rxd is on pin: " + String(RXD2));
  delay(250);
  Serial.println("Calibrartion Cycle ");
  delay(150);
  pinMode(TRIG, OUTPUT);
  digitalWrite(TRIG, LOW);
}

void loop() {
  //  while (Serial2.available()) {
  //    Serial.print(char(Serial2.read()));
  //  }
  digitalWrite(LED, HIGH);  
  read_distance();
  int distance_inch = (reading[0] - 48) * 100 + (reading[1] - 48) * 10 + (reading[2] - 48) ;
  float distance_cm = distance_inch * 2.54;
  Serial.print(distance_inch);
  Serial.println(" Inch ");
  Serial.print(distance_cm);
  Serial.println(" cm ");
  
  timestamp = millis();
  if(connected){
    sendReadingUdp(timestamp, distance_cm);
  }

  digitalWrite(LED, LOW);  

  long waitFor = millis()-timestamp;
  if(waitFor < period) 
    delay(period - waitFor);
}


// utility functions
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

void printWifiStatus() {
  // print the SSID of the network you're attached to:
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // print your WiFi shield's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  // print the received signal strength:
  long rssi = WiFi.RSSI();
  Serial.print("signal strength (RSSI):");
  Serial.print(rssi);
  Serial.println(" dBm");
}

//wifi event handler
void WiFiEvent(WiFiEvent_t event){
    switch(event) {
      case SYSTEM_EVENT_STA_GOT_IP:
          //When connected set 
          Serial.print("WiFi connected! IP address: ");
          Serial.println(WiFi.localIP());  
          //initializes the UDP state
          //This initializes the transfer buffer
          Udp.begin(WiFi.localIP(), localUdpPort);
          connected = true;
          break;
      case SYSTEM_EVENT_STA_DISCONNECTED:
          Serial.println("WiFi lost connection");
          connected = false;
          break;
      default: break;
    }
}

String sendReadingUdp(long timestamp, float distance) {
      int result = Udp.beginPacket(udp_server_ip, udp_server_port);
      if(result > 0) {
        //Send a packet
        // Serial.printf("{\"timestamp\":%d, \"distance\":%8.2f}", timestamp, distance);
        Udp.printf("{\"timestamp\":%d, \"distance\":%8.2f}", timestamp, distance);
        Udp.endPacket();
      }
}

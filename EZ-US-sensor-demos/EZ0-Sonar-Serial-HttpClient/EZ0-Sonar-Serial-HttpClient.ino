#include <WiFi.h>
#include <HTTPClient.h>
#include "arduino_secrets.h"

// Connect Tx....D8
// Connect Rx ....D9
#define RXD2 16
#define TXD2 17
#define TRIG 5

const char* ssid = SECRET_SSID;
const char* pass = SECRET_PASS;
const char* apiUrl = "http://192.168.1.100:8080/api/events";    // your Events API URL
const int period = 200;

const char* headers[1]= {"Location"};
long timestamp;
const int LED = 23;

HTTPClient http;

char reading[3];

void setup() {
  //Initialize serial and wait for port to open:
  Serial.begin(115200);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  // attempt to connect to Wifi network:
  Serial.println();
  Serial.println();

  Serial.print("Connecting to: ");
  Serial.println(ssid);

  WiFi.begin(ssid, pass);

  while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
  }
  printWifiStatus();
  
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
  digitalWrite(LED, HIGH);  
  read_distance();
  int distance_inch = (reading[0] - 48) * 100 + (reading[1] - 48) * 10 + (reading[2] - 48) ;
  float distance_cm = distance_inch * 2.54;
  Serial.print(distance_inch);
  Serial.println(" Inch ");
  Serial.print(distance_cm);
  Serial.println(" cm ");

  timestamp = millis();
  sendReadingPOST(timestamp, distance_cm);
  digitalWrite(LED, LOW);  

  long waitFor = millis()-timestamp;
  if(waitFor > 0) 
    delay(waitFor);
}

// utility functions
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

String sendReadingPOST(long timestamp, float distance) {
  Serial.print("[HTTP] begin...\n");
  http.begin(apiUrl); //HTTP

  Serial.print("[HTTP] Post: ");
  Serial.println(apiUrl);
  http.addHeader("Content-Type", "application/json");             //Specify content-type header
  char eventString[256];
  sprintf(eventString, "{\"timestamp\":%d, \"distance\":%8.2f}", timestamp, distance);
  Serial.println(eventString);
  http.collectHeaders(headers, 1);
  int httpResponseCode = http.POST(eventString);   //Send the actual POST request
 
  if(httpResponseCode>0){
    String response = http.getString();  //Get the response to the request
    Serial.print("Response code: ");    
    Serial.println(httpResponseCode);   //Print return code
    Serial.println(response);           //Print request answer
    Serial.print("Location : ");    
    Serial.println(http.header("Location"));   //Print Location header
    return response;
  }else{
    Serial.print("Error on sending POST: ");
    Serial.println(httpResponseCode);
    return "";
  }
  http.end();
}

// Include AWS IoT Certificates
#include "aws_iot_certs.h"
// Add the Wifi Library
#include "WiFi.h"
// Add the DFH Library
#include "DHT.h"
// Import MQTT and Wifi Secure used for AWS IoT
#include <WiFiClientSecure.h>
#include <MQTT.h>
// Import the Arduino Json Library
// Used for sending payload information to AWS IoT Core. 
#include <ArduinoJson.h>
// Intiallize the WifiClientSecure
WiFiClientSecure net = WiFiClientSecure();
// Setup MQTT Client with 512 packet size
MQTTClient client = MQTTClient(512);
// Defining our AWS IoT Configuration
#define DEVICE_NAME "eowings_ESP32"
#define AWS_IOT_ENDPOINT "a20g1zvgahvlpi-ats.iot.us-east-1.amazonaws.com"
//#define AWS_IOT_TOPIC "$aws/things/eowings_ESP32/shadow/update"
#define AWS_MAX_RECONNECT_TRIES 10
// Define Publish and Describe Topics
// Make sure to add your topics names
#define AWS_IOT_PUBLISH_TOPIC   "esp32/10/data"
//esp32/pub"
#define AWS_IOT_SUBSCRIBE_TOPIC "esp32/10/sub"
// Define the Network Specifications
#define WIFI_NETWORK "FiOS-0JJX3-Guest"
#define WIFI_PASS "P@ssWord"
#define WIFI_TIMEOUT_MS 20000
// Define the DHT Type
#define DHTTYPE DHT22
// Define the GPIO Pin Associated to the ESP32
#define DHTPIN 14
//---------------------------------------------------------
// DHT22 Sensor Function
void initializeDHT22Sensor() {
  // Initialize DHT22 Sensor
  DHT dht(DHTPIN, DHTTYPE);
  pinMode(DHTPIN, INPUT);
  dht.begin();  
  
  // Get the Temperature
  float temperature = dht.readTemperature(true);
  Serial.println(temperature);
  
  // Get Humidity Data
  float humidity = dht.readHumidity();
  Serial.println(humidity);
StaticJsonDocument<200> doc;
  doc["temperature"] = temperature;
  doc["humidity"] = humidity;
  
  char jsonBuffer[512];
  serializeJson(doc, jsonBuffer); // print to client
  client.publish(AWS_IOT_PUBLISH_TOPIC, jsonBuffer);

}
// End of Function
//------------------------------------------------------
// AWS Connection Function
void connectToAWSIoT() {
  // Adding the IoT Certificates for our AWS IoT Thing
  net.setCACert(AWS_ROOT_CA_CERT);
  net.setCertificate(AWS_CLIENT_CERT);
  net.setPrivateKey(AWS_PRIVATE_KEY);
// Associating the Endpoint and Port Number
  client.begin(AWS_IOT_ENDPOINT, 8883, net);
// Setting up Retry Count
  int retries = 0;
  Serial.print("Connecting to AWS IOT");
// Attempting Connection in While Loop
  while (!client.connect(DEVICE_NAME) && retries < AWS_MAX_RECONNECT_TRIES) {
    Serial.print(".");
    delay(100);
    retries++;
  }
// Setup If Else Statement to handle connections and failures. 
  if(!client.connected()){
    Serial.println("AWS Timed Out!");
    return;
  } else {
    Serial.println("Connected to AWS IoT Thing!");
// Subscribe to the AWS IoT Device 
    client.subscribe(AWS_IOT_SUBSCRIBE_TOPIC);
  }
}
// End of Function
//------------------------------------------------------
// Connection to Wifi Function
void connectToWifi() {
  Serial.print("Connecting to Wifi");
  // In order to connect to an existing network we need to utilize station mode. 
  WiFi.mode(WIFI_STA);
  
  // Connect to the Network Using SSID and Pass. 
  WiFi.begin(WIFI_NETWORK, WIFI_PASS);
// Store the time it takes for Wifi to connect. 
  unsigned long startAttemptTime = millis();
// The While loop utilize the Wifi Status to check if its connect as well as makes sure that the timeout was not reached. 
  while(WiFi.status() != WL_CONNECTED && millis() - startAttemptTime < WIFI_TIMEOUT_MS){   
    Serial.print(".");
    
    // Deply so this while loop does not run so fasts. 
    delay(100);
  }
if(WiFi.status() != WL_CONNECTED){
    Serial.println("Failed to Connect to Wifi");
    esp_deep_sleep_start();
  } else {
  }
  
}
// End Function
//---------------------------------------
void setup(){
  Serial.begin(9600);
//  connectToWifi();
//  delay(2000);
//  connectToAWSIoT();
}
void loop() {
  connectToWifi();
  delay(2000);
  connectToAWSIoT();
  initializeDHT22Sensor();
  WiFi.disconnect();
  client.loop();
  delay(900000);
}

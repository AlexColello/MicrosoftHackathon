#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <Arduino.h>
#include <ArduinoJson.h>

char WIFI_SSID[] = "SpectrumSetup-4D";
char WIFI_PASS[] = "statustheory991";

// button pressed for my ID 
char server[] = "usc-squad-hackathon.azurewebsites.net";

//CA certificate for authenticating and making HTTPS connection 
const char* ca_cert = \ 
  "-----BEGIN CERTIFICATE-----\n" \
  "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\n" \
  "-----END CERTIFICATE-----\n";

//Button pins
#define b1 16
#define b2 17

//WiFi Client for sending requests
WiFiClientSecure client;

//State machine for buttton handling 
int state = 0; 
int ostate = 0; 
int timer = 0; 

void setup()
{
  //Configure pins for button input
  pinMode(b1, INPUT_PULLUP);
  pinMode(b2, INPUT_PULLUP);

  Serial.begin(9600);
  delay(10);
  WiFi.mode(WIFI_STA);

  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(WIFI_SSID);

  //Connect to WiFi 
  WiFi.begin(WIFI_SSID, WIFI_PASS);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  
  client.setCACert(ca_cert);

  //Connect to server 
  Serial.println("\nStarting connection to server...");
  if (!client.connect(server, 443))
    Serial.println("Connection failed!");
  else {
    Serial.println("Connected to server!");
  }
  
}

void loop()
{
  delay(200);
  // We now create a URI for the request
  String url = "/alert";

  StaticJsonDocument<64> doc;
  
  doc["numButtons"] = "0";
  doc["deviceID"] = "a2hc"; 
  String output = "";
  
  //Check if both buttons are pressed 
  if( digitalRead(b1) == 0 && digitalRead(b2) == 0) {
    state = 2;
  }
  //Check if only one button is pressed 
  else if (digitalRead(b1)==0 || digitalRead(b2)==0) {
    if (state != 2){
      state = 1; 
    }
  }
  //Reset to zero if one minute has passed 
  else if (timer >=300){
    timer=0;
    state=0;
  }
  else {
    timer++;
  }

  //Send POST request if the state has changed 
  if ((state != ostate) && (state !=0)){
    ostate = state; 
    doc["numButtons"] = String(state);
    serializeJson(doc, output);
    client.println("POST https://usc-squad-hackathon.azurewebsites.net" + url + " HTTP/1.1");
    client.println("Host: " + String(server));
    client.println("Content-Type: application/json");
    client.println("Accept: */*");
    client.println("Content-Length: " + String(output.length()));
    client.println("Connection: keep-alive");
    client.println();
    client.println(output);
  
    String line = client.readStringUntil('\r');
    Serial.print(line);
  }

  // if there are incoming bytes available
  // from the server, read them and print them:
  while (client.available()) {
    char c = client.read();
    Serial.write(c);
  }
}

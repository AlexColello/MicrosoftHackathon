



// Set LED_BUILTIN if it is not defined by Arduino framework
// #define LED_BUILTIN 13
#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <Arduino.h>
#include <ArduinoJson.h>


char WIFI_SSID[] = "SpectrumSetup-4D";
char WIFI_PASS[] = "statustheory991";

// int status = WL_IDLE_STATUS;
// button pressed for my ID 
char server[] = //  "www.google.com"; 
   "usc-squad-hackathon.azurewebsites.net";

const char* ca_cert = \ 
  "-----BEGIN CERTIFICATE-----\n" \
  "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\n" \
  "-----END CERTIFICATE-----\n";

//Button pins
#define b1 16
#define b2 17

// HttpClient client = HttpClient(wifi, server, port);
WiFiClientSecure client;

void setup()
{
  pinMode(b1, INPUT_PULLUP);
  pinMode(b2, INPUT_PULLUP);


  Serial.begin(9600);
  delay(10);
  WiFi.mode(WIFI_STA);

  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(WIFI_SSID);

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

   Serial.println("\nStarting connection to server...");
  if (!client.connect(server, 443))
    Serial.println("Connection failed!");
  else {
    Serial.println("Connected to server!");
    // Make a HTTP request:
    /*
    client.println("GET https://usc-squad-hackathon.azurewebsites.net/ HTTP/1.0");
    client.println("Host: usc-squad-hackathon.azurewebsites.net");
    client.println("Connection: close");
    client.println();
    


    while (client.connected()) {
      String line = client.readStringUntil('\n');
      if (line == "\r") {
        Serial.println("headers received");
        break;
      }
    }
    // if there are incoming bytes available
    // from the server, read them and print them:
    while (client.available()) {
      char c = client.read();
      Serial.write(c);
    }
    */
   //client.stop();
  }
}

int value = 0;

void loop()
{

  if(digitalRead(b1) && digitalRead(b2)) {
    // Send http post here notifying to call whoever
  }
  delay(1000);
  ++value;
/*
  Serial.print("connecting to ");
  Serial.println(server);

  // Use WiFiClient class to create TCP connections
  //WiFiClient client;
  const int httpPort = 443;
  if (!client.connect(server, httpPort)) {
    Serial.println("connection failed");
    return;
  }
*/
    // We now create a URI for the request
   String url = "/test-post/";

    StaticJsonDocument<64> doc;
    
    doc["test"] = "test";
    String output = "";

    serializeJson(doc, output);

    client.println("POST https://usc-squad-hackathon.azurewebsites.net" + url + " HTTP/1.1");
    client.println("Host: " + String(server));
    client.println("Content-Type: application/json");
    client.println("Accept: */*");
    client.println("Content-Length: " + String(output.length()));
    client.println("Connection: keep-alive");
    client.println();
    client.println(output);


    while (client.connected()) {
      String line = client.readStringUntil('\n');
      if (line == "\r") {
        Serial.println("headers received");
        break;
      }
    }
    // if there are incoming bytes available
    // from the server, read them and print them:
    while (client.available()) {
      char c = client.read();
      Serial.write(c);
    }

    Serial.println("POST https://usc-squad-hackathon.azurewebsites.net" + url + " HTTP/1.1");
    Serial.println("Host: " + String(server));
    Serial.println("Accept: */*");
    Serial.println("Connection: keep-alive");
    Serial.println("Content-Type: application/json");
    Serial.println("Content-Length: " + String(output.length()));
    Serial.println("Body: " + output);
    Serial.println();
    /*
    client.println("Accept: */ /*");
    client.println("Content-Length: " + String(message.length()));
    client.println();
    client.println(message);
    */

    unsigned long timeout = millis();
    while (client.available() == 0) {
        if (millis() - timeout > 5000) {
            Serial.println(">>> Client Timeout !");
            client.stop();
            return;
        }
    }

    // Read all the lines of the reply from server and print them to Serial
    while(client.available()) {
        String line = client.readStringUntil('\r');
        Serial.print(line);
    }

    Serial.println();
    Serial.println("closing connection");

}


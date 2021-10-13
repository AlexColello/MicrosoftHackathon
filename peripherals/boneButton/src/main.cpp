// Set LED_BUILTIN if it is not defined by Arduino framework
// #define LED_BUILTIN 13
#include <WiFi.h>

char WIFI_SSID[] = "SpectrumSetup-4D";
char WIFI_PASS[] = "statustheory991";

// int status = WL_IDLE_STATUS;
char server[] = "usc-squad-hackathon.azurewebsites.net";


// HttpClient client = HttpClient(wifi, server, port);


void setup()
{
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
}

int value = 0;

void loop()
{
  delay(5000);
  ++value;

  Serial.print("connecting to ");
  Serial.println(server);

  // Use WiFiClient class to create TCP connections
  WiFiClient client;
  const int httpPort = 80;
  if (!client.connect(server, httpPort)) {
    Serial.println("connection failed");
    return;
  }

    // We now create a URI for the request
    String url = "/test-post/";
    String message = "yayAlexSetUpPostRequests";

    Serial.print("Requesting URL: ");
    Serial.println(url);

    // This will send the request to the server
    client.print(String("POST ") + url + message);
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

const int ledPin =11;
const int soilPin = 20;

void setup(){
    pinMode(ledPin,OUTPUT);
    Serial.begin(9800);
}

void loop(){
    int val = analogRead(soilPin);
    Serial.print("Soil : ");
    Serial.println(val);
    digitalWrite(ledPin, HIGH)
    delay(1000);
    digitalWrite(ledPin, LOW);
    delay(100);
}
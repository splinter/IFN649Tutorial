#define LEDPIN 11
void setup() {
  Serial.begin(9600);
  Serial1.begin(9600);
}

void loop() {
  if(Serial1.available()>0){
    String cmd = Serial1.readString();
    manageLED(cmd);
  }
}

void manageLED(String cmd){
  if(cmd.indexOf("CMD") < 0){
    return;
  }
  if(cmd.indexOf("ON") > 0) {
    digitalWrite(LEDPIN, HIGH);
  }
  if(cmd.indexOf("OFF") > 0) {
    digitalWrite(LEDPIN, LOW);
  }
}

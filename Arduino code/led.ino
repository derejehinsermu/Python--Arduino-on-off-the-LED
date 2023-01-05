const int ledPin = 13;
int incomingByte;      // variable stores  serial data
void setup() {

  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  

}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    // if it's a capital H (ASCII 72), turn on the LED:
    if (incomingByte == 'H') {
      digitalWrite(ledPin, HIGH);
    }
    // if it's an L (ASCII 76) turn off the LED:
    if (incomingByte == 'L') {
      digitalWrite(ledPin, LOW);
    }
  }
}

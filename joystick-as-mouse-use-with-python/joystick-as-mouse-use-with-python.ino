void setup() {
  Serial.begin(9600);
}

// mappings for a 4k display

void loop() {
  int x = map(analogRead(A1), 0, 1023, 2560, 0); 
  int y = map(analogRead(A0), 0, 1023, 1440, 0);
  Serial.print(x);
  Serial.print(' ');
  Serial.println(y);
  delay(120);
}

void setup() {
  Serial.begin(9600); // set the baud rate
  Serial.println("Ready"); // print "Ready" once
}
void loop() {
  int i;
  for(i=0; i<30;i++){
  	Serial.println(i); // send the data back in a new line so that it is not all one long line
  delay(100); // delay for 1/10 of a second
  }
}

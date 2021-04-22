#define echopin 2
#define trigpin 3
long duration;
long distance;
void setup() {
  // put your setup code here, to run once:
  pinMode(trigpin,OUTPUT);
  pinMode(echopin,INPUT);
  Serial.begin(9600);
  Serial.println("Arduino interface With Ultrasonic");
  delay(100);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(trigpin,LOW);
  delayMicroseconds(2);
  digitalWrite(trigpin,HIGH);
  delayMicroseconds(10);
  digitalWrite(trigpin,LOW);
  duration = pulseIn(echopin,HIGH);
  distance= duration * 0.034/2; //speed of sound divided by 2 (go and back)
  Serial.print(distance);
  Serial.print("CM");
  delay(100);
  Serial.print(distance/2.54);
  Serial.print("inch");
  delay(100);
}

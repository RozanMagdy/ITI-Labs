#define CLK 2
#define DT 3
#define SW 4
int Encoder_Postion = 0;
void setup() {
  Serial.begin(9600);
  pinMode(CLK, INPUT);
  pinMode(DT, INPUT);
  pinMode(SW, INPUT);
  attachInterrupt(0, Encoder_Action, CHANGE);
}
int valRotary,lastValRotary;
void loop() {
  int btn = digitalRead(SW);
  Serial.print(btn);
  Serial.print(" ");
  Serial.print(valRotary);
  if(valRotary>lastValRotary)
  {
  Serial.print("CW");
  }
  if(valRotary<lastValRotary)  
  {
  Serial.print("CCW");
  }
  lastValRotary = valRotary;
  Serial.println(" ");
  delay(250);
}
void Encoder_Action()
{
  if (digitalRead(CLK) == digitalRead(DT))
  {
  Encoder_Postion++;
  }
  else
  {
  Encoder_Postion--;
  }
  valRotary = Encoder_Postion/2.5;
}

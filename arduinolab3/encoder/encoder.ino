float pi= 3.14;
float T= 30.0;
float r= 0.15;
const int ch_A = 2;
const int ch_B = 3;
float cnt = 0;
float F = 0;
float rpm = 0;
float t1 ;
float t2  = 0;
float  w = 0;
float v = 0;
int last_cnt = 0;

void setup() {
  Serial.begin(9600);
  attachInterrupt(digitalPinToInterrupt(ch_A), count, RISING);
  pinMode(ch_B, INPUT);

}

void loop() 
{
 
//Serial.println(cnt);
t1 = millis();
if ((t1 - t2) >= T)
{
  F = (cnt - last_cnt) / ((t1 - t2)/1000);
  rpm = F *( 60.0 / 20.0);
  w  = 2.0 * pi * rpm/60.0; // rad/sec
  v = w * r;
  Serial.println(v);
  t2 = millis();
  last_cnt = cnt;
}
}
void count()
{
 
  if (digitalRead(ch_B)== HIGH) 
  {
    cnt = cnt + 1;
    
  }
  else
  {
    cnt = cnt - 1;
      
  }
  
    
}

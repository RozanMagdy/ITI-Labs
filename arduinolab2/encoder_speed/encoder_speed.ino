 #define outA 2 //A+
  float vel = 0;
  volatile byte counter = 0;
  unsigned long staT = 0;
  unsigned long stoT = 0;



void setup() {
  //define pins 
  pinMode(outA, INPUT_PULLUP);  

  Serial.begin(9600);

  attachInterrupt(0, doEncoderA, RISING);
  interrupts(); 
}

void loop() {
  staT = 0;
  stoT = 0;
  counter = 0;
  staT = micros(); //start_time
  while (counter < 20) { 
    //Serial.println(counter);
  }
  stoT = micros(); //End 
  float vel = 1000000 / (stoT - staT);     //calculate velocity    //rps 
  Serial.println("speed = ");
  Serial.println(vel);
}


void doEncoderA()  {
counter = counter+1;
}

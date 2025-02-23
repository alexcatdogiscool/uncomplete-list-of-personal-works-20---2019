const int ldr = A0;
const int green = A1;
const int yellow = A2;
const int red = A3;



void setup() {

  
  Serial.begin(9600);

  pinMode(ldr,INPUT);
  pinMode(green, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(red, OUTPUT);
  


}


void loop() {

  int l = analogRead(ldr);

  if (l < 150) {
    analogWrite(green, 700);
    analogWrite(red, 0);
    analogWrite(yellow, 0);
  }
  if (l < 250 and l > 150) {
    analogWrite(yellow, 700);
    analogWrite(green, 0);
    analogWrite(red, 0);
  }
  if (l < 350 and l > 250) {
    analogWrite(green, 0);
    analogWrite(yellow, 0);
    analogWrite(red, 600);
  }

  Serial.println(analogRead(ldr));
}

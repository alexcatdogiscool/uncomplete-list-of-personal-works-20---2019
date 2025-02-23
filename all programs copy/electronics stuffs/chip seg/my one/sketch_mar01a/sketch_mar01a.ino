const int ones = A0;
const int twos = A1;
const int fours = A2;
const int eights = A3;
const float ldr = A4;
const float sens = A5;
const int fff = A6;




void setup() {

pinMode(ones,OUTPUT);
pinMode(twos,OUTPUT);
pinMode(fours,OUTPUT);
pinMode(eights,OUTPUT);
pinMode(ldr, INPUT);
pinMode(sens,INPUT);
pinMode(fff,OUTPUT);

Serial.begin(9600);

  

}


void zero() {
  digitalWrite(ones,LOW);
  digitalWrite(twos,LOW);
  digitalWrite(fours,LOW);
  digitalWrite(eights,LOW);
}

void one() {
  digitalWrite(ones,HIGH);
digitalWrite(twos,LOW);
digitalWrite(fours,LOW);
digitalWrite(eights,LOW);
}

void two() {
  digitalWrite(ones,LOW);
digitalWrite(twos,HIGH);
digitalWrite(fours,LOW);
digitalWrite(eights,LOW);
}

void three() {
  digitalWrite(ones,HIGH);
digitalWrite(twos,HIGH);
digitalWrite(fours,LOW);
digitalWrite(eights,LOW);
}

void four() {
  digitalWrite(ones,LOW);
digitalWrite(twos,LOW);
digitalWrite(fours,HIGH);
digitalWrite(eights,LOW);
}

void five() {
  digitalWrite(ones,HIGH);
digitalWrite(twos,LOW);
digitalWrite(fours,HIGH);
digitalWrite(eights,LOW);
}

void six() {
  digitalWrite(ones,LOW);
digitalWrite(twos,HIGH);
digitalWrite(fours,HIGH);
digitalWrite(eights,LOW);
}

void seven() {
  digitalWrite(ones,HIGH);
digitalWrite(twos,HIGH);
digitalWrite(fours,HIGH);
digitalWrite(eights,LOW);;
}

void eight() {
  digitalWrite(ones,LOW);
digitalWrite(twos,LOW);
digitalWrite(fours,LOW);
digitalWrite(eights,HIGH);
}

void nine() {
  digitalWrite(ones,HIGH);
digitalWrite(twos,LOW);
digitalWrite(fours,LOW);
digitalWrite(eights,HIGH);
}


void segdisp(int number) {
  if (number == 0) {
    zero();
  }

  if (number == 1) {
    one();
  }

  if (number == 2) {
    two();
  }

  if (number == 3) {
    three();
  }

  if (number == 4) {
    four();
  }

  if (number == 5) {
    five();
  }

  if (number == 6) {
    six();
  }

  if (number == 7) {
    seven();
  }

  if (number == 8) {
    eight();
  }

  if (number == 9) {
    nine();
  } 
}

void loop() {


  digitalWrite(fff,HIGH);
  segdisp(random(0,9));
  delay(50);

  if (analogRead(sens) < 400) {
    for (int i = 0; i<10; i++) {
      segdisp(9-i);
      delay(1000);
      if (i == 8) {
        digitalWrite(fff,LOW);
        delay(50);
      }
    }
  }

}




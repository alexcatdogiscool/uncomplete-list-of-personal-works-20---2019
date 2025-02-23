const int ones = A0;
const int twos = A1;
const int fours = A2;
const int eights = A3;

int light = A4;


void setup() {
pinMode(ones,OUTPUT);
pinMode(twos,OUTPUT);
pinMode(fours,OUTPUT);
pinMode(eights,OUTPUT);
pinMode(light,INPUT);
}



void loop() {

int x = analogRead(light);  //read voltage from the voltage divider (with LDR)

if (x < 100) {
//display 0
digitalWrite(ones,LOW);
digitalWrite(twos,LOW);
digitalWrite(fours,LOW);
digitalWrite(eights,LOW);
delay (500);
}

else if (x >= 100 && x < 200) {
//display 1
digitalWrite(ones,HIGH);
digitalWrite(twos,LOW);
digitalWrite(fours,LOW);
digitalWrite(eights,LOW);
delay (500);
}

else if (x >= 200 && x < 300) {
//display 2
digitalWrite(ones,LOW);
digitalWrite(twos,HIGH);
digitalWrite(fours,LOW);
digitalWrite(eights,LOW);
delay (500);
}

else if (x >= 300 && x < 400) {
//display 3
digitalWrite(ones,HIGH);
digitalWrite(twos,HIGH);
digitalWrite(fours,LOW);
digitalWrite(eights,LOW);
delay (500);
}

else if (x >= 400 && x < 500) {
//display 4
digitalWrite(ones,LOW);
digitalWrite(twos,LOW);
digitalWrite(fours,HIGH);
digitalWrite(eights,LOW);
delay (500);
}

else if (x >= 500 && x < 600) {
//display 5
digitalWrite(ones,HIGH);
digitalWrite(twos,LOW);
digitalWrite(fours,HIGH);
digitalWrite(eights,LOW);
delay (500);
}

else if (x >= 600 && x < 700) {
//display 6
digitalWrite(ones,LOW);
digitalWrite(twos,HIGH);
digitalWrite(fours,HIGH);
digitalWrite(eights,LOW);
delay (500);
}

else if (x >= 700 && x < 800) {
//display 7
digitalWrite(ones,HIGH);
digitalWrite(twos,HIGH);
digitalWrite(fours,HIGH);
digitalWrite(eights,LOW);
delay (500);
}

else if (x >= 800 && x < 900) {
//display 8
digitalWrite(ones,LOW);
digitalWrite(twos,LOW);
digitalWrite(fours,LOW);
digitalWrite(eights,HIGH);
delay (500);
}

else if (x >= 900) {
//display 9
digitalWrite(ones,HIGH);
digitalWrite(twos,LOW);
digitalWrite(fours,LOW);
digitalWrite(eights,HIGH);
delay (500);
}

else {
}

delay (1);

}



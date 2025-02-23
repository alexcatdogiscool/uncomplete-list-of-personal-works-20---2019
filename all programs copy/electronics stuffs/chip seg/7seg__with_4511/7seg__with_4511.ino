const int ones = A0;
const int twos = A1;
const int fours = A2;
const int eights = A3;




void setup() {

pinMode(ones,OUTPUT);
pinMode(twos,OUTPUT);
pinMode(fours,OUTPUT);
pinMode(eights,OUTPUT);

}



void loop() {

//display 0
digitalWrite(ones,LOW);
digitalWrite(twos,LOW);
digitalWrite(fours,LOW);
digitalWrite(eights,LOW);
delay (500);

//display 1
digitalWrite(ones,HIGH);
digitalWrite(twos,LOW);
digitalWrite(fours,LOW);
digitalWrite(eights,LOW);
delay (500);

//display 2
digitalWrite(ones,LOW);
digitalWrite(twos,HIGH);
digitalWrite(fours,LOW);
digitalWrite(eights,LOW);
delay (500);

//display 3
digitalWrite(ones,HIGH);
digitalWrite(twos,HIGH);
digitalWrite(fours,LOW);
digitalWrite(eights,LOW);
delay (500);

//display 4
digitalWrite(ones,LOW);
digitalWrite(twos,LOW);
digitalWrite(fours,HIGH);
digitalWrite(eights,LOW);
delay (500);

//display 5
digitalWrite(ones,HIGH);
digitalWrite(twos,LOW);
digitalWrite(fours,HIGH);
digitalWrite(eights,LOW);
delay (500);

//display 6
digitalWrite(ones,LOW);
digitalWrite(twos,HIGH);
digitalWrite(fours,HIGH);
digitalWrite(eights,LOW);
delay (500);

//display 7
digitalWrite(ones,HIGH);
digitalWrite(twos,HIGH);
digitalWrite(fours,HIGH);
digitalWrite(eights,LOW);
delay (500);

//display 8
digitalWrite(ones,LOW);
digitalWrite(twos,LOW);
digitalWrite(fours,LOW);
digitalWrite(eights,HIGH);
delay (500);

//display 9
digitalWrite(ones,HIGH);
digitalWrite(twos,LOW);
digitalWrite(fours,LOW);
digitalWrite(eights,HIGH);
delay (500);

}



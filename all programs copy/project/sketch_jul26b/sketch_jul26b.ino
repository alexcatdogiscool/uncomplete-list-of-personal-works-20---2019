#include <LedControl.h>

int DIN1 = 2;
int CS1 =  3;
int CLK1 = 4;

int DIN2 = 5;
int CS2 =  6;
int CLK2 = 7;

int DIN3 = 8;
int CS3 =  9;
int CLK3 = 10;

int DIN4 = 11;
int CS4 =  12;
int CLK4 = 13;

int speaker = A7;

int imu = A3;


int xa = A0;
int ya = A1;
int button = A2;

float ballx = 0;
float bally = 0;
float xv = 0;
float yv = 0;

float avgx = 0;
float avgy = 0;


byte a[] = {0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000};
byte b[] = {0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000};
byte c[] = {0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000};
byte d[] = {0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000};


LedControl lc0 = LedControl(DIN1,CLK1,CS1,0);
LedControl lc1 = LedControl(DIN2,CLK2,CS2,0);
LedControl lc2 = LedControl(DIN3,CLK3,CS3,0);
LedControl lc3 = LedControl(DIN4,CLK4,CS4,0);


void draw(int x, int y) {//this function takes in an x and y var and diplays a dot on the corresponding location on the led matrix
  int dispNum = 0;
  if (x > 7) {
    dispNum += 1;
    x -= 8;
  }
  if (y > 7) {
    dispNum += 2;
    y -= 8;
  }

  if (dispNum == 0) {
    bitWrite(a[y],7-x,1);
    //return a;
  }

  if (dispNum == 1) {
    bitWrite(c[7-y],x,1);
    //return b;
  }

  if (dispNum == 2) {
    bitWrite(b[y],7-x,1);
    //return c;
  }

  if (dispNum == 3) {
    bitWrite(d[7-y],x,1);
    //return d;
  }
}

void printNum(int x, int y, int n) {//displays a number that you give to the function on the matrix(only 1 or 2 digits)
  if (n > 9){
    printNum(4,0,n-((int)(n/10))*10);
    n = (int)(n/10);
  }
  if (n == 0) {
    draw(x+0, y+0);
    draw(x+1, y+0);
    draw(x+2, y+0);
    draw(x+0, y+1);
    draw(x+0, y+2);
    draw(x+0, y+3);
    draw(x+0, y+4);
    draw(x+2, y+1);
    draw(x+2, y+2);
    draw(x+2, y+3);
    draw(x+2, y+4);
    draw(x+1, y+4);
  }
  if (n == 1) {
    draw(x+1, y+0);
    draw(x+1, y+1);
    draw(x+1, y+2);
    draw(x+1, y+3);
    draw(x+1, y+4);
    draw(x+0, y+0);
    draw(x+0, y+4);
    draw(x+2, y+4);
  }
  if (n == 2) {
    draw(x+0, y+0);
    draw(x+1, y+0);
    draw(x+2, y+0);
    draw(x+2, y+1);
    draw(x+0, y+2);
    draw(x+1, y+2);
    draw(x+2, y+2);
    draw(x+0, y+3);
    draw(x+0, y+4);
    draw(x+1, y+4);
    draw(x+2, y+4);
  }
  if (n == 3) {
    draw(x+0, y+0);
    draw(x+1, y+0);
    draw(x+2, y+0);
    draw(x+0, y+2);
    draw(x+1, y+2);
    draw(x+2, y+2);
    draw(x+0, y+4);
    draw(x+1, y+4);
    draw(x+2, y+4);
    draw(x+2, y+1);
    draw(x+2, y+3);
  }
  if (n == 4) {
    draw(x+0, y+0);
    draw(x+0, y+1);
    draw(x+0, y+2);
    draw(x+1, y+2);
    draw(x+2, y+2);
    draw(x+2, y+0);
    draw(x+2, y+1);
    draw(x+2, y+3);
    draw(x+2, y+4);
  }
  if (n == 5) {
    draw(x+0, y+0);
    draw(x+1, y+0);
    draw(x+2, y+0);
    draw(x+0, y+2);
    draw(x+1, y+2);
    draw(x+2, y+2);
    draw(x+0, y+4);
    draw(x+1, y+4);
    draw(x+2, y+4);
    draw(x+0, y+1);
    draw(x+2, y+3);
  }
  if (n == 6) {
    draw(x+0, y+0);
    draw(x+0, y+1);
    draw(x+0, y+2);
    draw(x+0, y+3);
    draw(x+0, y+4);
    draw(x+1, y+4);
    draw(x+2, y+4);
    draw(x+1, y+2);
    draw(x+2, y+2);
    draw(x+2, y+3);
    draw(x+1, y+0);
    draw(x+2, y+0);
  }
  if (n == 7) {
    draw(x+0, y+0);
    draw(x+1, y+0);
    draw(x+2, y+0);
    draw(x+2, y+1);
    draw(x+2, y+2);
    draw(x+2, y+3);
    draw(x+2, y+4);
  }
  if (n == 8) {
    draw(x+0, y+0);
    draw(x+1, y+0);
    draw(x+2, y+0);
    draw(x+0, y+2);
    draw(x+1, y+2);
    draw(x+2, y+2);
    draw(x+0, y+4);
    draw(x+1, y+4);
    draw(x+2, y+4);
    draw(x+0, y+1);
    draw(x+2, y+1);
    draw(x+0, y+3);
    draw(x+2, y+3);
  }
  if (n == 9) {
    draw(x+0, y+0);
    draw(x+1, y+0);
    draw(x+2, y+0);
    draw(x+0, y+2);
    draw(x+1, y+2);
    draw(x+2, y+2);
    draw(x+0, y+1);
    draw(x+2, y+1);
    draw(x+2, y+3);
    draw(x+2, y+4);
    draw(x+1, y+4);
    draw(x+0, y+4);   
  }
  
  
}

class hole {//the destination you need go to
  public:
  int x = (int)random(1,15);
  int y = (int)random(1,15);

  void drawHole() {
    draw(x, y-1);
    draw(x-1, y);
    draw(x+1, y);
    draw(x, y+1);
  }
};

class Dot {//the player
  public:
  float x = 8;
  float y = 8;
  void drawSelf() {
    draw((int)x, (int)y);
  }
};

void setup(){
 lc0.shutdown(0,false);       //The MAX72XX is in power-saving mode on startup
 lc0.setIntensity(0,15);      // Set the brightness to maximum value
 lc0.clearDisplay(0);         // and clear the display
 
 lc1.shutdown(0,false);       //The MAX72XX is in power-saving mode on startup
 lc1.setIntensity(0,15);      // Set the brightness to maximum value
 lc1.clearDisplay(0);         // and clear the display
 
 lc2.shutdown(0,false);       //The MAX72XX is in power-saving mode on startup
 lc2.setIntensity(0,15);      // Set the brightness to maximum value
 lc2.clearDisplay(0);         // and clear the display
 
 lc3.shutdown(0,false);       //The MAX72XX is in power-saving mode on startup
 lc3.setIntensity(0,15);      // Set the brightness to maximum value
 lc3.clearDisplay(0);         // and clear the display
 
 Serial.begin(9600);

  analogWrite(imu, 1023);

 
  for (int i=0; i<20; i++) {
    avgx += analogRead(xa)/20.f;
    avgy += analogRead(ya)/20.f;
  }  
}


Dot ball;
hole dest;



bool playing = true;

int score = 0;

int PreButt = 0;

void loop(){
  int butt = analogRead(button);
  if (butt - PreButt > 500){
    playing = !playing;
  }

  if (playing) {
    xv += (analogRead(xa) - avgx) / 1000.f;
    yv += (analogRead(ya) - avgy) / -1000.f;
  
    ball.x += xv;
    ball.y += yv;
  
    if ((int)ball.x == dest.x and (int)ball.y == dest.y) {
      score++;
      dest.x = random(1,14);
      dest.y = random(1,14);
      tone(speaker, 1200, 100);
    }
    if (ball.x > 16 or ball.x < 0 or ball.y > 16 or ball.y <0) {
      ball.x = 8;
      ball.y = 8;
      xv = 0;
      yv = 0;
      score = 0;
      tone(speaker, 200, 100);
    }
    clearScreens();
    dest.drawHole();
    ball.drawSelf();
    disp();
  }
  if (playing == false) {
    clearScreens();
    printNum(0,0,score);
    disp();
  }
  
  
  PreButt = butt;
}

void clearScreens() {//clears the screen of everything that has been drawn
  for (int i = 0; i < 8; i ++) {
    a[i] = 0b00000000;
    b[i] = 0b00000000;
    c[i] = 0b00000000;
    d[i] = 0b00000000;
  }
}



void disp() {//actually gives the screen to the matrix
  printByte(a,0);
  printByte(b,1);
  printByte(c,2);
  printByte(d,3);
}



void printByte(byte character [], int num)//actually puts a dot on the screen variable matrix thing
{
  int i = 0;
  for(i=0;i<8;i++)
  {
    if (num == 0){
      lc0.setRow(0,i,character[i]);
    }

    if (num == 1){
      lc1.setRow(0,i,character[i]);
    }

    if (num == 2){
      lc2.setRow(0,i,character[i]);
    }

    if (num == 3){
      lc3.setRow(0,i,character[i]);
    }
  }
}

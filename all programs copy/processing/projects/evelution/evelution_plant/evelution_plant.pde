float rwidth = 55;
float rheight = 100;
float sarea = (rwidth * 2) + (rheight * 2);
float volume = rwidth * rheight;
float fwidth = 0;
float fheight = 0;
float fwidth2 = 0;
float fheight2 = 0;
float error = sarea / volume;
int count = 0;
float cbest = 0;

void setup(){
  size(1500,1000);
  background(135,206,235);
  
  
}

void draw(){
  background(135,206,235);
  rect(750,500,rwidth, rheight);
  
  if (count < 10) {
    
    rwidth = fwidth2 + random(-0,5);
    rheight = fheight2 + random(-0,5);
    
    sarea = (rwidth * 2) + (rheight * 2);
    volume = rwidth * rheight;
    
    error = sarea - volume;
    
    if (error > cbest) {
      cbest = error;
      print(cbest);
      print("n");
      fwidth = rwidth;
      fheight = rheight;
    }
    
    
  
  
  
    count = count + 1;
  }
  fwidth2 = fwidth;
  fheight2 = fheight;
  count = 0;
}

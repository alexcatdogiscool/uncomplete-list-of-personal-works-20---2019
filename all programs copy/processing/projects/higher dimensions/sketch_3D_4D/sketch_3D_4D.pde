float w = 0.5;
float w2 = 0.5;
float size = 560;
int gap = 77;

void setup() {
  size(2736,1824,P3D);
  background(0);
  lights();
  
}

void draw() {
  background(0);
  
  pushMatrix();
  translate(130, height/2, 0);
  rotateY(1.25);
  rotateX(-0.4);
  noStroke();
  box(100);
  popMatrix();

  pushMatrix();
  translate(300+500, 300, -200);
  noFill();
  stroke(255);
  sphere(280);
  popMatrix();
  pushMatrix();
  translate(300+500, 300, -200);
  noFill();
  stroke(255);
  sphere(280*w);
  popMatrix();
  //end
  
  pushMatrix();
  translate(860+500, 300, -200);
  noFill();
  stroke(255);
  sphere(280);
  popMatrix();
  pushMatrix();
  translate(860+500, 300, -200);
  noFill();
  stroke(255);
  sphere(280*w);
  popMatrix();
  //end
  
  pushMatrix();
  translate(300+500, 860, -200);
  noFill();
  stroke(255);
  sphere(280);
  popMatrix();
  pushMatrix();
  translate(300+500, 860, -200);
  noFill();
  stroke(255);
  sphere(280*w);
  popMatrix();
  //end
  
  pushMatrix();
  translate(860+500, 860, -200);
  noFill();
  stroke(255);
  sphere(280);
  popMatrix();
  pushMatrix();
  translate(860+500, 860, -200);
  noFill();
  stroke(255);
  sphere(280*w);
  popMatrix();
  //end
  
  
  
  pushMatrix();
  translate(300+500, 300, 360);
  noFill();
  stroke(255);
  sphere(280);
  popMatrix();
  pushMatrix();
  translate(300+500, 300, 360);
  noFill();
  stroke(255);
  sphere(280*w);
  popMatrix();
  //end
  
  pushMatrix();
  translate(860+500, 300, 360);
  noFill();
  stroke(255);
  sphere(280);
  popMatrix();
  pushMatrix();
  translate(860+500, 300, 360);
  noFill();
  stroke(255);
  sphere(280*w);
  popMatrix();
  //end
  
  pushMatrix();
  translate(300+500, 860, 360);
  noFill();
  stroke(255);
  sphere(280);
  popMatrix();
  pushMatrix();
  translate(300+500, 860, 360);
  noFill();
  stroke(255);
  sphere(280*w);
  popMatrix();
  //end
  
  pushMatrix();
  translate(860+500, 860, 360);
  noFill();
  stroke(255);
  sphere(280);
  popMatrix();
  pushMatrix();
  translate(860+500, 860, 360);
  noFill();
  stroke(255);
  sphere(280*w);
  popMatrix();
  //end
  
  
  
  //inner sphere
  fill(0, 200, 0, 200);
  pushMatrix();
  translate(580+500, 580, 80);
  noFill();
  stroke(255);
  sphere(size);
  popMatrix();
  pushMatrix();
  translate(580+500, 580, 80);
  noFill();
  stroke(255);
  sphere(size*w2);
  popMatrix();
  
  if (mousePressed) {
    size = size+1;
  }
  print(size);
  print(gap);
  
  
//  w = w*0.99;
//  w2 = w2*0.99;
}

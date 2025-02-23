// Declare and construct two objects (h1, h2) from the class HLine 
 

int swidth = 800;
int sheight = 800;
int num_of_bugs = 10;
//bug initial parameters
//bug b;
//bug b = new bug();
Bug[] bugs; 
Food[] food;

void setup() 
{
  size(800, 800);
  frameRate(30);
  bugs = new Bug[num_of_bugs];
  food = new Food[0];
  for (int x = 0; x < num_of_bugs; x++) {
      bugs[x] = new Bug();
    }
}

void draw() { 
  background(204);
//  bugs[1].evolve();
//  bugs[1].display();
  for (Bug b : bugs) {
    b.evolve();    
    b.display(); 
    if (b.alive = false) {food = append(food, new Food(b.xpos, b.ypos));}
  }
  for (Food f : food) {
    f.display();     
  }
  printArray(food);
  }
  
class Food {
   int xpos, ypos;
   
   Food(int x, int y) {
     xpos = x;
     ypos = y;
   }
   
   void display() {
      fill(0,255,0);
      rect(xpos, ypos ,30, 30);  
   }
   
}
 
class Bug { 
  int xpos, ypos;
  float speed, dir; 
  float health;
  boolean alive;
  
   
  Bug() {
    health = 50;
    alive = true;
    xpos = int(random(0, swidth));
    ypos = int(random(0, sheight));
    speed = random(10, 25);
    dir = random(2 * 3.14);   
  }
  
  void display() {
    if (alive) {
      dir = dir + random(-0.1, 0.1);
      xpos = xpos + int(speed *  sin(dir)); 
      ypos = ypos +int(speed * cos(dir));
      if (xpos > swidth) {xpos = 0;}
      if (ypos > sheight) {ypos = 0;}
      if (xpos < 0) {xpos = swidth;}
      if (ypos < 0) {ypos = sheight;}
 
      health = health - random(0.1);
      if (health < 0) {alive = false;}
      fill(255,0,0);
      rect(xpos, ypos ,health, health);
 //     if (alive == false) {food = append(food,new Food(xpos, ypos));} 
 //     food = append(food,new Food(xpos, ypos));
    }
  }
  
  void evolve() {
    if (alive) {
//      speed = random(0,5);
//      xpos = xpos + random (-speed, speed);
//      ypos = ypos + random (-speed, speed);
    }
  }
  
} 

// Declare and construct two objects (h1, h2) from the class HLine 
 

int swidth = 1400;
int sheight = 1200;
int num_of_bugs = 10;
//bug initial parameters
ArrayList<Bug> bugs = new ArrayList<Bug>();
ArrayList<Food> food = new ArrayList<Food>();

void setup() 
{
  size(1400, 1200);
  frameRate(30);
  for (int x = 0; x < num_of_bugs; x++) {
      bugs.add(new Bug(int(random(0,swidth)), int(random(0,sheight))));
    }
   for (int x = 0; x < 10; x++) {
      food.add(new Food(100,100));
    } 
    
}

void draw() { 
  background(204);
  for (Bug b : bugs) {
    b.evolve();
    b.eat(); 
    b.display(); 
   if (b.alive == false) {food.add(new Food(b.xpos, b.ypos));   }
  }
  
 // for (Bug b : bugs) {
 //   if (b.health > 100) {
 //     bugs.add(new Bug(b.xpos,b.ypos));
 //     bugs.add(new Bug(b.xpos,b.ypos));     
 //     b.alive = false;
 //     }
//  }
   
   // Remove dead bugs from array list
   for (int i = bugs.size() - 1; i >= 0; i--) {
      Bug b = bugs.get(i);
      if (b.alive == false) {
    bugs.remove(i);
  }
  }
  
  if (random(0,100) < 5) {food.add(new Food(int(random(0,swidth)), int(random(0,sheight))));}
  
  for (Food f : food) {
    f.display();     
  }
  
//  print(bugs.size()); 
  }
  
class Food {
   int xpos, ypos;
   int energy;
   boolean eaten;
   
   Food(int x, int y) {
     energy = 60;
     eaten = false;
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
  int size;
  
   
  Bug(int x, int y) {
    size = int(random(10,60));
    health = random(30,80);
    alive = true;
    xpos = x;
    ypos = y;
    speed = random(10, 25);
    dir = random(2 * 3.14);   
  }
  
  void eat() {
    for (Food f : food) {
      if ((sq(f.xpos - xpos) < 120) & (sq(f.ypos - ypos) < 120)) {
        if (f.eaten == false) {
          health = health + f.energy;
          f.eaten = true;}
        }
    }
      // Remove eaten food from array list
   for (int i = food.size() - 1; i >= 0; i--) {
      Food f = food.get(i);
      if (f.eaten == true) {food.remove(i);}     
      }
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
 
      health = health - (0.0001 * (speed * size));
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


int sw = 1200;
int sh = 800;

void settings(){
  size(sw,sh);
}

void setup(){
}





int sum(int a, int b){
  return a+b;
}

public class box{
  int x = 100;
  int y = 100;
  
  int bw = 50;
  int bh = 50;
  
  int[] sel = new int[2];
  
  void drawBox(int x, int y){
    rect(x,y,50,50);
  }
  
  int[] updateSel(int x, int y, int bw, int bh, int[] sel, boolean pre){
    if (mouseX > x & mouseX < x+bw & mouseY > y & mouseY < y+bh){
      if (mousePressed == true & pre == false){
        sel[0] = mouseX - x;
        sel[1] = mouseY - y;
      }
    }
    return sel;
  }
  
  int[] moveBox(int x, int y, int bw, int bh, int[] sel){
    if (mouseX > x & mouseX < x+bw & mouseY > y & mouseY < y+bh){
      if(mousePressed == true){
        int[] p = new int[2];
        p[0] = mouseX - sel[0];
        p[1] = mouseY - sel[1];
        return p;
      }
    }
    int[] p = new int[2];
    p[0] = x;
    p[1] = y;
    return p;
  }
}

boxes = new ArrayList<box>();
for (int i=0; i<10; i = i + 1){
  box b;
  boxes[i] = b;
}




box b = new box();


boolean mpre;
void draw(){
  background(0);
  
  b.sel = b.updateSel(b.x,b.y, b.bw,b.bh, b.sel, mpre);
  int[] p = b.moveBox(b.x,b.y, b.bw,b.bh, b.sel);
  b.x = p[0];
  b.y = p[1];
  b.drawBox(b.x, b.y);
  
  println(b.sel[0], b.sel[1]);
  
  
  
  
  mpre = mousePressed;
}

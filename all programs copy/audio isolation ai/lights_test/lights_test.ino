int led = 5;
int reset = 3;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(led, OUTPUT);
}

void softReset(){
asm volatile ("  jmp 0");
}

// the loop function runs over and over again forever
void loop() {
//  digitalWrite(reset, LOW);
  digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(10000);
  digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  delay(10000);
  softReset();

}

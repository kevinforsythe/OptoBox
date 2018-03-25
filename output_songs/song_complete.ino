// reset pin = hardwired through reset button to ground
// test button = hardwired to momentarily connect transistor gate and VCC
// manual overide switch = latches transistor gate to VCC, also connects to pin0 for interrupt
//
// pin0 = wired to manual override switch, for interrupt signal (INT2), HIGH when manually overide is on (normally pulled LOW)
// pin2 = LED Yellow, indicates program is ready to run
// pin3 = LED Green, indicates program running
// pin4 = LED Red, indicates program finished
// pin9 = BUTTON, starts the loaded program (normally held HIGH)
// pin10 = gate for transistor driven LEDs
//

const int switchManualOverride = 0;
const int LEDYellow = 2;
const int LEDGreen = 3;
const int LEDRed = 4;
const int buttonStart = 9;
const int LEDBlue = 10;

int buttonStartState = 1;

void setup() {

  digitalWrite(switchManualOverride, LOW);
  attachInterrupt(INT2, manualoverride, HIGH);

  pinMode(LEDYellow, OUTPUT);
  pinMode(LEDGreen, OUTPUT);
  pinMode(LEDRed, OUTPUT);
  pinMode(buttonStart, INPUT);
  digitalWrite(buttonStart, HIGH);
  pinMode(LEDBlue, OUTPUT);
}

void loop() {
  digitalWrite(LEDYellow, HIGH);  // turn on Yellow LED when ready to start program
  while (buttonStartState == 1) {
    buttonStartState = digitalRead(buttonStart);
  }
  digitalWrite(LEDYellow, LOW); // turn off Yellow LED when program starts

  digitalWrite(LEDGreen, HIGH);  // turn on Green LED while programm running
digitalWrite(LEDBlue, HIGH);
delay(250);
digitalWrite(LEDBlue, HIGH);
delay(250);
digitalWrite(LEDBlue, LOW);
delay(250);
digitalWrite(LEDBlue, LOW);
delay(250);
digitalWrite(LEDBlue, HIGH);
delay(250);
digitalWrite(LEDBlue, HIGH);
delay(250);
digitalWrite(LEDBlue, LOW);
delay(250);
digitalWrite(LEDBlue, LOW);
delay(250);
digitalWrite(LEDBlue, HIGH);
delay(250);
digitalWrite(LEDBlue, HIGH);
delay(250);
digitalWrite(LEDBlue, LOW);
delay(250);
digitalWrite(LEDBlue, LOW);
delay(250);
digitalWrite(LEDBlue, HIGH);
delay(250);
digitalWrite(LEDBlue, HIGH);
delay(250);
digitalWrite(LEDBlue, LOW);
delay(250);
digitalWrite(LEDBlue, LOW);
delay(250);

  digitalWrite(LEDGreen, LOW);   // turn off Green LED after program finishes
  digitalWrite(LEDRed, HIGH);  // turn on Red LED after program finishes and
                               // enter indefinite while loop doing nothing
  while (1) {
  }
}

void manualoverride() {
  while (1) {
      digitalWrite(LEDYellow, HIGH);
      digitalWrite(LEDGreen, HIGH);
      digitalWrite(LEDRed, HIGH);
  }
}

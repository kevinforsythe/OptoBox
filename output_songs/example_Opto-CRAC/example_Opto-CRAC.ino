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


//  manual override switch interrupt:
//  if the manual override switch has been engaged, then all three LED
//  indicators (yellow+green+red) will be lit and latched in the ON position
//  and the song will be stuck in an infinite loop (you'll need to reset the box
//  if you want to run the loaded song from the beginning)
void manualoverride() {
  while (1) {
      digitalWrite(LEDYellow, HIGH);
      digitalWrite(LEDGreen, HIGH);
      digitalWrite(LEDRed, HIGH);
  }
}


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

// song intro template ends here, and
// Opto-CRAC song starts here:
//
digitalWrite(LEDBlue, HIGH);
delay(30000);
digitalWrite(LEDBlue, LOW);
delay(120000);
digitalWrite(LEDBlue, HIGH);
delay(30000);
digitalWrite(LEDBlue, LOW);
delay(120000);
digitalWrite(LEDBlue, HIGH);
delay(30000);
digitalWrite(LEDBlue, LOW);
delay(120000);

//  Opto-CRAC song ends here, and
//  song coda starts here:
//
  digitalWrite(LEDBlue, LOW);   // turn off the Blue LEDs in case they were
                                // on during the last beat of the song
  digitalWrite(LEDGreen, LOW);   // turn off Green LED after program finishes
  digitalWrite(LEDRed, HIGH);  // turn on Red LED after program finishes and
                               // enter indefinite while loop doing nothing
  while (1) {
  }
}

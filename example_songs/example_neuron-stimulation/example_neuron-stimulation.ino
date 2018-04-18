// reset pin = hardwired through reset button to ground
// test button = hardwired to momentarily connect transistor gate and VCC
// manual overide switch = latches transistor gate to VCC, also connects to pin0 for interrupt
//
// pin0 = wired to manual override switch, for interrupt signal (INT2), HIGH when manually overide is on (normally pulled LOW)
// pin2 = LED Yellow, indicates program is ready to run
// pin3 = LED Green, indicates program running
// pin4 = LED Red, indicates program finishedOpto-CRAC_3cyles
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
  // example_neuron-stimulation song starts here:

  // the 'on-off' motiff will run for 12 cycles
  for (int i=0; i < 12; i++) {
    // the 'on' phase will blink at 20Hz, period = 50msec (25msec on, 25msec off)
    // and will be on for 30s, or 600 cycles (600*50msec=30,000msec)
    for (int j=0; j < 600; j++) {
      digitalWrite(LEDBlue, HIGH);
      delay(25);
      digitalWrite(LEDBlue, LOW);
      delay(25);
    }
    // the 'off' phase will last 2 minutes, or 120,000msec
    delay(120000);
  }

//  example_neuron-stimulation song ends here, and
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

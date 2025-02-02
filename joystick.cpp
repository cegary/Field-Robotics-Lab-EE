const int y = A0;
const int x = A1;
const int click = 13;

void setup() {
  Serial.begin(9600);
  pinMode(click, INPUT_PULLUP);  // Enable internal pull-up for button


}

void loop() {
  int x = analogRead(x);     // 0-1023
  int y = analogRead(y);     // 0-1023
  bool btn = !digitalRead(click); // default: 0

  Serial.println("x:"+x);
  Serial.println("y:"+y);
  Serial.println("btn:"+btn);
  delay(30);
}
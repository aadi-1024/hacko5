#include <Servo.h>

Servo servo1;

void setup() {
  servo1.attach(7);
  servo1.write(60);
}

void loop() {
  for (int i = 180; i > 0; i--) {
    servo1.write(i);
    delay(10);
  }
  for (int i = 0; i < 180; i++) {
    servo1.write(i);
    delay(10);
  }
}
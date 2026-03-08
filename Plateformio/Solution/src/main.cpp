#include <Arduino.h>

int X = 2;
int Y = 3;

int A = 4;
int B = 5;
int C = 6;
int D = 7;

void setup()
{
    pinMode(X, INPUT_PULLUP);
    pinMode(Y, INPUT_PULLUP);

    pinMode(A, OUTPUT);
    pinMode(B, OUTPUT);
    pinMode(C, OUTPUT);
    pinMode(D, OUTPUT);
}

void loop()
{
    int x = digitalRead(X);
    int y = digitalRead(Y);

    int z = x ^ y;

    digitalWrite(A, z);
    digitalWrite(B, LOW);
    digitalWrite(C, LOW);
    digitalWrite(D, LOW);

    delay(100);
}

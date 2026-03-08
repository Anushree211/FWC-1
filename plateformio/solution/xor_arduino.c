#include <Arduino.h>

int X = 10;
int Y = 11;

int A = 2;
int B = 3;
int C = 4;
int D = 5;

void setup()
{
    pinMode(X, INPUT);
    pinMode(Y, INPUT);

    pinMode(A, OUTPUT);
    pinMode(B, OUTPUT);
    pinMode(C, OUTPUT);
    pinMode(D, OUTPUT);
}

void loop()
{
    int x = digitalRead(X);
    int y = digitalRead(Y);

    int Z = x ^ y;

    if(Z == 0)
    {
        digitalWrite(A, LOW);
        digitalWrite(B, LOW);
        digitalWrite(C, LOW);
        digitalWrite(D, LOW);
    }
    else
    {
        digitalWrite(A, HIGH);
        digitalWrite(B, LOW);
        digitalWrite(C, LOW);
        digitalWrite(D, LOW);
    }
}

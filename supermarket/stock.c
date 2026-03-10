#include <stdio.h>
#include "stock.h"

int stock = 50;

void addstock(int qty)
{
    stock = stock + qty;
    printf("Stock added successfully\n");
}

void deletestock(int qty)
{
    stock = stock - qty;
    printf("Stock removed successfully\n");
}

int getstock()
{
    return stock;
}

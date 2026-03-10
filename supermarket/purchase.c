#include <stdio.h>
#include "stock.h"

#define MAX_STOCK 100

void purchase(int qty)
{
    if(getstock() + qty <= MAX_STOCK)
    {
        addstock(qty);
        printf("Purchase successful\n");
    }
    else
    {
        printf("Not enough space in stock room\n");
    }
}

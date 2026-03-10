#include <stdio.h>
#include "stock.h"

void sell(int qty);
void purchase(int qty);

int main()
{
    int choice, qty;

    while(1)
    {
        printf("\n---- SuperMarket Menu ----\n");
        printf("1. Check Available Stock\n");
        printf("2. Purchase Items\n");
        printf("3. Sell Items\n");
        printf("4. Quit\n");

        printf("Enter choice: ");
        scanf("%d",&choice);

        switch(choice)
        {
            case 1:
                printf("Available Stock: %d\n", getstock());
                break;

            case 2:
                printf("Enter quantity: ");
                scanf("%d",&qty);
                purchase(qty);
                break;

            case 3:
                printf("Enter quantity: ");
                scanf("%d",&qty);
                sell(qty);
                break;

            case 4:
                return 0;

            default:
                printf("Invalid choice\n");
        }
    }
}

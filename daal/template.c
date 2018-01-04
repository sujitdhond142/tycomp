/*
    This is template for your program including menu 
    and switch case statement.
*/

#include<stdio.h>
#include<stdlib.h>

// function declaration


// main function
void main(){
    int arr[20],n=0,choice;
    char ch;
    do{
        //program menu
        printf("\nProgram Menu");
        printf("\n1.Accpet");
        printf("\n2.Display");
        printf("\n3.");
        printf("\n0.Exit");
        printf("\nEnter your choice : ");
        scanf("%d",&choice);
        switch(choice){
            case 1:
                /* Accept */
                break;
            case 2:
                /* Display */
                break;
            case 3:
                /* Other functions */
                break;
            case 0:
                /* Exit */
                exit(0);
            default:
                printf("\nInvalid choice\n");
                break;
        }
        printf("Do you want to continue(y/n) ");
        scanf("%s",&ch);
    }while(ch=='y'||ch=='Y');
    return;
}

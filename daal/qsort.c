/*
    Aim: Program to perform quick sort on array.
*/

#include<stdio.h>
#include<stdlib.h>

// function declaration
void accept(int [],int);
void display(int [],int);
void qcksort(int [],int,int);

// main function
void main(){
    int arr[20],n=0,choice;
    char ch;
    do{
        //program menu
        printf("\nProgram Menu");
        printf("\n1.Accpet");
        printf("\n2.Display");
        printf("\n3.Quick Sort");
        printf("\n0.Exit");
        printf("\nEnter your choice : ");
        scanf("%d",&choice);
        switch(choice){
            case 1:
                /* Accept array */
                printf("Enter no of elements of array : ");
                scanf("%d",&n);
                accept(arr,n);
                break;
            case 2:
                /* Display array */
                printf("Array is : ");
                display(arr,n);
                break;
            case 3:
                /* Perform Quick-sort on array */
                qcksort(arr,0,n-1);
                printf("Sorted array \n");
                display(arr,n);
                break;
            case 0:
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
void accept(int a[20],int n){
    int i=0;
    printf("Enter array ");
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
}
void display(int a[20],int n){
    int i=0;
    for(i=0;i<n;i++){
        printf("%d ",a[i]);
    }
    printf("\n");
}

/*
    quicksort function definition
    parameters: array,lowest,highest index
*/
void qcksort(int a[20],int low,int high){
    int i=low,j=high,tmp,pivot=a[low];
    if(low<high){
        while(i<j){
            while(a[i]<=pivot)
                i++;
            while(a[j]>pivot)
                j--;
            if(i<j){
                tmp=a[i];
                a[i]=a[j];
                a[j]=tmp;
            }
        }
        tmp=a[low];
        a[low]=a[j];
        a[j]=tmp;

        qcksort(a,low,j-1);     //calling function recursively
        qcksort(a,j+1,high);    //calling function recursively
    }
}

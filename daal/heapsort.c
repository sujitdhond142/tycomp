/*
    Aim: Program to perform heap sort on array.
*/

#include<stdio.h>
#include<stdlib.h>

// function declaration
void accept(int [],int);
void display(int [],int);
void heapsort(int [],int );
void heapify(int [],int,int);

// main function
void main(){
    int arr[20],n=0,choice;
    char ch;
    do{
        //program menu
        printf("\nProgram Menu");
        printf("\n1.Accpet");
        printf("\n2.Display");
        printf("\n3.Heap sort");
        printf("\n0.Exit");
        printf("\nEnter your choice : ");
        scanf("%d",&choice);
        switch(choice){
            case 1:
                /* Accept */
                printf("Enter no of elements of array : ");
                scanf("%d",&n);
                accept(arr,n);
                break;
            case 2:
                /* Display */
                printf("Array is : ");
                display(arr,n);
                break;
            case 3:
                /* Heap sort */
                heapsort(arr,n);
                printf("Sorted array\n");
                display(arr,n);
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

/* Heapsort will sort the array */
void heapsort(int a[20],int n){
    int i,temp;
    for(i=n/2-1;i>=0;i--){
        heapify(a,n,i);
    }
    for(i=n-1;i>=0;i--){
        temp=a[0];
        a[0]=a[i];
        a[i]=temp;
        heapify(a,i,0);
    }
}

/*
    Heapify will arrange the array elements 
    in correct heap order 
*/
void heapify(int a[20],int n,int i){
    int temp;
    int largest=i;
    int l=2*i+1;
    int r=2*i+2;

    if(l<n && a[l]>a[largest]){
        largest=l;
    }
    if(r<n && a[r]>a[largest]){
        largest=r;
    }
    if(largest!=i){
        temp=a[i];
        a[i]=a[largest];
        a[largest]=temp;
        heapify(a,n,largest);
    }
}
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

void myStaticFunction(void) {
    static int myStaticArray[543210];
}

void myHeapFunction(void) {
    int heap = 4321424;
    int *myHeapArray = (int *)calloc(heap, sizeof(int));
}

void myStackFunction(void) {
    int myStackArray[789456];
}

int main(void){
   int i;
   int length = 100001;
   double amountOfTime;
   clock_t pointA, pointB;
   pointA = clock();
   for (i = 0; i < length; i++){
       myStaticFunction();
   }
   pointB = clock();
   amountOfTime = ((double) (pointB - pointA)) / CLOCKS_PER_SEC;
   printf("myStaticFunction: %f seconds \n", amountOfTime); 
   pointA = clock();
   for (i = 0; i < length; i++){
       myHeapFunction();
   }
   pointB = clock();
   amountOfTime = ((double) (pointB - pointA)) / CLOCKS_PER_SEC;
   printf("myHeapFunction: %f seconds \n", amountOfTime);
   pointA = clock();
   for (i = 0; i < length; i++){
       myStackFunction();
   }
   pointB = clock();
   amountOfTime = ((double) ((pointB - pointA)) / CLOCKS_PER_SEC);
   printf("myStackFunction: %f seconds \n", amountOfTime); 
}

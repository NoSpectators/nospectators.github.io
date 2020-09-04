#include <stdio.h>
#define MAX 10

void bubbleSort(int list[]) {
   int temp;
   int i,j;
	
   for(i = 0; i < MAX-1; i++) { 
      for(j = 0; j < MAX-1-i; j++) {  			
         if(list[j] > list[j+1]) {
            temp = list[j];
            list[j] = list[j+1];
            list[j+1] = temp;                   
         }			
      }
   }	
}

main() {
   int list[MAX] = {1,81,4,6,-1,34,5,2,7,9};
   bubbleSort(list);
   int i =0;
   for(i = 0; i < MAX; i++){
      printf("%d ",list[i]);
   }
   printf("\n");      
}

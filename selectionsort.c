#include <stdio.h>

void selectionSort(int arr[], int numbersSize){
	int n = numbersSize;
	int x,y;
	for(x=0; x<n; x++)	{

		int index_of_min = x;
		
		for(y=x; y<n; y++){
			if(arr[index_of_min]>arr[y]){
				index_of_min = y;
			}
		}
		int temp = arr[x];
		arr[x] = arr[index_of_min];
		arr[index_of_min] = temp;
	}
	return;
}

void main(){
	int numbers[] = { 10, 2, 78, 4, 45, 32, 7, 11 };
	const int NUMBERS_SIZE = 8;
	int i = 0;

	printf("UNSORTED: ");
	for (i = 0; i < NUMBERS_SIZE; ++i) {
	  printf("%i ", numbers[i]);
	}
	printf("\n");

	selectionSort(numbers, NUMBERS_SIZE);
	
	printf("SORTED: ");
	for (i = 0; i < NUMBERS_SIZE; ++i) {
	  printf("%i ", numbers[i]);
	}
	printf("\n");

	return;

}
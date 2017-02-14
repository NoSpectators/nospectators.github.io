public class BubbleSort {
    
        public static void main(String[] args) {
               
                int intArray[] = {5,90,35,45,150,3};                 
                
                bubbleSort(intArray);                            
                
                for(int i=0; i < intArray.length; i++){
                        System.out.print(intArray[i] + " ");
                }
                System.out.println();

        } 
        public static void bubbleSort(int[] intArray) {               
                int n = intArray.length;
                int temp = 0;               
                for(int i=0; i < n; i++){
                        for(int j=1; j < (n-i); j++){                               
                                if(intArray[j-1] > intArray[j]){
                                        //swap the elements!
                                        temp = intArray[j-1];
                                        intArray[j-1] = intArray[j];
                                        intArray[j] = temp;
                                }
                               
                        }
                }


        }
}
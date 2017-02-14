public class insertionSort {  
    public static void insertionSort(int[] a){  
        for (int i = 0; i < a.length - 1; i++) {  
            int temp = a[i];
            int j;  
            for (j = i - 1; j >= 0 && temp < a[j]; j--){  
                a[j+1] = a[j]; 
            }
            a[j+1] = temp;              
        }  
    }  
       
    public static void main(String a[]) {  
        int[] arr1 = {9,14,3,2,43,11,58,22};  
        System.out.println("Before Insertion Sort");  
        for(int i:arr1){  
            System.out.print(i+" ");  
        }  
        System.out.println();  
          
        insertionSort(arr1);//sorting array using selection sort  
         
        System.out.println("After Insertion Sort");  
        for(int i:arr1){  
            System.out.print(i+" ");  
        }  
        System.out.println();
    }  
}  
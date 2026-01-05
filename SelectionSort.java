import java.util.Arrays;

public class SelectionSort {
      



      public static int[] selectionSort(int[] dataset){

            for(int i = 0; i < dataset.length - i; i++){

                  int target = dataset[i];
                  int targetIndex = 0;
                  if(dataset[i] <= target){
                        target = dataset[i];
                        targetIndex = i;
                  }

                  System.out.printf("smallest value is %d in turn %d\n", target, i);

                  int temp = dataset[i];
                  dataset[i] = dataset[targetIndex];
                  dataset[targetIndex] = temp;
            }
            System.out.printf("smallest value is %d in turn %d\n", target, i);
            
            return dataset;
      }
      public static void main (String[] args){


            int [] example = {47, 15, 88, 23, 9, 62, 34, 51, 12, 76};
            System.out.println(Arrays.toString(example));
            String printArray = Arrays.toString(selectionSort(example));
            System.out.println(printArray);

      }
}

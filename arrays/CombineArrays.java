/**
 * Given 2 integer arrays sorted in ascending order, return a
 *  different array containing all the integers in this array, sorted in 
 *  ascending order.
 **/

import java.util.Arrays;

public class CombineArrays {
    public static void main(String[] args) {
        int[] arr1 = new int[]{};
        int[] arr2 = new int[]{101, 102, 103, 104, 105, 106};

        System.out.println("Combining " + Arrays.toString(arr1) + " and " 
            + Arrays.toString(arr2));
        System.out.println("Combined array: " 
            + Arrays.toString(combineArrays(arr1, arr2)));

        int[] arr3 = new int[]{100, 101, 200, 300};
        System.out.println("Combining " + Arrays.toString(arr2) + " and " 
            + Arrays.toString(arr3));
        System.out.println("Combined array: " 
            + Arrays.toString(combineArrays(arr2, arr3)));
    }

    public static int[] combineArrays(int[] arr1, int[] arr2) {
        // If one of the arrays is empty, then just return the other array
        if (arr2.length == 0)
            return arr1;
        else if (arr1.length == 0)
            return arr2;

        // We are going to keep 2 seperate counters and step through each
        // array roughly in tandem

        // Define combined array
        int[] arr3 = new int[arr1.length + arr2.length];

        int i = 0; // Counter for first array
        int j = 0; // Counter for second array

        // We using the index for the combined array as our loop condition
        // / loop control
        for (int k = 0; k < arr3.length; k++) {
            // If both arrays still need to be added, we must compare
            // their values. We do the comparisions as noted below:
            // If the value from the first array is smaller than the
            // value from the second array, we add it to the combined
            // array and increment the counter for the first array
            // If the value for the second array is smaller, we do the
            // same but in reverse. If the values are tied we arbitrarily
            // use the value from the first array.
            if (i < arr1.length && j < arr2.length) {
                if (arr1[i] < arr2[j]) {
                    arr3[k] = arr1[i];
                    i++;
                } else if (arr2[j] < arr1[i]) {
                    arr3[k] = arr2[j];
                    j++;
                } else if (arr1[i] == arr2[j]) {
                    arr3[k] = arr1[i];
                    i++;
                }
            }

            // Other wise, there is no need to do comparisons and we can just
            // toss the values from the array which still has elements into
            // the third array
            else if (i < arr1.length) { // First array still has items
                arr3[k] = arr1[i];
                i++;   
            } else if (j < arr2.length) {// If we get here, this is guranteed to be true but this makes it explicitly clear
                arr3[k] = arr2[j];
                j++;
            }
        }

        return arr3;
    }
}

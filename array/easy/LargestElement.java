package array.easy;
//https://www.geeksforgeeks.org/problems/largest-element-in-array4009/0/
public class LargestElement {
    public static int largest(int[] arr) {
        // code here
        int max = 0;

        for (int n:arr){
            if (n > max){
                max = n;
            }
        }
        return max;
    }
}

package array.easy;

public class SecondLargest {
    public int getSecondLargest(int[] arr) {
        int max = Integer.MIN_VALUE;
        int second_max = Integer.MIN_VALUE;

        for (int n : arr) {
            if (n > max) {
                second_max = max;
                max = n;
            } else if (n > second_max && n < max) {
                second_max = n;
            }
        }

        return second_max == Integer.MIN_VALUE ? -1 : second_max;
    }
}

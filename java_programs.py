code_string_palindrome = '''
public class Palindrome_String{
    public static void main(String[] args) {
        
        String s = "xqxl";
        s.toLowerCase();
        System.out.println(is_Palindrome(s));
        }

        static boolean is_Palindrome(String s)
        {
            if(s.length() == 0 || s == null)
            {
                return true;
            }
            for(int i = 0; i < s.length(); i++)
            {
                char start = s.charAt(i);
                char end = s.charAt(s.length()-1 - i);

                if(start == end)
                {
                    return true;
                }
            }
            return false;
    }
}'''

code_reverse_string = '''public class Reverse_string {
    public static void main (String[] args) {
       
        String str= "Geeks for skeeg", nstr="";
        char ch;
    
      System.out.print("Original word: ");
      System.out.println("Geeks"); //Example word
       
      for (int i=0; i<str.length(); i++)
      {
        ch= str.charAt(i); //extracts each character
        nstr= ch+nstr; //adds each character in front of the existing string
      }
      System.out.println("Reversed word: "+ nstr);
    }
}
'''

code_reverse_array = '''import java.util.Arrays;

public class Reverse_array_usingSwap {
    public static void main(String[] args)
    {
        int[] a = {11,55,88,64,77,22};
        System.out.println(Arrays.toString(a));
        reverse(a);
        System.out.println(Arrays.toString(a));
    }
    static void reverse(int[] x)
    {
        int start = 0;
        int end = x.length - 1;

        while(start<end)
        {
            swap(x, start, end);
            start++;
            end--;
        }
    }

    static void swap(int[] arr, int x, int y)
    {
        int temp = arr[x];
        arr[x] = arr[y]; 
        arr[y] = temp;
    }
}
'''

code_recursion = '''public class Rec_sum {
    public static void main(String[] args) {
        int n = 10;
        System.out.println(sum_rec(n));
    }

    static int sum_rec(int n)
    {
        if(n <= 1)
        {
            return n;
        }

        return n + sum_rec(n-1);
    }
}
'''

code_binary_search = '''public class BinarySearch {
    public static void main(String[] args)
    {
        int[] a = {0,1,9,64,98,101,333};
        int target = 64;
        int ans = binarysearch(a, target);
        System.out.println(ans);
    }   
    static int binarysearch(int[] a, int target)
    {
        int start = 0;
        int end = a.length-1;

        while(start<=end)
        {
            int mid = start + (end-start) / 2;

            if(target > a[mid])
            {
                start = mid + 1;
            }
            else if(target < a[mid])
            {
                end = mid -1;
            }
            else{
                return mid;
            }
        }
        return -1;
    } 
}
'''

code_linear_search = '''

public class LineaSearch {
    public static void main(String[] args)
    {
        int[] a = {45,78,3,78,54,122,98,63};
        int target = 00;
        linearSearch(a,target);
    }

    static void linearSearch(int[] a, int target)
    {
        if(a.length == 0)
        {
            System.out.println("Array is Empty");
        }
        for(int i = 0; i < a.length; i++)
        {
            int element = a[i];
            if(element == target)
            {
                System.out.println(i); //Print the INDEX
                break;                 //Added break so that loop stops after finding the target element
            }
        }

    }
}
'''

code_insertion_sort = '''import java.util.Arrays;

public class insertionSort {
    public static void main(String[] args)
    {
        int a[] = {4, 51, 87, 55, 10};
        insertion_sort(a);
        System.out.println(Arrays.toString(a));
    }

    static void insertion_sort(int[] a)
    {
        for(int i = 0; i < a.length; i++)
        {
            for(int j = i + 1; j > 0; j--)
            {
                if(a[j] < a[j-1])
                {
                    int temp = a[j];
                    a[j] = a[j-1];
                    a[j-1] = temp;
                }
                else{
                    break;
                }
            }
        }
    }
}
'''

cyclic_sort = '''package com.kunal;

import java.util.Arrays;

public class CyclicSort {
    public static void main(String[] args) {
        int[] arr = {5, 4, 3, 2, 1};
        sort(arr);
        System.out.println(Arrays.toString(arr));
    }

    static void sort(int[] arr) {
        int i = 0;
        while (i < arr.length) {
            int correct = arr[i] - 1;
            if (arr[i] != arr[correct]) {
                swap(arr, i , correct);
            } else {
                i++;
            }
        }
    }

    static void swap(int[] arr, int first, int second) {
        int temp = arr[first];
        arr[first] = arr[second];
        arr[second] = temp;
    }


}'''

find_duplicate_number = '''package com.kunal;
// https://leetcode.com/problems/find-the-duplicate-number/
public class FindDuplicate {
    public int findDuplicate(int[] arr) {
        int i = 0;
        while (i < arr.length) {

            if (arr[i] != i + 1) {
                int correct = arr[i] - 1;
                if (arr[i] != arr[correct]) {
                    swap(arr, i , correct);
                } else {
                    return arr[i];
                }
            } else {
                i++;
            }
        }
        return -1;
    }

    static void swap(int[] arr, int first, int second) {
        int temp = arr[first];
        arr[first] = arr[second];
        arr[second] = temp;
    }
}'''

all_star_patterns = '''package com.kunal;

public class Main {
    public static void main(String[] args) {
        pattern31(4);
    }

    static void pattern31(int n) {
        int originalN = n;
        n = 2 * n;
        for (int row = 0; row <= n; row++) {
            for (int col = 0; col <= n; col++) {
                int atEveryIndex = originalN - Math.min(Math.min(row, col), Math.min(n - row, n - col));
                System.out.print(atEveryIndex + " ");
            }
            System.out.println();
        }
    }

    static void pattern30(int n) {
        for (int row = 1; row <= n; row++) {

            for (int space = 0; space < n-row; space++) {
                System.out.print("  ");
            }

            for (int col = row; col >= 1; col--) {
                System.out.print(col + " ");
            }
            for (int col = 2; col <= row; col++) {
                System.out.print(col + " ");
            }

            System.out.println();
        }
    }

    static void pattern17(int n) {
        for (int row = 1; row <= 2 * n; row++) {

            int c = row > n ? 2 * n - row: row;

            for (int space = 0; space < n-c; space++) {
                System.out.print("  ");
            }

            for (int col = c; col >= 1; col--) {
                System.out.print(col + " ");
            }
            for (int col = 2; col <= c; col++) {
                System.out.print(col + " ");
            }

            System.out.println();
        }
    }

    static void pattern28(int n) {
        for (int row = 0; row < 2 * n; row++) {
            int totalColsInRow = row > n ? 2 * n - row: row;

            int noOfSpaces = n - totalColsInRow;
            for (int s = 0; s < noOfSpaces; s++) {
                System.out.print(" ");
            }

            for (int col = 0; col < totalColsInRow; col++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }

    static void pattern5(int n) {
        for (int row = 0; row < 2 * n; row++) {
            int totalColsInRow = row > n ? 2 * n - row: row;
            for (int col = 0; col < totalColsInRow; col++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }

    static void pattern4(int n) {
        for (int row = 1; row <= n; row++) {
            // for every row, run the col
            for (int col = 1; col <= row; col++) {
                System.out.print(col + " ");
            }
            // when one row is printed, we need to add a newline
            System.out.println();
        }
    }

    static void pattern3(int n) {
        for (int row = 1; row <= n; row++) {
            // for every row, run the col
            for (int col = 1; col <= n-row+1; col++) {
                System.out.print("* ");
            }
            // when one row is printed, we need to add a newline
            System.out.println();
        }
    }

    static void pattern1(int n) {
        for (int row = 1; row <= n; row++) {
            // for every row, run the col
            for (int col = 1; col <= n; col++) {
                System.out.print("* ");
            }
            // when one row is printed, we need to add a newline
            System.out.println();
        }
    }

    static void pattern2(int n) {
        for (int row = 1; row <= n; row++) {
            // for every row, run the col
            for (int col = 1; col <= row; col++) {
                System.out.print("* ");
            }
            // when one row is printed, we need to add a newline
            System.out.println();
        }
    }
}'''

quick_sort = '''package com.kunal.sorting;

import java.util.Arrays;

public class QuickSort {
    public static void main(String[] args) {
        int[] arr = {5, 4, 3, 2, 1};
//        sort(arr, 0, arr.length - 1);
//        System.out.println(Arrays.toString(arr));
        Arrays.sort(arr);
    }

    static void sort(int[] nums, int low, int hi) {
        if (low >= hi) {
            return;
        }

        int s = low;
        int e = hi;
        int m = s + (e - s) / 2;
        int pivot = nums[m];

        while (s <= e) {

            // also a reason why if its already sorted it will not swap
            while (nums[s] < pivot) {
                s++;
            }
            while (nums[e] > pivot) {
                e--;
            }

            if (s <= e) {
                int temp = nums[s];
                nums[s] = nums[e];
                nums[e] = temp;
                s++;
                e--;
            }
        }

        // now my pivot is at correct index, please sort two halves now
        sort(nums, low, e);
        sort(nums, s, hi);
    }
}'''

merge_sort = '''package com.kunal.sorting;

import java.util.Arrays;

public class MergeSort {
    public static void main(String[] args) {
        int[] arr = {5, 4, 3, 2, 1};
        mergeSortInPlace(arr, 0, arr.length);
        System.out.println(Arrays.toString(arr));
    }

    static int[] mergeSort(int[] arr) {
        if (arr.length == 1) {
            return arr;
        }

        int mid = arr.length / 2;

        int[] left = mergeSort(Arrays.copyOfRange(arr, 0, mid));
        int[] right = mergeSort(Arrays.copyOfRange(arr, mid, arr.length));

        return merge(left, right);
    }

    private static int[] merge(int[] first, int[] second) {
        int[] mix = new int[first.length + second.length];

        int i = 0;
        int j = 0;
        int k = 0;

        while (i < first.length && j < second.length) {
            if (first[i] < second[j]) {
                mix[k] = first[i];
                i++;
            } else {
                mix[k] = second[j];
                j++;
            }
            k++;
        }

        // it may be possible that one of the arrays is not complete
        // copy the remaining elements
        while (i < first.length) {
            mix[k] = first[i];
            i++;
            k++;
        }

        while (j < second.length) {
            mix[k] = second[j];
            j++;
            k++;
        }

        return mix;
    }



    static void mergeSortInPlace(int[] arr, int s, int e) {
        if (e - s == 1) {
            return;
        }

        int mid = (s + e) / 2;

        mergeSortInPlace(arr, s, mid);
        mergeSortInPlace(arr, mid, e);

        mergeInPlace(arr, s, mid, e);
    }

    private static void mergeInPlace(int[] arr, int s, int m, int e) {
        int[] mix = new int[e - s];

        int i = s;
        int j = m;
        int k = 0;

        while (i < m && j < e) {
            if (arr[i] < arr[j]) {
                mix[k] = arr[i];
                i++;
            } else {
                mix[k] = arr[j];
                j++;
            }
            k++;
        }

        // it may be possible that one of the arrays is not complete
        // copy the remaining elements
        while (i < m) {
            mix[k] = arr[i];
            i++;
            k++;
        }

        while (j < e) {
            mix[k] = arr[j];
            j++;
            k++;
        }

        for (int l = 0; l < mix.length; l++) {
            arr[s+l] = mix[l];
        }
    }

}'''

count_zeros = '''package com.kunal.easy;

public class CountZeros {
    public static void main(String[] args) {
        System.out.println(count(30210004));
    }

    static int count(int n) {
        return helper(n, 0);
    }

    // special pattern, how to pass a value to above calls
    private static int helper(int n, int c) {
        if (n == 0) {
            return c;
        }

        int rem = n % 10;
        if (rem == 0) {
            return helper(n/10, c+1);
        }
        return helper(n/10, c);
    }
}'''

fibo_recursion = '''package com.kunal.intro;

public class Fibo {
    public static void main(String[] args) {
        int ans = fibo(50);
        System.out.println(ans);
    }

    static int fibo(int n) {
        // base condition
        if (n < 2) {
            return n;
        }
        return fibo(n-1) + fibo(n-2);
    }
}'''
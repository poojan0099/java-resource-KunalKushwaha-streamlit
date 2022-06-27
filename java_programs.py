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
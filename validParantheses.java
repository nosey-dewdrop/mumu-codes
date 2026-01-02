import java.util.Scanner;
import java.util.Stack;
public class validParantheses {
      
      public static boolean isValid(String s) {
            Stack<Character> stack = new Stack<>();

            for (char c : s.toCharArray()) {
                  if (c == '(' || c == '{' || c == '[') {
                        stack.push(c);
                  } 

                  else {
                        if (stack.isEmpty()) {
                              return false;
                        }

                        char top = stack.pop();
                        if ((c == ')' && top != '(') ||
                            (c == '}' && top != '{') ||
                            (c == ']' && top != '[')) {
                              return false;
                        }
                  }
            }
            return stack.isEmpty();
      }     

      public static void main (String[] args){
            Scanner scanner = new Scanner(System.in);

            System.out.println("enter the parentheses string:");
            String str = scanner.nextLine();

            boolean result = isValid(str);
            System.out.println("is the parentheses string valid? " + result);
            scanner.close();
      }
}

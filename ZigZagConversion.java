import java.util.Scanner;

class ZigZagConversion {

      public static int findRepetition(String str, int numRows) {

            int period = 2*numRows - 2;
            System.out.println("the period is: " + period);

            int periodCompleted = str.length()/period;
            System.out.println("the period completed is: " + periodCompleted);

            int lambda = numRows-1;
            System.out.println("the lambda is: " + lambda);

            int preceedingChars = str.length() % period;
            System.out.println("the preceeding chars is: " + preceedingChars);

            if(preceedingChars == 0){
                  return lambda*periodCompleted;
            }
            else{
                  return lambda*periodCompleted + 1;
            }
      }


      public static void main (String[] args) {

            Scanner scanner = new Scanner (System.in);

            System.out.print("enter the string to convert: ");
            String str = scanner.nextLine();

            System.out.print("enter the number of rows:");
            int numRows = 0;

            if(scanner.hasNextInt()){
                  numRows = scanner.nextInt();
                  scanner.nextLine();
            }

            int period = findRepetition(str, numRows);
            System.out.println("the repetition of the period is: " + period);

            char[][] zigzag = new char[numRows][period];

            
            scanner.close();
      }

}

import java.util.*;

public class MiniSudoku {

    static int SIZE = 9;
    static int[][] board = new int[SIZE][SIZE];
    static int emptySpaces = SIZE*SIZE;
    static int tries = 0;
    static ArrayList<Integer> tryIDArray;

    public static void printBoard(){
        System.out.println();
        for(int i = 0; i < SIZE; i++){
            for(int j = 0; j < SIZE; j++){

                if(j % 3 == 2){
                    System.out.print(board[i][j]+ " | ");
                }

                else if(j < SIZE-1){
                    System.out.print(board[i][j]+ " ");
                }

                else{
                    System.out.print(board[i][j]+ "");
                }
            }
            System.out.println();
            if(i % 3 == 2 && i < SIZE - 1){
                    System.out.println("------*-------*-------*");
            }
        }
    }

    public static void playPosition(int number, int rows, int columns){

        if(number >= 1 && number <= 9 && board[rows][columns] == 0){
            board[rows][columns] = number;
            emptySpaces--;
        }

        else{
            System.out.println("the board is filled or the number is not proper.");
        }
        
        printBoard();
    }

    public static boolean isPlayed3x3(int number, int rows, int columns){
        for(int i = 0; i < SIZE; i++){
            for(int j = 0; j < SIZE; j++){
                if(number == board[i][j]){
                    return true;
                }
            }
        }
        return false;
    }

    public static boolean isValid(int number, int rows, int columns){

        int triesID = number*100 + rows*10 + columns;
        tryIDArray.add(triesID);

        if(isPlayed3x3(number, rows, columns)){
            System.out.println("cannot play this position due to rules!!");
            printBoard();
            return false; 
        }
        for(int i = 0; i < SIZE; i++){
            if(number == board[rows][i]){
                return false;
            }
        }


        // bir de column sabit tutup rows değiştiriyorum.
        for(int j = 0; j < SIZE; j++){
            if(number == board[j][columns]){
                return false;
            }
        }

        return true;
    }


    public static void playSudoku(){

        Scanner scanner = new Scanner(System.in);
        System.out.print("number to be played 1-9: ");
            int number = scanner.nextInt();

            System.out.println("which position do you want to play?");

            System.out.print("rows: ");
            int rows = scanner.nextInt() - 1;

            System.out.print("columns: ");
            int columns = scanner.nextInt() - 1;



            if(isValid(number, rows, columns)){
                playPosition(number, rows, columns);
            }

            tries++;

            System.out.printf(
                "\nnumber: " + number +
                "\nrows: " + rows +
                "\ncolumns: " + columns +
                "\ntries: " + tries
            );
            
            System.out.println();
            scanner.close();

    }


    public static void playSudokuAI(){
        Random rand = new Random();
        int rows = rand.nextInt(9);      
        int columns = rand.nextInt(9);      
        int number = rand.nextInt(9) + 1; 

        if(isValid(number, rows, columns)){
                playPosition(number, rows, columns);
            }

            tries++;

            System.out.printf(
                "\nnumber: " + number +
                "\nrows: " + rows +
                "\ncolumns: " + columns +
                "\ntries: " + tries
            );
            
            System.out.println();
    }

    public static void main(String[] args) {
        printBoard();

        while(emptySpaces != 0){
            //playSudoku();
            playSudokuAI();
        }
    }
}

/*
this is hard bro. */
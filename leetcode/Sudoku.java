package leetcode;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Sudoku {
      int boardWidth = 400; 
      int boardHeight = 400;

      JFrame frame = new JFrame("sudoku!!!");

      JLabel textLabel = new JLabel();
      JPanel textPanel = new JPanel();

      JPanel boardPanel = new JPanel();


      public Sudoku(){

            frame.setVisible(true);
            frame.setSize(boardWidth, boardHeight);
            frame.setResizable(false); // user cannot resize it.
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // when click x, the app closes.
            frame.setLocationRelativeTo(null);
            frame.setLayout(new BorderLayout()); // place components in the window. nsewc place them. 

            textLabel.setFont(new Font("Arial", Font.BOLD, 30));
            textLabel.setHorizontalAlignment(JLabel.CENTER);
            textLabel.setText("Sudoku: 0");

            textPanel.add(textLabel);
            frame.add(textPanel, BorderLayout.NORTH); // top in the frame. 

      }
}

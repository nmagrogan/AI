/*
Class: CPSC 427 
Team Member 1: Nathan Magrogan
Team Member 2: none
Submitted By Nathan Magrogan
GU Username: nmagrogan
File Name: TSPTest.java
 Usage: java WordGuess <paramFile> <start data file>
 Example: java WordGuess param.dat start_data.txt
    Using the parameter file, param.dat, try to find a soulutioin for the 
    traveling sales person problem.
*/

import java.lang.*;
import java.io.*;
import java.util.*;

public class TSPTest
{

 public static void main(String args[])
    {

        TSP TSP1 = new TSP(args[0],args[1]);


        System.out.println();
        //TSP1.DisplayParams(); //Uncomment to display the contents of the parameter file
        TSP1.DisplayPop(); //Uncomment to display the population before evolution
        TSP1.Evolve();
        //WG1.DisplayPop(); Uncomment to display the population after evolution
        System.out.println();
        
    }
}




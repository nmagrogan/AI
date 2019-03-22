/*
 Usage: java WordGuess <paramFile> <targetWord>
 Example: java WordGuess param.dat genetic
    Using the parameter file, param.dat, try to generate the word "genetic."
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
        //TSP1.Evolve();
        //WG1.DisplayPop(); Uncomment to display the population after evolution
        System.out.println();
        
    }
}


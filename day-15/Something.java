/*
An example of a Java program, with all its flaws.
*/

import java.util.Scanner;

class Something {

    public static void main(String[] args) {
        /**
         * This is a simple main function.  It is automatically run when the program is run.
         */

        // all variables and functions are "typed"... the data type is indicated and required.
        int doSomething = 10; // declare and assign a value

        // variable declarations can be separated from their assignments
        boolean keepGoing; // declare a variable, but don't assign it a value
        keepGoing = true; // assign a value to the variable

        // print some output
        System.out.println("Hello world!")

        // get input from the user... look how hard this is!
        System.out.println("Please enter something: ");
        Scanner scanner = new Scanner(System.in); // make a scanner to read input
        String someResponse = scanner.nextLine(); // get the input up until the user presses enter
        scanner.close(); // close the scanner to avoid resource leaks
        System.out.println("You entered: " + someResponse); // output the user's response

    }
}

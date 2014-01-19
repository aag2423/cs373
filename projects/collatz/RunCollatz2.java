// ---------------------------------
// projects/collatz/RunCollatz2.java
// Copyright (C) 2014
// Glenn P. Downing
// ---------------------------------

/*
To run the program:
    % javac -Xlint RunCollatz2.java
    % java  -ea    RunCollatz2 < RunCollatz.in > RunCollatz.out

To document the program:
    % javadoc -d html -private Collatz2.java
*/

// -------
// imports
// -------

import java.io.IOException;
import java.io.PrintWriter;
import java.io.Writer;

import java.util.Scanner;

// ----------
// RunCollatz
// ----------

final class RunCollatz2 {
    public static void main (String[] args) throws IOException {
        final Scanner r = new Scanner(System.in);
        final Writer  w = new PrintWriter(System.out);
        Collatz2.solve(r, w);}}

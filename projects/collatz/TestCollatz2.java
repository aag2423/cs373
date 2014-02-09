// ----------------------------------
// projects/collatz/TestCollatz2.java
// Copyright (C) 2014
// Glenn P. Downing
// ----------------------------------

/*
To test the program:
    % locate junit4-4.8.2.jar
    /usr/share/java/junit4-4.8.2.jar
    % setenv CLASSPATH .:/usr/share/java/junit4-4.8.2.jar
    % javac -Xlint TestCollatz2.java
    % java  -ea    TestCollatz2 >& TestCollatz.java.out
*/

// -------
// imports
// -------

import java.io.IOException;
import java.io.StringWriter;
import java.io.Writer;

import java.util.Iterator;
import java.util.Scanner;

import junit.framework.Assert;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import junit.textui.TestRunner;

// -----------
// TestCollatz
// -----------

public final class TestCollatz2 extends TestCase {
    // ----
    // read
    // ----

    public void testRead () {
        final Scanner         r = new Scanner("1 10\n");
        final Iterable<int[]> x = Collatz2.read(r);
        final Iterator<int[]> p = x.iterator();
        Assert.assertTrue(p.hasNext());
        int[] a = p.next();
        Assert.assertTrue(a[0] ==  1);
        Assert.assertTrue(a[1] == 10);}

    // ----
    // eval
    // ----

    public void testEval1 () {
        final Iterable<int[]> x = Collatz2.eval(new ReadItr(new Scanner("1 10\n")));
        final Iterator<int[]> p = x.iterator();
        final int[]           a = p.next();
        Assert.assertTrue(a[0] == 20);}

    public void testEval2 () {
        final Iterable<int[]> x = Collatz2.eval(new ReadItr(new Scanner("100 200\n")));
        final Iterator<int[]> p = x.iterator();
        final int[]           a = p.next();
        Assert.assertTrue(a[0] == 20);}

    public void testEval3 () {
        final Iterable<int[]> x = Collatz2.eval(new ReadItr(new Scanner("201 210\n")));
        final Iterator<int[]> p = x.iterator();
        final int[]           a = p.next();
        Assert.assertTrue(a[0] == 20);}

    public void testEval4 () {
        final Iterable<int[]> x = Collatz2.eval(new ReadItr(new Scanner("900 1000\n")));
        final Iterator<int[]> p = x.iterator();
        final int[]           a = p.next();
        Assert.assertTrue(a[0] == 20);}

    // -----
    // print
    // -----

    public void testPrint () throws IOException {
        final Writer w = new StringWriter();
        Collatz2.print(w, new EvalItr(new ReadItr(new Scanner("1 10\n"))));
        Assert.assertTrue(w.toString().equals("1 10 20\n"));}

    // -----
    // solve
    // -----

    public void testSolve () throws IOException {
        final Scanner r = new Scanner("1 10\n100 200\n201 210\n900 1000\n");
        final Writer  w = new StringWriter();
        Collatz2.solve(r, w);
        Assert.assertTrue(w.toString().equals("1 10 20\n100 200 125\n201 210 89\n900 1000 174\n"));}

    // ----
    // main
    // ----

    public static void main (String[] args) {
        System.out.println("TestCollatz2.java");
        TestRunner.run(new TestSuite(TestCollatz2.class));
        System.out.println("Done.");}}

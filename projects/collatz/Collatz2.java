// ------------------------------
// projects/collatz/Collatz2.java
// Copyright (C) 2014
// Glenn P. Downing
// ------------------------------

import java.io.IOException;
import java.io.Writer;

import java.util.Iterator;
import java.util.Scanner;

class Itr implements Iterable<int[]>, Iterator<int[]> {
    Scanner _r;

    /**
     * @return true if not empty
     */
    public Itr (Scanner r) {
        _r = r;}

    public boolean hasNext () {
        return _r.hasNext();}

    public Iterator<int[]> iterator () {
        return this;}

    /**
     * reads two ints into a[0] and a[1]
     * @return an array of int
     */
    public int[] next () {
        final int[] a = {0, 0};
        a[0] = _r.nextInt();
        a[1] = _r.nextInt();
        assert a[0] > 0;
        assert a[1] > 0;
        return a;}

    public void remove ()
        {}}

public final class Collatz2 {
    // ----
    // read
    // ----

    public static Iterable<int[]> read (Scanner r) {
        return new Itr(r);}

    // ----
    // eval
    // ----

    /**
     * @param i the beginning of the range, inclusive
     * @param j the end       of the range, inclusive
     * @return the max cycle length in the range [i, j]
     */
    public static int eval (int i, int j) {
        assert i > 0;
        assert j > 0;
        // <your code>
        int v = 1;
        assert v > 0;
        return v;}

    // -----
    // print
    // -----

    /**
     * prints the values of i, j, and v
     * @param w a java.io.Writer
     * @param i the beginning of the range, inclusive
     * @param j the end       of the range, inclusive
     * @param v the max cycle length
     */
    public static void print (Writer w, int i, int j, int v) throws IOException {
        assert i > 0;
        assert j > 0;
        assert v > 0;
        w.write(i + " " + j + " " + v + "\n");
        w.flush();}

    // -----
    // solve
    // -----

    /**
     * @param r a java.util.Scanner
     * @param w a java.io.Writer
     */
    public static void solve (Scanner r, Writer w) throws IOException {
        for (int[] a : read(r)) {
            final int v = eval(a[0], a[1]);
            print(w, a[0], a[1], v);}}}

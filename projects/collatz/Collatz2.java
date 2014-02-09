// ------------------------------
// projects/collatz/Collatz2.java
// Copyright (C) 2014
// Glenn P. Downing
// ------------------------------

import java.io.IOException;
import java.io.Writer;

import java.util.Iterator;
import java.util.Scanner;

class EvalItr implements Iterable<int[]>, Iterator<int[]> {
    Iterator<int[]> _p;

    public EvalItr (Iterable<int[]> a) {
        _p = a.iterator();}

    /**
     * @return true if not empty
     */
    public boolean hasNext () {
        return _p.hasNext();}

    public Iterator<int[]> iterator () {
        return this;}

    /**
     * @return an array of three ints, i, j, and v
     * @       i the beginning of the range, inclusive
     * @       j the end       of the range, inclusive
     * @       v the max cycle length
     */
    public int[] next () {
        final int[] a = _p.next();
        assert a[0] > 0;
        assert a[1] > 0;
        // <your code>
        int v = 1;
        assert v > 0;
        return new int[]{a[0], a[1], v};}

    public void remove ()
        {}}

class ReadItr implements Iterable<int[]>, Iterator<int[]> {
    Scanner _r;

    public ReadItr (Scanner r) {
        _r = r;}

    /**
     * @return true if not empty
     */
    public boolean hasNext () {
        return _r.hasNext();}

    public Iterator<int[]> iterator () {
        return this;}

    /**
     * @return an array of two ints, i and j
     * @       i the beginning of the range, inclusive
     * @       j the end       of the range, inclusive
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

    /**
     * @param r a java.util.Scanner
     * @return an iterable of an array of two ints, i and j
     * @       i the beginning of the range, inclusive
     * @       j the end       of the range, inclusive
     */
    public static Iterable<int[]> read (Scanner r) {
        return new ReadItr(r);}

    // ----
    // eval
    // ----

    /**
     * @param an iterable of an array of two ints, i and j
     * @      i the beginning of the range, inclusive
     * @      j the end       of the range, inclusive
     * @return an iterable of an array of three ints, i, j, and v
     * @      i the beginning of the range, inclusive
     * @      j the end       of the range, inclusive
     * @      v the max cycle length
     */
    public static Iterable<int[]> eval (Iterable<int[]> a) {
        return new EvalItr(a);}

    // -----
    // print
    // -----

    /**
     * prints the values of i, j, and v
     * @param w a java.io.Writer
     * @param an iterable of an array of three ints, i, j, and v
     * @      i the beginning of the range, inclusive
     * @      j the end       of the range, inclusive
     * @      v the max cycle length
     */
    public static void print (Writer w, Iterable<int[]> a) throws IOException {
        for (int[] b : a) {
            w.write(b[0] + " " + b[1] + " " + b[2] + "\n");
            w.flush();}}

    // -----
    // solve
    // -----

    /**
     * @param r a java.util.Scanner
     * @param w a java.io.Writer
     */
    public static void solve (Scanner r, Writer w) throws IOException {
        print(w, eval(read(r)));}}

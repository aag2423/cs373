// ------------
// Adapter.java
// ------------

// http://en.wikipedia.org/wiki/Adapter_pattern

import java.util.ArrayList;

class Stack<T> {
    private ArrayList<T> _a;

    public Stack () {
        _a = new ArrayList<T>();}

    public Boolean empty () {
        return _a.isEmpty();}

    public void pop () {
        _a.remove(_a.size() - 1);}

    public void push (T v) {
        _a.add(v);}

    public T top () {
        return _a.get(_a.size() - 1);}}

final class Adapter {
    public static void main (String[] args) {
        System.out.println("Adapter.java");

        Stack<Integer> s = new Stack<Integer>();
        s.push(2);
        s.push(3);
        s.push(4);
        assert s.top() == 4;
        s.pop();
        assert s.top() == 3;

        System.out.println("Done.");}}

// ---------------
// Reflection.java
// ---------------

interface I {
    String f ();}

final class A implements I {
    public String f () {
        return "A.f()";}}

final class B implements I {
    public String f () {
        return "B.f()";}}

final class C {
    private C ()
        {}}

final class D {
    public D (int i)
        {}}

abstract class E
    {}

class F
    {}

final class Reflection {
    public static void main (String[] args) {
        System.out.println("Reflection.java");

        try {
            assert ((I) A.class.newInstance()).f() == "A.f()";
            assert ((I) B.class.newInstance()).f() == "B.f()";}
        catch (ClassCastException e) {
            assert false;}
        catch (IllegalAccessException e) {
            assert false;}
        catch (InstantiationException e) {
            assert false;}

        try {
            assert ((I) new A().getClass().newInstance()).f() == "A.f()";
            assert ((I) new B().getClass().newInstance()).f() == "B.f()";}
        catch (ClassCastException e) {
            assert false;}
        catch (IllegalAccessException e) {
            assert false;}
        catch (InstantiationException e) {
            assert false;}

        try {
            assert ((I) Class.forName("A").newInstance()).f() == "A.f()";
            assert ((I) Class.forName("B").newInstance()).f() == "B.f()";}
        catch (ClassCastException e) {
            assert false;}
        catch (ClassNotFoundException e) {
            assert false;}
        catch (IllegalAccessException e) {
            assert false;}
        catch (InstantiationException e) {
            assert false;}

        try {
            Class.forName("C").newInstance();
            assert false;}
        catch (ClassNotFoundException e) {
            assert false;}
        catch (IllegalAccessException e) {
            assert e.toString().equals("java.lang.IllegalAccessException: Class Reflection can not access a member of class C with modifiers \"private\"");}
        catch (InstantiationException e) {
            assert false;}

        try {
            Class.forName("D").newInstance();
            assert false;}
        catch (ClassNotFoundException e) {
            assert false;}
        catch (IllegalAccessException e) {
            assert false;}
        catch (InstantiationException e) {
            assert e.toString().equals("java.lang.InstantiationException: D");}

        try {
            Class.forName("E").newInstance();
            assert false;}
        catch (ClassNotFoundException e) {
            assert false;}
        catch (IllegalAccessException e) {
            assert false;}
        catch (InstantiationException e) {
            assert e.toString().equals("java.lang.InstantiationException");}

        try {
            Class.forName("I").newInstance();
            assert false;}
        catch (ClassNotFoundException e) {
            assert false;}
        catch (IllegalAccessException e) {
            assert false;}
        catch (InstantiationException e) {
            assert e.toString().equals("java.lang.InstantiationException: I");}

        try {
            I x = (I) Class.forName("F").newInstance();
            assert false;}
        catch (ClassCastException e) {
            assert e.toString().equals("java.lang.ClassCastException: F cannot be cast to I");}
        catch (ClassNotFoundException e) {
            assert false;}
        catch (IllegalAccessException e) {
            assert false;}
        catch (InstantiationException e) {
            assert e.toString().equals("java.lang.InstantiationException: I");}

        try {
            Class.forName("G").newInstance();
            assert false;}
        catch (ClassNotFoundException e) {
            assert e.toString().equals("java.lang.ClassNotFoundException: G");}
        catch (IllegalAccessException e) {
            assert false;}
        catch (InstantiationException e) {
            assert false;}

        System.out.println("Done.");}}

// --------------
// Singleton.java
// --------------

class A {
    private static final A _only = new A();

    private A ()
        {}

    public static A only () {
        return _only;}

    public String f () {
        return "A.f()";}}

class B {
    private static B _only;

    private B ()
        {}

    public static B only () {
        if (B._only == null)
            B._only = new B();
        return B._only;}

    public String f () {
        return "B.f()";}}

final class Singleton {
    public static void main (String[] args) {
        System.out.println("Singleton.java");

        assert A.only()     == A.only();
        assert A.only().f() == "A.f()";

        assert B.only()     == B.only();
        assert B.only().f() == "B.f()";

        System.out.println("Done.");}}

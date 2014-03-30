// ---------
// Test.java
// ---------

class A {}
class B extends A {}

final class Test {

    public static void main (String[] args) {
        System.out.println("Test.java");

        A x = new A();
        B y = new B();
        System.out.println(x == y);

        System.out.println("Done.");}}

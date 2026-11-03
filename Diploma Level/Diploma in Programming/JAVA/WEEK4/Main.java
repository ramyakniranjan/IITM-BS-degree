package WEEK4;

// Abstarct class
abstract class Animal {
    // Abstract method doesn't have a body
    public abstract void animalSound();
    // Regular method
    public void sleep(){
        System.out.println("Zzz");
    }
}

// Subclass (inherit from Animal)
class Pig extends Animal {
    public void animalSound() {
        // The body of animal sound is provided here
        System.out.println("The pig says: wee wee");
    }
}

class Main {
     public static void main(String[] args) {
        Pig myPig = new Pig();
        myPig.animalSound();
        myPig.sleep();    
    }
}
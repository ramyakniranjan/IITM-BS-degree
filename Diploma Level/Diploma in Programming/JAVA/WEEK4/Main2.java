package WEEK4;

// interface
interface Bird {
    public  void birdSound(); // interface method (doesn't have a body)
    public void fly(); // interface method (doesn't have a body)
}

class Crow implements Bird {
    public void birdSound() {
        System.out.println("The crow says: caw caw");
    }
    public void fly() {
        System.out.println("yes");
    }
}

class Main2 {
    public static  void  main(String[] args) {
        Crow myCrow = new Crow();
        myCrow.birdSound();
        myCrow.fly();
    }
}
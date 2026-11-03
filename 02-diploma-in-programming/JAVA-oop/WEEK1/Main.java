public class Main{
    public static void main(String[] args){
        Animal animal1 = new Animal();  //Instance of class Animal
        Animal animal2 = new Animal();  //Another instance of class Animal
        Dog dog = new Dog();
        animal1.walk();
        dog.walk();
    }
}

class Animal{
//  super class
    // its own data
    String name;
    int age;
    // its own methods
    public void walk(){
        System.out.println("walk");
    }
}
// template to create "instances" / "objects" of the Animal

class Dog extends Animal{
// subclass - inheritence
}
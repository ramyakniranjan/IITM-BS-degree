package WEEK4.AQ1;

interface Shape{
    //no constructor
    int a = 10 ; //must be initialized ,
    //abstract methods in interface
	void draw(); //method which doesnt have a  body/implementation/defintion //implicitly , public and abstract
	//1.cannot create objects
	//default method : method with implementation in interface
	default void f(){
	    System.out.println("default method in interface");
	}
	//static methods in interface
	static void s(){
	     System.out.println("static method in interface");
	}
	
}

class Circle implements Shape{
   
    public void draw() {//mandatory to define 
		System.out.println("Drawing a Circle");
	}
	

}
class Square implements Shape{
	public void draw() {
		System.out.println("Drawing a Square");
	}
}
class Rectangle implements Shape{
	public void draw() {
		System.out.println("Drawing a Rectangle");
	}
}
public class Main {
	//we cant create objects of abstract class
	public static void main(String[] args) {
	
	Shape c1 = new Circle();     //The reference variable s1 is of type Shape, the object is of type Circle
	c1.draw();
	c1.f();
    Shape.s();



}	
	
}
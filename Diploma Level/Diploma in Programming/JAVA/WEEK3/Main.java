package WEEK3;

public class Employee {
	  private String name;
	  private double salary;

	  public Employee(String n, double s) { //access modifier , public,default(no modiefier, protected . private)
	    this.name = n;
	    this.salary = s;
	  }

	  public void setName(String n) {
	    this.name = n;
	  }

	  public void setSalary(double s) {
	    this.salary = s;
	  }

	  public String getName() {
	    return this.name;
	  }

	  public double getSalary() {
	    return this.salary;
	  }

	  public double bonus(float percent){
	    return(percent/100.0)*salary; //67/100*100 = 67
	  }
	}

class Manager extends Employee {
	  private String secretary;

	  public Manager(String n, double s, String sec) {
	    super(n, s);// this is a call to superclass matching Employee constructor
	    this.secretary = sec;
	  }

	  public void setSecretary(String sec) {
	    this.secretary = sec;
	  }

	  public String getSecretary() {
	    return this.secretary;
	  }

	  public double bonus(float percent) { //method overriding : giving a new definition for method from the parent class
	    double b = super.bonus(percent);  //invoke the bonus method of Employee class
	    
	    return 1.5 * b; //1.5*67 = 100.5
	  }
	}
public class Main {
    public static void main(String[] args){
        Employee e1 = new Employee("Hiya", 250000);
        System.out.println(e1.getName());
        
        
        
        Employee obj = new Manager("Liya", 100, "Kiran");  //Parent class reference variable = child class object
        System.out.println(obj.getName());
        System.out.println(obj.getSalary());
       // System.out.println(obj.getSecretary()); //here
        System.out.println(obj.bonus(67));//prev bonus: 67, curent bonjs:100.5. //static means compile time, dynamic means runtime
     



        
    }

} {
    
}

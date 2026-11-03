package WEEK4.AQ1;

public class Operation extends Calculator{
     public int addition(int c,int d){
          return c+d;
     }

     public int subtraction(int c,int d){
          return c-d;
     }

     public int division(int c,int d){
          return c/d;
     }

     public static void main(String args[]){
          Operation obj = new Operation();
          System.out.println(obj.division(5,2));
     }
}

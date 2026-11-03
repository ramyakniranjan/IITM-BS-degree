public static int factorial(int n) {
    if (n==0){
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

public static void main(String[] args){
    int input = 3;  // Local variable
    int result = factorial(input);
    System.out.println("Factorial of " + input +" is: " + result);
}
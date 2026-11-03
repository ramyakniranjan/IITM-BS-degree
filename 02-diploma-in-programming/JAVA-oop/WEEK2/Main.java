public class Main {
    // int myNumber = 56;           // 2147483647   // primitive variables stored in heap
    int myNumbaer;                  // 32 bits (+/-)()()-> max value that an int an hold 2^31
    myNumber = 56;
    int a = 2147483647;
    
    long a = 2147483648L;           //L indicates change in int to long if value of int is above 2^31-1
    long mynum = 214L;              //64 bits   //(+/-)2^63-1

    long myNumLong = myNumber;      // long can take int// default
    int muNumInt = (int) myNum;     //explicit type casting, reduces to 32 if long is bigger, information is lost

    float myFLoat = 3.14f;          //32 bit
    double myDouble = 4.5;          //default max precisson, 64 bit, more precise, bigger than float    // variable

    char myChar = 'A';              // single quote is char, double is string
    boolean myBoolean = true;

    String myString = "Hello Java"; //String is a class in java, aleardy defined so 'String' not 'string', reference type, 
                                    // heap meomray, variable in stack carry address to location

}
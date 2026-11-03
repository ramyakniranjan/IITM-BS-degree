package WEEK1;

class BankAccount{
    // Instance variables are stored in HEAP inside the BankAccount object
    private int accountNumber;
    private double balance;

    public BankAccount(int accountNumber, double intitialBalance){
        this.accountNumber = accountNumber;
        this.balance = intitialBalance;
    }

    public void depositBonus(double baseBonus){
        // Local variables & parameters are stored in depositBonus() STACK frame
        double multiplier = 1.5;
        double finalBonus = baseBonus + multiplier;

        this.balance += finalBonus; // Modifies balance in HEAP
    }

    public void display(){
        System.out.println("Account #" + accountNumber +" Balance: $" + balance);
    }
}

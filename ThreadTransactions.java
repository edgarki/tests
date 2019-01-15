//Java Chanllenge
//Java Threads: Transactions

//implement classes Account and Transaction to simulate banking system
//Transaction class have to call Account to execute deposit and withdraw
//remember to synchronize methods to follow their code using threads


//example of input (value of threadsCount, transactionsCount, total number of transactions performed by each of the threads
//2
//3
//3

//example of this output
/Depositing $59
//Withdrawing $2
//Depositing $62
//Depositing $16
//Withdrawing $52
//Balance $83

//the output isn't deterministic considering Random
//TransactionRunnable and Solution classes are given


import java.security.SecureRandom;
import java.util.List;
import java.util.Scanner;

import java.util.ArrayList;

/*
 * Create the Account and Transaction classes here.
 */
class Account {
    int balance = 0;

    String deposit(int money) {
        // System.out.println(getBalance());
        balance += money;
        return "Depositing $" + money;
    }

    String withdraw(int money) {
        // System.out.println(getBalance());
        if (getBalance() >= money) {
            balance -= money;
            return "Withdrawing $" + money;
        } else
            return "Withdrawing $" + money + " (Insufficient Balance)";
    }

    int getBalance() {
        return balance;
    }

}

class Transaction {
    private List<String> t = new ArrayList<String>();
    private Account acc = new Account();

    Transaction(Account a) {
        t = new ArrayList<String>();
        acc = a;
    }

    synchronized void deposit(int money) {

        // String o = acc.deposit(money);
        // System.out.println(o);
        // recordTransaction(o);
        try {
            recordTransaction(acc.deposit(money));
        } catch (Exception e) {
        }
    }

    synchronized void withdraw(int money) {
        // String o = acc.withdraw(money);
        // System.out.println(o);
        // recordTransaction(o);
        try {
            recordTransaction(acc.withdraw(money));
        } catch (Exception e) {
        }
    }

    private void recordTransaction(String m) {
        t.add(m);
    }

    List<String> getTransaction() {
        return t;
    }
}
class TransactionRunnable implements Runnable {
    private static final SecureRandom RANDOM_GENERATOR = new SecureRandom();
    private final Transaction transaction;
    private final int transactionsCount;
    
    public TransactionRunnable(Transaction transaction, int transactionsCount) {
        this.transaction = transaction;
        this.transactionsCount = transactionsCount;
    }
    
    @Override
    public void run() {
        for (int i = 0; i < this.transactionsCount; i++) {
            int transactionType = RANDOM_GENERATOR.nextInt() % 2;
            int money = RANDOM_GENERATOR.nextInt(100) + 1;

            if (transactionType == 0) {
                this.transaction.deposit(money);
            } else {
                this.transaction.withdraw(money);
            }
        }
    }
}

public class Solution {
    private static final Scanner SCANNER = new Scanner(System.in);
    private static final Account ACCOUNT = new Account();
    private static final Transaction TRANSACTION = new Transaction(ACCOUNT);
    
    public static void main(String[] args) throws InterruptedException {
        int threadsCount = Integer.parseInt(SCANNER.nextLine());
        Thread[] threads = new Thread[threadsCount];
        
        int expectedTransactionsCount = 0;
        for (int i = 0; i < threadsCount; i++) {
            int transactionsCount = Integer.parseInt(SCANNER.nextLine());
            expectedTransactionsCount += transactionsCount;
            
            threads[i] = new Thread(new TransactionRunnable(TRANSACTION, transactionsCount));
        }
        
        for (int i = 0; i < threadsCount; i++) {
            threads[i].start();
        }
        
        for (int i = 0; i < threadsCount; i++) {
            threads[i].join();
        }
        
        List<String> transactions = TRANSACTION.getTransaction();
        
        if (transactions.size() != expectedTransactionsCount) {
            System.out.println("Wrong Answer");
        } else {
            boolean correct = true;
            for (String transaction: transactions) {
                if (transaction == null) {
                    correct = false;
                    
                    break;
                }
            }
            
            if (!correct) {
                System.out.println("Wrong Answer");
            } else {
                int balance = ACCOUNT.getBalance();
                
                if (balance < 0) {
                    System.out.println("Wrong Answer");
                } else {
                    for (String transaction: transactions) {
                        System.out.println(transaction);
                    }

                    System.out.println("Balance $" + balance);
                }
            }
        }
    }
}

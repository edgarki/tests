//Java Challenge
//errors and exceptions in java
//simulation of a digital wallet to send and receive money easier with auth.


//example of input
//2
//1 Julia bff834a2c117a76d9ceb782f98e428686ca3c4ea
//2 Samantha
//10
//1 pay 50
//1 add 100
//1 add 0
//1 pay 30
//2 add 500
//1 add -5
//1 add 1000
//1 pay -20
//1 pay 100
//1 add 720

//example of output
//INSUFFICIENT_BALANCE: Insufficient balance.
//Wallet successfully credited.
//INVALID_AMOUNT: Amount should be greater than zero.
//Wallet successfully debited.
//USER_NOT_AUTHORIZED: User not authorized.
//INVALID_AMOUNT: Amount should be greater than zero.
//Wallet successfully credited.
//INVALID_AMOUNT: Amount should be greater than zero.
//Wallet successfully debited.
//Wallet successfully credited.
//
//1 Julia 1690
//2 Samantha 0



//create TransactionException, DigitalWallet, and DigitalWalletTransaction classes
//Solution method was given


import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;


/*
 * Create TransactionException, DigitalWallet, and DigitalWalletTransaction classes here.
 */
class TransactionException extends Exception {
    private String errorMessage, errorCode;

    TransactionException(String errorMessage) {
        super(errorMessage);
    }

    TransactionException(String errorMessage, Throwable errorCode) {
        super(errorMessage, errorCode);
    }

    TransactionException(String errorMessage, String errorCode) {
        super(errorMessage);
        this.errorCode = errorCode;
    }

    String getErrorCode() {
        return this.errorCode;
    }
}

class DigitalWallet {
    private String walletId, userName, userAccessCode;
    private int balance;

    DigitalWallet(String walletId, String userName) {
        this.walletId = walletId;
        this.userName = userName;
        this.balance = 0;
    }

    DigitalWallet(String walletId, String userName, String userAccessCode) {
        this.walletId = walletId;
        this.userName = userName;
        this.userAccessCode = userAccessCode;
        this.balance = 0;
    }

    String getWalletId() {
        return this.walletId;
    }

    String getUsername() {
        return this.userName;
    }

    String getUserAccessToken() {
        return this.userAccessCode;
    }

    int getWalletBalance() {
        return this.balance;
    }

    void setWalletBalance(int walletBalance) {
        this.balance = walletBalance;
    }

}

class DigitalWalletTransaction {

    void addMoney(DigitalWallet digitalWallet, int amount) throws TransactionException {
        int now = digitalWallet.getWalletBalance();

        if (digitalWallet.getUserAccessToken() == null) {
            throw new TransactionException("User not authorized", "USER_NOT_AUTHORIZED");
        }
        if (amount > 0) {
            digitalWallet.setWalletBalance(now + amount);
        } else {
            throw new TransactionException("Amount should be greater than zero", "INVALID_AMOUNT");
        }

    }

    void payMoney(DigitalWallet digitalWallet, int amount) throws TransactionException {

        int now = digitalWallet.getWalletBalance();
        if (digitalWallet.getUserAccessToken() == null) {
            throw new TransactionException("User not authorized", "USER_NOT_AUTHORIZED");
        }

        if (amount < 0) {
            throw new TransactionException("Amount should be greater than zero", "INVALID_AMOUNT");
        }

        if (now < amount) {
            throw new TransactionException("Insufficient balance", "INSUFFICIENT_BALANCE");
        }

        if (now >= amount && amount > 0) {
            digitalWallet.setWalletBalance(now - amount);
        }

    }

}
 
public class Solution {
    private static final Scanner INPUT_READER = new Scanner(System.in);
    private static final DigitalWalletTransaction DIGITAL_WALLET_TRANSACTION = new DigitalWalletTransaction();
    
    private static final Map<String, DigitalWallet> DIGITAL_WALLETS = new HashMap<>();
    
    public static void main(String[] args) {
        int numberOfWallets = Integer.parseInt(INPUT_READER.nextLine());
        while (numberOfWallets-- > 0) {
            String[] wallet = INPUT_READER.nextLine().split(" ");
            DigitalWallet digitalWallet;
            
            if (wallet.length == 2) {
                digitalWallet = new DigitalWallet(wallet[0], wallet[1]);
            } else {
                digitalWallet = new DigitalWallet(wallet[0], wallet[1], wallet[2]);
            }
            
            DIGITAL_WALLETS.put(wallet[0], digitalWallet);
        }
        
        int numberOfTransactions = Integer.parseInt(INPUT_READER.nextLine());
        while (numberOfTransactions-- > 0) {
            String[] transaction = INPUT_READER.nextLine().split(" ");
            DigitalWallet digitalWallet = DIGITAL_WALLETS.get(transaction[0]);
            
            if (transaction[1].equals("add")) {
                try {
                    DIGITAL_WALLET_TRANSACTION.addMoney(digitalWallet, Integer.parseInt(transaction[2]));
                    System.out.println("Wallet successfully credited.");
                } catch (TransactionException ex) {
                    System.out.println(ex.getErrorCode() + ": " + ex.getMessage() + ".");
                }
            } else {
                try {
                    DIGITAL_WALLET_TRANSACTION.payMoney(digitalWallet, Integer.parseInt(transaction[2]));
                    System.out.println("Wallet successfully debited.");
                } catch (TransactionException ex) {
                    System.out.println(ex.getErrorCode() + ": " + ex.getMessage() + ".");
                }
            }
        }
        
        System.out.println();
        
        DIGITAL_WALLETS.keySet()
                .stream()
                .sorted()
                .map((digitalWalletId) -> DIGITAL_WALLETS.get(digitalWalletId))
                .forEachOrdered((digitalWallet) -> {
                    System.out.println(digitalWallet.getWalletId()
                            + " " + digitalWallet.getUsername()
                            + " " + digitalWallet.getWalletBalance());
                });
    }
}

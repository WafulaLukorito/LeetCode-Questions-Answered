
// Count the number of prime numbers less than a non-negative number, n.

//* Sieve of Erastothenes */

import java.util.Arrays;

public class CountPrimes{
    public static int countPrimes (int n){
       if (n < 2){
        return 0;
       }

       boolean[] isPrime = new boolean[n];
       Arrays.fill(isPrime, true);

       for (int i=2; i*i < n; i++){
        if (isPrime[i]){
        for (int j= i*i; j< n; j+=i){
            isPrime[j] = false;

        }
       }
    }
    
    int count = 0;
     for (boolean p: isPrime){
        if (p){
            count++;
        }
     }
     return count;
    }

     public static void main(String[] args) {
        int n = 10;
        System.out.println("Number of primes less than " + n + ": " + countPrimes(n));
    }

}
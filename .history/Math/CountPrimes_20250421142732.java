
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

       isPrime[0] = isPrime[1] = false;

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

// Alternative Approach (Bit Manipulation for Space Optimization)
// If memory is a constraint, you can use a bitmask instead of a boolean array to reduce space usage (each bit represents a number). However, this complicates the code and is less readable.

// java
// import java.util.BitSet;

// public static int countPrimesBitSet(int n) {
//     if (n <= 2) return 0;
//     BitSet primes = new BitSet(n);
//     primes.set(2, n);
//     for (int i = 2; i * i < n; i++) {
//         if (primes.get(i)) {
//             for (int j = i * i; j < n; j += i) {
//                 primes.clear(j);
//             }
//         }
//     }
//     return primes.cardinality();
// }
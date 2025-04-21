
// Count the number of prime numbers less than a non-negative number, n.

//* Sieve of Erastothenes */

import java.util.Arrays;

public class CountPrimes{
    public static int countPrimes (int n){
        if (n<2){
            return 0;
        }

        boolean[] isPrime = new boolean[n];
        Arrays.fill (isPrime, true);
        isPrime[0] = isPrime[1] = false;
        int count = 0;

        for (int i=2; i*i < n; i++){
            if (isPrime[i]){
                for (int j = i*i; j < n; j+=i){
                    isPrime[j]= false;

                }
            }
        }
        for (i=0; i<n-1; i++){
            if (isPrime[i]){
                count ++;
            }
        }
        return count;
    }
}
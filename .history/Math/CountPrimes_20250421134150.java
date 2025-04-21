
// Count the number of prime numbers less than a non-negative number, n.

//* Sieve of Erastothenes */

public class CountPrimes{
    public static int (int n){
        if (n<2){
            return 0;
        }

        boolean[] isPrime = new boolean[n];
        Arrays.fill (isPrime, true);
        isPrime[0] = isPrime[1] = false;
    }
}
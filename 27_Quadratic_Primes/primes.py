from linkedlist import Node, LinkedList
import math
import pdb
        
class Primes:
    """
    Prime numbers producer and checker
    """

    def __init__(self):
        # We add the three first primes
        self.primes = [2, 3, 5]

        # Candidates generator
        self.candidates = self._get_candidates()
        
    def is_prime(self, n):
        """
        Checks whether n is prime
        """
        if n < self.primes[-1]:
            return n in self.primes

        while True:
            p = self._get_next_prime()
            if p > n:
                return False
            elif p == n:
                return True
            # p < n: oontinue

    def get_primes(self):
        """
        Prime numbers generators method
        """

        # while we have a number under last_check_prime, we
        # return it.  Once we get above it, we get a candidate
        # and check it
        for prime in self.primes:
            yield prime
        
        while True:
            yield self._get_next_prime()

    def _get_next_prime(self):
        """
        finds and registers a primes, and returns 
        """
        while True:
            # Now we get the next candidate
            candidate = next(self.candidates)
            limit = math.sqrt(candidate)
            for p in self.get_primes():
                # We loop through primes to check whether the
                # candidate is prime.

                if p > limit:
                    # YES we have a prime number
                    self.primes.append(candidate)
                    return candidate
                elif candidate % p == 0:
                    # NO, candidate is not prime, 
                    # get next candidate
                    break

                # continue with next prime dividor

    def _get_candidates(self):
        """
        Get candidates to be primes.  We start at 7 as primes 2, 3 and 5 are 
        already added and "checked" in the constructor
        """
        n = 0
        while True:
            if n > 0: 
                yield n+1
            yield n+7
            yield n+11
            yield n+13
            yield n+17
            yield n+19
            yield n+23
            yield n+29
            n += 30        
    
if __name__ == "__main__":
    primes = Primes()
    k = 0
    for p in primes.get_primes():
        print(p)
        k += 1
        if k > 10: break

    print (primes.primes)

    for i in [35, 67, 113]:
        print (i, primes.is_prime(i))

    print (primes.primes)
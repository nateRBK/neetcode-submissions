class Solution:
    def climbStairs(self, n: int) -> int:
        #the most amount of steps is n, all ones, one permutation
        #assuming even:
        #the least amount of steps is n/2, all twos. one permutation
        # I could have all ones, save for a two. This reduces the list to 
        #n-1 elements. The number of permutations is now n-1
        #now i have all ones, save for two twos. this reduces the list to 
        #n-2 elements. for every n-2 placement of a two, there is then 
        #n-3 placements for the other two. this means:
        #(n-2)(n-3) permutations. repeating for three twos:
        #(n-3)(n-4)(n-5) permutations. for k twos:
        #(n-k)!/(n-2k)!
        #the max amount of twos is n/2. so when k = n/2:
        # (n/2)!
        # i have not accounted for the fact that each two is identical. so I 
        #need to divide out k! options:
        #(n-k)!/k!(n-2k)!
        #so then the answer would be the sum over k from 0 to n/2. on n = 3:
        #(3-0)!/(0)!(3-0)! + (3-1)!/(1)!(3-2)!
        #3!/3! + 2! = 3. approved. 
        sum = 0
        for k in range(0,n//2+1):
            term1 = math.factorial(n - k)
            term2 = math.factorial(k)
            term3 = math.factorial(n-2*k)
            sum += term1/(term2*term3)
        return int(sum)
def findFirstNumIndex(k, n):
 
    if (n == 1):
        return 0, k
         
    n -= 1
 
    first_num_index = 0
     
    # n_actual_fact = n!
    n_partial_fact = n
 
    while (k >= n_partial_fact and n > 1):
        n_partial_fact = n_partial_fact * (n - 1)
        n -= 1
 
    # First position of the kth sequence
    # will be occupied by the number present
    # at index = k / (n-1)!
    first_num_index = k // n_partial_fact
 
    k = k % n_partial_fact
 
    return first_num_index, k
 
# Function to find the
# kth permutation of n numbers
def findKthPermutation(n, k):
 
    # Store final answer
    ans = ""
 
    s = set()
 
    # Insert all natural number
    # upto n in set
    for i in range(1, n + 1):
        s.add(i)
 
    # Subtract 1 to get 0 based indexing
    k = k - 1
 
    for i in range(n):
 
        # Mark the first position
        itr = list(s)
 
        index, k = findFirstNumIndex(k, n - i)
 
        # itr now points to the
        # number at index in set s
        ans += str(itr[index])
 
        # remove current number from the set
        itr.pop(index)
         
        s = set(itr)
     
    return ans
 
# Driver code
if __name__=='__main__':
 
    n = 3
    k = 4
     
    kth_perm_seq = findKthPermutation(n, k)
 
    print(kth_perm_seq)

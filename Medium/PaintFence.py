# 276(Premium): Paint Fence
# There is a fence with n posts, each post can be painted with one of the k colors.
# You have to paint all the posts such that no more than two adjacent fence posts have the same color.
# Return the total number of ways you can paint the fence.
# Note: n and k are non-negative integers.
# Example: Input: n = 3, k = 2. Output: 6
# Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:
#            post1  post2  post3
# -----      -----  -----  -----
#   1         c1     c1     c2
#   2         c1     c2     c1
#   3         c1     c2     c2
#   4         c2     c1     c1
#   5         c2     c1     c2
#   6         c2     c2     c1

def numWays(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k

    same = k # The 1st fence has k choices, so if the 2nd fence has the same color as 1st, there are k possibilities.
    diff = k * (k-1) # The 1st fence has k choices, so if the 2nd fence has different color as 1st, there are k-1 possibilities.
    for i in range(3, n+1): # If the 3rd one wants to be different, there are k-1 choices, so in total: same*(k-1)+diff*(k-1)
                            # If the 3rd one wants to be the same, the first 2 must be different, then the 3rd one can choose
                            # the same colar as the 2nd one, so: diff*1 = diff
        same,diff = diff,(same+diff)*(k-1)
    return same + diff
# https://www.youtube.com/watch?v=deh7UpSRaEY&ab_channel=MissWright
n = 3
k = 2
print(numWays(n, k))
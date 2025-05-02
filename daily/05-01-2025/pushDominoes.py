"""838. Push Dominoes
Medium

Topics
Companies
There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.

 

Example 1:

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Example 2:


Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
 

Constraints:

n == dominoes.length
1 <= n <= 105
dominoes[i] is either 'L', 'R', or '.'."""
class Solution:
    # need to check the rightmost domino for falling left and leftmost domino for falling right and then iterate in opposite directions
    def pushDominoes(dominoes: str) -> str:
        # every domino right of the first right domino has a rightward force
        def dominoes_fall_right(dominoes: list, i: int) -> list:
            j = dominoes.index(0b10)
            # dominoes fall right until there is a vertical domino between a right falling domino and a left falling domino (j - 1)
            for i in dominoes[i : j - 1]:
                dominoes[i] |= 0b01
            return dominoes
        
        # every domino left of the first left domino as a leftward force
        def dominoes_fall_left(bitmask_dominoes: list, i: int) -> list:
            if bitmask_dominoes[-1 - i] == 0b10:
                for j in range(-1 - i, -len(bitmask_dominoes)-1, -1):
                    bitmask_dominoes[j] |= 0b10
                return bitmask_dominoes
            
        # convert dominoes to a list since str is an immutable type
        dominoes = list(dominoes)
        # bitmask the dominoes to reduce memory usage
        bitmask = {
            '.': 0b00,
            'L': 0b10,
            'R': 0b01
        }
        dominoes = [bitmask[d] for d in dominoes]

        for i in range(len(dominoes)):
            if dominoes[i] == 0b00 and dominoes[-1 - i] == 0b00:
                continue

            if dominoes[i] == 0b01:
                dominoes = dominoes_fall_right(dominoes, i)
            
            if dominoes[-1-i] == 0b10:
                dominoes = dominoes_fall_left(dominoes, i)

                
        n = len(dominoes)
        # check for a L domino to the right
        def check_right(domino: str) -> bool:
            if domino == "." and dominoes[i + 1] == "L":
                return True 
            else: 
                False
        
        # check for a R domino to the left
        def check_left(domino: str) -> bool:
            domino = dominoes[i] 
            if domino == "." and dominoes[-1 - i] == "R":
                return True
            else:
                return False 
            
        for i in range(n):
            domino = dominoes[i]
            # only check the straight up and down dominoes
            if domino != ".":
                continue
            
            # first domino has no domino to the left
            if i == 0:
                right = check_right(domino)
                left = False
            # last domino has no domino to the right 
            elif i == n - 1:
                left = check_left(domino)
                right = False
            # all of the other dominoes have dominos on both sides
            else:
                right = check_right(domino)
                left = check_right(domino)
            
            # if left and right are both falling, the domino stays straight up 
            if left==right:
                continue
            # if the left domino is falling to the right, but the right domino is not falling to the left
            elif left and not right:
                dominoes[i] = "R"
            # if the right domino is falling to the left, but the left domino is not falling to the right
            elif right and not left:
                dominoes[i] = "L"
            
        dominoes = ''.join(dominoes)
        
        return dominoes 

            
                

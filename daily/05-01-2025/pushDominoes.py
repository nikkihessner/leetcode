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
        # convert dominoes to a list since str is an immutable type
        n = len(dominoes)

        if n == 1:
            return dominoes 

        dominoes = list(dominoes)
        
        # bitmask the dominoes to reduce memory usage
        bitmask = {
            '.': 0b00,
            'L': 0b10,
            'R': 0b01
        }
        dominoes = [bitmask[d] for d in dominoes]

        # make copies of dominoes to examine leftward and rightward forces separately
        right = [dominoes[0]]
        left = [dominoes[-1]]

        for i in range(n - 2):
            if dominoes[i + 1] in [0b00, 0b01] and dominoes[i + 2] != 0b10 and right[-1] == 0b01:
                right.append(0b01)
            elif dominoes[i + 1] == 0b00 and right[-1] == 0b00:
                right.append(0b00)
            else:
                right.append(dominoes[i+1])
        
        if dominoes[-2] == 0b01 and dominoes[-1] != 0b10:
            right.append(0b01)
        else:
            right.append(dominoes[-1])

        for i in range(n - 2):
            if dominoes[-2 - i] in [0b00, 0b10] and dominoes[-3 - i] != 0b01 and left[-1] == 0b10:
                left.append(0b10)
            elif dominoes[-2 - i] == 0b00 and left[-1] == 0b00:
                left.append(0b00)
            else:
                left.append(dominoes[-2 - i])
        
        if dominoes[1] == 0b10 and dominoes[0] != 0b01:
            left.append(0b10)
        else:
            left.append(dominoes[0])

        left.reverse()        

        dominoes = [r | l for r, l in zip(right, left)]

        reverse_bitmask = {0b00: '.',
                           0b01: 'R',
                           0b10: 'L',
                           0b11: '.'}
        
        dominoes = [reverse_bitmask[d] for d in dominoes]



        dominoes = ''.join(dominoes)

        return(dominoes)
class Solution:
    # need to check the rightmost domino for falling left and leftmost domino for falling right and then iterate in opposite directions
    @staticmethod
    def pushDominoes(dominoes: str) -> str:
        # convert dominoes to a list since str is an immutable type
        n = len(dominoes)

        # don't eat time and resources when you don't need to
        if n == 1:
            return dominoes 
        
        # make dominoes mutable
        dominoes = list(dominoes)
        
        # bitmask the dominoes to reduce memory usage
        bitmask = {
            '.': 0b00,
            'L': 0b10,
            'R': 0b01
        }
        dominoes = [bitmask[d] for d in dominoes]

        # make copies of dominoes to examine leftward and rightward forces separately and initialize
        right = [dominoes[0]]
        left = [dominoes[-1]]

        # analyze the dominoes falling from left to right
        count = 0
        for i in range(n - 2):
            # check to see if the domino to the right is either a right domino or an upright domino
            # if the domino two to the right is falling left, it will create a condition for an upright domino
            # the last domino in right is the one acting on the rest.
            if dominoes[i + 1] in [0b00, 0b01] and dominoes[i + 2] != 0b10 and right[-1] == 0b01:
                right.append(0b01)
                # the count only counts upright dominos that are affected, so they can be divided between R and L dominos
                if dominoes[i + 1] == 0b00:
                    count +=1
                else:
                    count = 0 
            # accounts for upright dominoes with no forces acting on them
            elif dominoes[i + 1] == 0b00 and right[-1] == 0b00:
                right.append(0b00)
            # accounts for the division of long strings of upright dominoes between an R and a L being split evenly between them
            else:
                right.append(dominoes[i+1])
                if count > 2 and right[-1] != 0b01:
                    shift = count >> 1
                    right[-shift:] = [0b00] * shift

                    if count & 1:
                        right[-shift-1:] = [0b00] * shift
                        right.append(dominoes[i+1])
                    else:
                        right[-shift:] = [0b00] * shift
                
                count = 0
        
        # handle the last domino, since (n-2)
        if right[-1] == 0b01 and dominoes[-1] != 0b10:
            right.append(0b01)
        else:
            right.append(dominoes[-1])

        # same as above, but for left, running through the data right to left
        count = 0
        for i in range(n - 2):
            if dominoes[-2 - i] in [0b00, 0b10] and dominoes[-3 - i] != 0b01 and left[-1] == 0b10:
                left.append(0b10)
                if dominoes[-2 -i] == 0b00:
                    count += 1
                else:
                    count = 0
            elif dominoes[-2 - i] == 0b00 and left[-1] == 0b00:
                left.append(0b00)
            else:
                left.append(dominoes[-2 - i])
                if count > 2 and left[-1] != 0b10:
                    shift = count >> 1
                    left[-shift:] = [0b00] * shift

                    if count & 1:
                        left[-shift-1:] = [0b00] * shift
                        left.append(dominoes[-2 - i])
                    else:
                        left[-shift:] = [0b00] * shift
                
                count = 0
        
        if left[-1] == 0b10 and dominoes[0] != 0b01:
            left.append(0b10)
        else:
            left.append(dominoes[0])

        # reverse
        left.reverse()        

        # compare the two lists with bitwise or to determine which forces are acting on the upright dominoes
        dominoes = [r | l for r, l in zip(right, left)]

        # reverse the bitmask
        reverse_bitmask = {0b00: '.',
                           0b01: 'R',
                           0b10: 'L',
                           0b11: '.'}
        
        dominoes = [reverse_bitmask[d] for d in dominoes]

        # convert back to string
        dominoes = ''.join(dominoes)

        return(dominoes)
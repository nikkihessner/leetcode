from pushDominoes import Solution

def test_pushDominoes_case1():
    assert Solution.pushDominoes(dominoes="RR.L") == "RR.L"

def test_pushDominoes_case2():
    assert Solution.pushDominoes(dominoes=".L.R...LR..L..") == "LL.RR.LLRRLL.."
from pushDominoes import Solution

def test_pushDominoes_case1():
    assert Solution.pushDominoes(dominoes="RR.L") == "RR.L"

def test_pushDominoes_case2():
    assert Solution.pushDominoes(dominoes=".L.R...LR..L..") == "LL.RR.LLRRLL.."

def test_pushDominoes_case3():
    assert Solution.pushDominoes(dominoes=".") == "."

def test_pushDominoes_case4():
    assert Solution.pushDominoes(dominoes="RL") == "RL"

def test_pushDominoes_case5():
    assert Solution.pushDominoes(dominoes="R.") == "RR"

def test_pushDominoes_case6():
    assert Solution.pushDominoes(dominoes=".L") == "LL"

def test_pushDominoes_case7():
    assert Solution.pushDominoes(dominoes=".R") == ".R"

def test_pushDominoes_case8():
    assert Solution.pushDominoes(dominoes="L.") == "L."


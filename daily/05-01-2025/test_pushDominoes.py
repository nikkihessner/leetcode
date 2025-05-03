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

def test_pushDominoes_case9():
    assert Solution.pushDominoes(dominoes="..R..") == "..RRR"

def test_pushDominoes_case10():
    assert Solution.pushDominoes(dominoes="R.......L.R.........") == "RRRR.LLLL.RRRRRRRRRR"

def test_pushDominoes_case11():
    assert Solution.pushDominoes(dominoes="RR..LL") == "RRRLLL"

def test_pushDominoes_case12():
    assert Solution.pushDominoes(dominoes="L.....RR.RL.....L.R.") == "L.....RRRRLLLLLLL.RR"

def test_pushDominoes_case13():
    assert Solution.pushDominoes(dominoes="...RL....R.L.L........RR......L....R.L.....R.L..RL....R....R......R.......................LR.R..L.R.") == "...RL....R.LLL........RRRRRLLLL....R.L.....R.L..RL....RRRRRRRRRRRRRRRRRRRRRRRR.LLLLLLLLLLLLRRRRLL.RR" 

def test_pushDominoes_case14():
    assert Solution.pushDominoes(dominoes="RLLL..LR....LL......LLR.RL...RRL..........R..L....RR.R..L.LR.L...L..LL.R.R.L.RR.....LRL.L.LL..LRR.L.") == "RLLLLLLRRRLLLLLLLLLLLLRRRL...RRL..........RRLL....RRRRRLLLLR.LLLLLLLLL.RRR.L.RRRR.LLLRLLLLLLLLLRR.L."
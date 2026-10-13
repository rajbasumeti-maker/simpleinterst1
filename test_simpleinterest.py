from simpleinetrest import simInt

def test_simpleint_pos():
    assert simInt(1000, 5, 2) == 100.0
def test_simpleInt_zero():
    assert simInt(1000, 5, 0) == 0.0
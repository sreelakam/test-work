import breakdown
def test_breakdown():
    b=breakdown.change(1500)
    assert b==['1000 * 1 = 1000','500 * 1 = 500']

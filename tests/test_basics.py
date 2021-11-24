import core_actions


def test_core():
    m = 10
    res = core_actions.dummy_list(m)
    assert m == 10
    assert len(res) == m + 1
    assert max(res) == m

def test_bla():
    print('bla')

def test_example():
    # Test code goes here
    assert True == True


def test_another_example():
    # Test code goes here
    # why we need approx:
    # x = 0.01
    # for i in range(0, 20):
    #     x += 0.01
    #     print(x)
    assert 1 + 1 == 2

test_another_example()
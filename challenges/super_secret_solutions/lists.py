from super_secret_solutions.testing import test_function, Test

def test(reverse, repeat):
    test_function(reverse, [
        Test('basic', [[1, 2]], [2, 1]),
        Test('empty', [[]], []),
        Test('single', [[1]], [1]),
        Test('long', [[1, 2, 3, 4, 5, 6, 7, 8, 9]], [9, 8, 7, 6, 5, 4, 3, 2, 1])
    ])

    test_function(repeat, [
        Test('basic', [[1, 2], 2], [1, 2, 1, 2]),
        Test('single', [[66, 65], 1], [66, 65]),
        Test('null', [[3, 4, 5], 0], []),
        Test('long', [[1, 2, 3], 10], [1, 2, 3] * 10)
    ])
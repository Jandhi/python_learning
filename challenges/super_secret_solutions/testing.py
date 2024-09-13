class Test:
    def __init__(self, name : str, input : any, expected : any, hide_expected : bool = False) -> None:
        self.name = name
        self.input = input
        self.expected = expected
        self.hide_expected = hide_expected

def test_function(function : callable, tests : list[Test]):
    print('-----')
    print(f'TESTING {function.__name__.upper()}')
    for (i, test) in enumerate(tests):
        test_assert(f'{i}: {test.name}', function(*test.input), '???' if test.hide_expected else test.expected)

def test_assert(name, input, expected):
    if input == expected:
        print(f'test {name} passed ✅')
    else:
        print(f'test {name} failed ❌ (expected {expected}, got {input})')
    

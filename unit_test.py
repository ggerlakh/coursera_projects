class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        for x in 'string', 1.5:
            with self.subTest(i=x):
                self.assertRaises(TypeError, factorize, x)

    def test_negative(self):
        for x in -1, -10, -100:
            with self.subTest(i=x):
                self.assertRaises(ValueError, factorize, x)

    def test_zero_and_one_cases(self):
        for x in 0, 1:
            with self.subTest(i=x):
                self.assertEqual((x,), factorize(x))

    def test_simple_numbers(self):
        for x in 3, 13, 29:
            with self.subTest(i=x):
                self.assertEqual((x,), factorize(x))

    def test_two_simple_multipliers(self):
        for x in 6, 26, 121:
            with self.subTest(i=x):
                self.assertEqual(Factor(x), factorize(x))

    def test_many_multipliers(self):
        for x in 1001, 9699690:
            with self.subTest(i=x):
                self.assertEqual(Factor(x), factorize(x))



def Factor(n):
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        ans.append(n)
    ans.sort()
    return tuple(ans)


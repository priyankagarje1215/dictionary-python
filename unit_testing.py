class DemoTest(unittest.TestCase):

    D1 = {'2020-01-01':4, '2020-01-02':4, '2020-01-03':6}
    D2 = {'2020-01-01':4, '2020-01-02':4, '2020-01-03':6}

    def test_not_so_useful(self):
        assert self.D1 == self.D2

    def test_useful(self):
        self.assertDictEqual(self.D1, self.D2)
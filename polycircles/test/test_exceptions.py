import unittest
from polycircles import polycircles
from nose.tools import raises

class TestExceptions(unittest.TestCase):

    @raises(ValueError)
    def test_less_than_3_vertices_no_1(self):
        polycircle = polycircles.Polycircle(latitude=30,
                                           longitude=30,
                                           radius=100,
                                           number_of_vertices=2)

    @raises(ValueError)
    def test_less_than_3_vertices_no_2(self):
        polycircle = polycircles.Polycircle(latitude=30,
                                           longitude=30,
                                           radius=100,
                                           number_of_vertices=-3)

    @raises(ValueError)
    def test_less_than_3_vertices_no_3(self):
        polycircle = polycircles.Polycircle(latitude=30,
                                           longitude=30,
                                           radius=100,
                                           number_of_vertices=0)



if __name__ == '__main__':
    unittest.main(verbose=2)
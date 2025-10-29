# test_testunit.py

import pytest
from testunit import plus

class TestPlus:
    # ------------------- Happy Path Tests -------------------

    
    def test_plus_two_positive_integers(self):
        """Test adding two positive integers."""
        assert plus(2, 3) == 5

    
    def test_plus_two_negative_integers(self):
        """Test adding two negative integers."""
        assert plus(-4, -6) == -10

    
    def test_plus_positive_and_negative_integer(self):
        """Test adding a positive and a negative integer."""
        assert plus(7, -2) == 5

    
    def test_plus_zero_and_integer(self):
        """Test adding zero and an integer."""
        assert plus(0, 8) == 8
        assert plus(8, 0) == 8

    
    def test_plus_two_floats(self):
        """Test adding two float numbers."""
        assert plus(2.5, 3.1) == pytest.approx(5.6)

    
    def test_plus_integer_and_float(self):
        """Test adding an integer and a float."""
        assert plus(5, 2.5) == pytest.approx(7.5)
        assert plus(2.5, 5) == pytest.approx(7.5)

    
    def test_plus_two_strings(self):
        """Test adding (concatenating) two strings."""
        assert plus("foo", "bar") == "foobar"

    
    def test_plus_two_lists(self):
        """Test adding (concatenating) two lists."""
        assert plus([1, 2], [3, 4]) == [1, 2, 3, 4]

    
    def test_plus_two_tuples(self):
        """Test adding (concatenating) two tuples."""
        assert plus((1, 2), (3, 4)) == (1, 2, 3, 4)

    # ------------------- Edge Case Tests -------------------

    
    def test_plus_large_numbers(self):
        """Test adding very large integers."""
        large1 = 10**100
        large2 = 10**100
        assert plus(large1, large2) == 2 * 10**100

    
    def test_plus_empty_strings(self):
        """Test adding two empty strings."""
        assert plus("", "") == ""

    
    def test_plus_empty_lists(self):
        """Test adding two empty lists."""
        assert plus([], []) == []

    
    def test_plus_empty_tuples(self):
        """Test adding two empty tuples."""
        assert plus((), ()) == ()

    
    def test_plus_string_and_integer_raises_typeerror(self):
        """Test adding a string and an integer raises TypeError."""
        with pytest.raises(TypeError):
            plus("foo", 1)

    
    def test_plus_list_and_tuple_raises_typeerror(self):
        """Test adding a list and a tuple raises TypeError."""
        with pytest.raises(TypeError):
            plus([1, 2], (3, 4))

    
    def test_plus_none_and_integer_raises_typeerror(self):
        """Test adding None and an integer raises TypeError."""
        with pytest.raises(TypeError):
            plus(None, 1)

    
    def test_plus_boolean_and_integer(self):
        """Test adding a boolean and an integer (True is 1, False is 0)."""
        assert plus(True, 2) == 3
        assert plus(False, 2) == 2

    
    def test_plus_boolean_and_boolean(self):
        """Test adding two booleans (should behave as integers)."""
        assert plus(True, False) == 1
        assert plus(True, True) == 2
        assert plus(False, False) == 0

    
    def test_plus_nested_lists(self):
        """Test adding two nested lists."""
        assert plus([[1], [2]], [[3], [4]]) == [[1], [2], [3], [4]]

    
    def test_plus_dicts_raises_typeerror(self):
        """Test adding two dictionaries raises TypeError."""
        with pytest.raises(TypeError):
            plus({'a': 1}, {'b': 2})
            

if __name__ == "__main__":
    pytest.main()
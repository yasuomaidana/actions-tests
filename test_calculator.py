"""Unit tests for calculator module."""

import pytest
from calculator import add, add_multiple


class TestAdd:
    """Test cases for the add function."""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5
        
    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        assert add(-2, -3) == -5
        
    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        assert add(5, -3) == 2
        assert add(-5, 3) == -2
        
    def test_add_zero(self):
        """Test adding zero."""
        assert add(0, 5) == 5
        assert add(5, 0) == 5
        assert add(0, 0) == 0
        
    def test_add_floats(self):
        """Test adding floating point numbers."""
        assert add(2.5, 3.5) == 6.0
        assert add(1.1, 2.2) == pytest.approx(3.3)


class TestAddMultiple:
    """Test cases for the add_multiple function."""
    
    def test_add_multiple_numbers(self):
        """Test adding multiple numbers."""
        assert add_multiple(1, 2, 3, 4, 5) == 15
        
    def test_add_multiple_with_negatives(self):
        """Test adding multiple numbers including negatives."""
        assert add_multiple(10, -5, 3, -2) == 6
        
    def test_add_multiple_single_number(self):
        """Test adding a single number."""
        assert add_multiple(42) == 42
        
    def test_add_multiple_no_numbers(self):
        """Test adding no numbers (empty args)."""
        assert add_multiple() == 0
        
    def test_add_multiple_floats(self):
        """Test adding multiple floating point numbers."""
        assert add_multiple(1.5, 2.5, 3.0) == 7.0

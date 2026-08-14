# test_pivotpulse.py
"""
Tests for PivotPulse module.
"""

import unittest
from pivotpulse import PivotPulse

class TestPivotPulse(unittest.TestCase):
    """Test cases for PivotPulse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PivotPulse()
        self.assertIsInstance(instance, PivotPulse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PivotPulse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

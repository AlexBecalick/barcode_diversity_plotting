"""
Unit tests for the calculation function.
"""

import pytest
import diversity_calculation_funcs

def test_give_answer():
    assert diversity_calculation_funcs.my_data(1, 100, 1, 0)[] == [1, 1]
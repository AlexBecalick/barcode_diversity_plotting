"""
Unit tests for the calculation function.
"""

import pytest
import numpy
import diversity_calculation_funcs as df

def test_barcode_array_generation():
    expected = np.array([[ 1.        ,  1.01005017],
       [ 2.        ,  1.02020134],
       [ 3.        ,  1.03045453],
       [ 4.        ,  1.04081077],
       [ 5.        ,  1.0512711 ],
       [ 6.        ,  1.06183655],
       [ 7.        ,  1.07250818],
       [ 8.        ,  1.08328707],
       [ 9.        ,  1.09417428],
       [10.        ,  1.10517092]])
    actual = list(df.my_data(10, 100, 1, 1))
    
    np.testing.assert_allclose(expected, actual, rtol=1e-06)
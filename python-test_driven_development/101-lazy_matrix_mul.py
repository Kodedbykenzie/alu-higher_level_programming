#!/usr/bin/python3
"""
This module provides a function `lazy_matrix_mul` to multiply two matrices using NumPy.
"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b using NumPy.

    Args:
        m_a (list of lists): First matrix to multiply.
        m_b (list of lists): Second matrix to multiply.

    Returns:
        list of lists: The result of multiplying m_a by m_b.

    Raises:
        TypeError: If m_a or m_b is not a list of lists, or contains non-numeric types.
        ValueError: If m_a or m_b is empty, or if the matrices cannot be multiplied.
    """
    
    # Convert input matrices to NumPy arrays
    try:
        np_a = np.array(m_a, dtype=float)
        np_b = np.array(m_b, dtype=float)
    except Exception as e:
        raise TypeError("m_a and m_b must be lists of lists containing numbers") from e
    
    # Check if the input matrices are non-empty and of correct dimensions
    if np_a.size == 0 or np_b.size == 0:
        raise ValueError("m_a and m_b can't be empty")
    
    # Check if the dimensions of matrices allow for multiplication
    if np_a.shape[1] != np_b.shape[0]:
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = np.matmul(np_a, np_b)
    
    # Convert result to a list of lists
    return result.tolist()


"""
This module provides a function `matrix_mul` to multiply two matrices.

The matrices must be validated before performing multiplication. The function
ensures that the matrices are lists of lists containing only integers or floats,
that they are rectangular (all rows have the same size), and that the matrices
can be multiplied based on their dimensions.
"""

def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b.

    Args:
        m_a (list of lists): First matrix to multiply.
        m_b (list of lists): Second matrix to multiply.

    Returns:
        list of lists: The result of multiplying m_a by m_b.

    Raises:
        TypeError: If m_a or m_b is not a list, list of lists, or contains non-numeric types.
        ValueError: If m_a or m_b is empty, or if the matrices cannot be multiplied.
    """
    
    # Validate m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    
    # Validate m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    
    # Validate m_a and m_b are not empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    
    # Validate that elements in m_a and m_b are integers or floats
    for row in m_a:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("m_b should contain only integers or floats")
    
    # Validate m_a and m_b are rectangular (all rows have the same size)
    row_size_a = len(m_a[0])
    if any(len(row) != row_size_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    row_size_b = len(m_b[0])
    if any(len(row) != row_size_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    
    # Validate m_a and m_b can be multiplied (columns in m_a == rows in m_b)
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            elem_sum = 0
            for k in range(len(m_b)):
                elem_sum += m_a[i][k] * m_b[k][j]
            row.append(elem_sum)
        result.append(row)
    
    return result

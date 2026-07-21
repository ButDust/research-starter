## NumPy Understanding

1. `shape = (3, 4)` means the array has 3 rows and 4 columns.

2. `array_3x4[:, 2]` means selecting all rows and the third column. In NumPy indexing, `:` means all rows, and `2` is the column index because indexing starts from 0.

3. NumPy vectorization is usually faster than a Python for loop because the computation is executed by optimized low-level C/Fortran code. A Python loop handles elements one by one at the Python level, which has more overhead.
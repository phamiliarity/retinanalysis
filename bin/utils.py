#!/usr/bin/python3
"""Functions for printing data in human-readable format

Functions:
    - print_aligned_data: print data in aligned format

"""
def print_aligned_data(data):
    """print data in aligned format

    Args:
        data (list of lists): data to be printed. Nested lists represents a
                              rows of data.

    Returns:
        N/A - function returns nothing.

    Example:
    >>> data = [["idx", "name", "img_path", "mask_path"],
                [0, "stack_01", "stack_01_img.tif", "stack_01_labels.tiff"],
                [1, "this_is_a_long_name", "short", "hello_world"]]
    >>> print_aligned_data(data)

        idx    name                   img_path            mask_path
        0      stack_01               stack_01_img.tif    stack_01_labels.tiff
        1      this_is_a_long_name    short               hello_world

    """
    #calculate custom column widths for input data
    column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]

    for row in data:
        print("    ".join(f"{str(item):<{width}}" for item, width
                          in zip(row, column_widths)))
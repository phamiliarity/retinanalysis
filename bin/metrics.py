#!/usr/bin/python3
"""Functions for ...

Functions:
    - calculate_jaccard: Calculate Jaccard index between two sets of
                         coordinates.

"""
def calculate_jaccard(reference_list, compare_list):
    """Calculate Jaccard index between two sets of coordinates.

    Args:
        reference_list (list): np.array of arrays - coordinates for reference
        compare_list (list): np.array of arrays - coordinates for comparison

    Returns:
        0. list of tuples: Tuples both lists have in common (intersection)
        1. list of tuples: All unique tuples in both lists (union)
        2. list of floats: Jaccard index (intersection/union)
    """
    reference_tuples = list(map(tuple, reference_list))
    compare_tuples = list(map(tuple, compare_list))
    intersection = set(reference_tuples).intersection(set(compare_tuples))
    union = set(reference_tuples).union(set(compare_tuples))
    jaccard = len(intersection) / len(union)
    return intersection, union, jaccard
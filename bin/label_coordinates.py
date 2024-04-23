#!/usr/bin/python3
"""Functions for retrieving information regarding label coordinates.

Functions:
    - get_iplanes: Get planes in which the mask id is present in a 3D matrix
    > used in: 04_find_overlapping_masks_in_Z.ipynb

    - get_mask_px_coords: Get pixel coordinates with specified mask ID in a
                          matrix (2D or 3D).
    > used in: 04_find_overlapping_masks_in_Z.ipynb

    - get_mask_ids_from_coords: Get unique mask IDs from specified pixel
                                coordinates in a 2D matrix
    > used in: 04_find_overlapping_masks_in_Z.ipynb
"""

def get_iplanes(mask_matrix, mask_id):
    """Get planes in which the mask id is present in a 3D matrix

    Args:
        mask_matrix (numpy.ndarray): 3D mask matrix
        mask_id (int): ID of the mask to search for

    Returns:
        list of ints - plane indices where the mask is present, sorted in
                       ascending order
    """
    planes = []
    for iplane in range(mask_matrix.shape[0]):
        if mask_id in mask_matrix[iplane,:,:]:
            planes.append(iplane)
    return sorted(planes)

def get_mask_px_coords(mask_matrix, mask_id):
    """Get pixel coordinates with specified mask ID in a 2D/3D matrix

    Args:
        mask_matrix (numpy.ndarray): mask matrix of one plane or a full stack
            2D shape: nY x nX
            3D shape: nPlanes x nY x nX
        mask_id (int): ID of the mask to retrieve pixel coordinates.

    Returns:
        numpy.ndarray: Array of pixel coordinates where the mask is present
            nested arrays of 2 elements (or 3 if 3D) - 2D: (Y, X)
                                                       3D: (plane id, Y, X)
    """
    mask = copy.deepcopy(mask_matrix)
    mask[~np.isin(mask,[mask_id])] = 0
    return np.transpose(np.nonzero(mask))

def get_mask_ids_from_coords(plane_mask_matrix, px_coords, unique=True):
    """Get unique mask IDs from specified pixel coordinates in a 2D matrix

    Args:
        2d_plane_mask_matrix (numpy.ndarray): 2D mask matrix of a single plane
        px_coords (list): list of pixel coordinates
        unique (bool, optional): if True, retain unique ids;
                                 if False, duplicates are included
                                 Default: True

    Returns:
        list - mask IDs at the specified pixel coordinates.
    """
    mask_ids = np.array([plane_mask_matrix[px_coord[0], px_coord[1]]
                         for px_coord in px_coords])
    mask_ids = list(mask_ids[mask_ids != 0])
    if unique:
        mask_ids = list(np.unique(mask_ids))
    return mask_ids
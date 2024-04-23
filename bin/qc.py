#!/usr/bin/python3
"""Functions for refining masks

Functions:
    - extrapolate_using_intersection: Extrapolates mask data based on intersection info in merge_df.
    - rename_matrix: 

"""
def extrapolate_using_intersection(stack_data, merge_df, verbose=False):
    """Extrapolates mask data based on intersection info in merge_df.

    Args:
        stack_data (object): Stack data containing mask info.
        merge_df (pd.DataFrame): DataFrame with intersection data.
        verbose (bool): If True, prints progress. Default: False.

    Returns:
        np.ndarray - extrapolated mask data.

    """
    if verbose: print(f"{datetime.now()}\tStarted extrapolation")
    for idx, main_mask_id, main_plane_id, overlap_mask_id, overlap_plane_id, \
        _, gap_iplanes in merge_df.itertuples(index=True):

        if verbose: print(f"\r{datetime.now()}"+
                          f"\t{(idx+1)/(merge_df.shape[0]+1)*100:.2f}%"+
                          f"\tProcessing row {idx} / {merge_df.shape[0]}",
                          end="", flush=True)

        mask_matrix = copy.deepcopy(stack_data.mask_matrix)

        #get main pixels
        main_px = get_mask_px_coords(mask_matrix[main_plane_id, :, :],
                                     main_mask_id)

        #get overlap pixels
        overlap_px = get_mask_px_coords(mask_matrix[overlap_plane_id, :, :],
                                        overlap_mask_id)

        #get intersection
        intersection_px, _, _ = calculate_jaccard(main_px, overlap_px)

        # extrapolate
        for gap_iplane in gap_iplanes:
            for x_coord, y_coord in intersection_px:
                mask_matrix[gap_iplane, x_coord, y_coord] = main_mask_id

    if verbose: print(f"\n{datetime.now()}\tFinished extrapolation")
    return mask_matrix

def rename_matrix(mask_matrix, connected_components, verbose=False):
    """Renames labels in the mask matrix based on connected components.

    Args:
        mask_matrix (ndarray): Original mask matrix with label IDs.
        connected_components (list): List of connected components, where each
                                     component is a set of label IDs.
        verbose (bool, optional): If True, prints progress information.
                                  Default: False.

    Returns:
        ndarray: Mask matrix with renamed labels.
    """
    if verbose: print(f"{datetime.now()}\tStarted renaming labels")

    merged_label_matrix = np.copy(mask_matrix)

    for idx, component in enumerate(connected_components, 1):
        first_id = min(component)
        
        if verbose: print(f'\r{datetime.now()}\t{idx}/{len(connected_components)}\tnew id: {first_id}, old ids: {component}', end="", flush=True)

        merged_label_matrix[np.isin(merged_label_matrix, list(component))] = first_id

    if verbose: print(f"\n{datetime.now()}\tFinished renaming labels")
    return merged_label_matrix
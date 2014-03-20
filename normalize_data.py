# Sebastian Raschka, 03/2014

def normalize_val(x, data_list):
    """
    Normalizes a value to a data list returning a float
    between 0.0 and 1.0. 
    Returns the original object if value is not a integer or float.
    
    """
    if isinstance(x, float) or isinstance(x, int):
        numerator = x - min(data_list)
        denominator = max(data_list) - min(data_list)
        return numerator/denominator
    else:
        return x

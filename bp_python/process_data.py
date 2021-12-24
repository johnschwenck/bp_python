# SBP Adjustment Helper Function
def process_helper_sbp_adj():
    x

# Process Data Function
def process_data(data, sbp = None):
    """
    \nData Pre-Processor\n

    A helper function to assist in pre-processing the user-supplied
    input data into a standardized format for use with other functions 
    in the bp_python package.\n

    data: User-supplied dataset containing blood pressure data. Must
    contain data for Systolic blood pressure and Diastolic blood pressure at a
    minimum.\n

    sbp: Required column name (character string) corresponding to Systolic Blood
    Pressure (mmHg)
    """
    
    if data is None:
        print("here")

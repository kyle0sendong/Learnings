
""" Guido's Gorgeous Lasagna
    Learn the basics of Python by cooking Guido's Gorgeous Lasagna.
"""
EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """ Returns baking time remaining
    This function takes one number that represents the time the lasagna has been
    baking and subtracts the expected bake time
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
def preparation_time_in_minutes(number_of_layers):
    """ Returns additional time in minutes depending on layer """
    preparation_time = number_of_layers * 2
    return preparation_time
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """ Returns the minutes remaining plus the number of layers """
    elapsed_time = (number_of_layers * 2) + elapsed_bake_time
    return elapsed_time
    
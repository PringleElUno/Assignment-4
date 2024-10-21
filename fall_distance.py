# Author: Luis Pringle
# GitHub username: PringleElUno
# Date: 10/21/2024
# Define a formula that is used to determine the distance an object falls due to gravity in a specfic time period.

def fall_distance (time):
    """
    Calculate the distance an object falls due to gravity in a specific time period.

    Parameters:
    time (float): the time in seconds that it takes for the object to fall.

    Returns:
    float: the distance in meters the object has to fall.
    """

    # Gravity equals 9.8
    gravity = 9.8

    # Caculate the distance using the formula, (1/2) * gravty * time^2
    distance = 1/2 * gravity * time^2

    # Round the distance to three decimal places
    distance = round(distance, 3)
    # Returns the value of fall_distance rounded to the third decimal point
    return distance
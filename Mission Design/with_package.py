import numpy as np
from datetime import datetime
from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris, get_body


def hohmann_transfer(departure_date_str, arrival_date_str, planet1_str,
                     planet2_str):
    # Input validation could go here.

    # Parse date strings
    departure_date = Time(departure_date_str, format='iso', scale='tdb')
    arrival_date = Time(arrival_date_str, format='iso', scale='tdb')

    # Use Astropy to get planet data
    with solar_system_ephemeris.set('builtin'):
        planet1 = get_body(planet1_str, departure_date)
        planet2 = get_body(planet2_str, arrival_date)

    r1 = planet1.radius.to('km').value
    r2 = planet2.radius.to('km').value

    # Using the sun's gravitational parameter - can update if needed
    mu_sun = 1.327e11

    # Rest of the Hohmann transfer calculation as before... (see previous response for this part of the code)
    # Convert dates to Julian dates
    dep_jd = departure_date.toordinal() + 1721425.5
    arr_jd = arrival_date.toordinal() + 1721425.5

    # Semi-major axis of transfer orbit
    a_trans = (r1 + r2) / 2

    # Calculate velocities at departure and arrival points
    v1 = np.sqrt(mu_sun * ((2 / r1) - (1 / a_trans)))
    v2 = np.sqrt(mu_sun * ((2 / r2) - (1 / a_trans)))

    # Calculate delta-v for each burn
    delta_v1 = v1 - np.sqrt(mu_sun / r1)
    delta_v2 = np.sqrt(mu_sun / r2) - v2

    # Time of flight (half the period of the transfer orbit)
    tof = np.pi * np.sqrt(a_trans ** 3 / mu_sun)
    tof_days = tof / 86400  # Convert seconds to days

    # Check for validity of transfer window
    if tof_days > (arr_jd - dep_jd):
        print(
            'Arrival date is not reachable within the calculated transfer window')

    return delta_v1, delta_v2, tof_days

# Example usage
departure_date_str = input("Enter departure date (YYYY-MM-DD): ")
arrival_date_str = input("Enter arrival date (YYYY-MM-DD): ")
planet1_str = input("Enter departure planet (e.g., Earth): ")
planet2_str = input("Enter arrival planet (e.g., Mars): ")

delta_v1, delta_v2, tof = hohmann_transfer(departure_date_str, arrival_date_str,
                                           planet1_str, planet2_str)

print("Delta-v for the first burn:", delta_v1, "km/s")
print("Delta-v for the second burn:", delta_v2, "km/s")
print("Time of flight:", tof, "days")
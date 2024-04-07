import numpy as np
from datetime import datetime


def hohmann_transfer(departure_date, arrival_date, r1, r2, mu_sun):
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


# Example usage: Earth to Mars transfer
# Departure date and arrival date
departure_date = datetime(2024, 11, 15)
arrival_date = datetime(2025, 8, 20)

# Orbital radii (in km) - you will need to update this for the planets of interest
r1 = 149.6e6  # Earth's orbital radius
r2 = 227.9e6  # Mars' orbital radius

# Standard gravitational parameter of the Sun (km^3/s^2)
mu_sun = 1.327e11

delta_v1, delta_v2, tof_days = hohmann_transfer(departure_date, arrival_date,
                                                r1, r2, mu_sun)

print("Delta-v for the first burn:", delta_v1, "km/s")
print("Delta-v for the second burn:", delta_v2, "km/s")
print("Time of flight:", tof_days, "days")
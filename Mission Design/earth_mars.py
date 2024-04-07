# Poliastro requires Python 3.8 - 3.10

from poliastro.bodies import Earth
from poliastro.bodies import Mars
from poliastro.twobody import Orbit
from poliastro.maneuver import Maneuver
from astropy import units as u


# Assume a circular parking orbit around Earth (modify as needed)
earth_orbit = Orbit.circular(Earth, alt=500*u.km)

# Target Mars orbit
mars_orbit = Orbit.circular(Mars, alt=500*u.km)

# Compute Hohmann transfer using poliastro
maneuver = Maneuver.hohmann(earth_orbit, mars_orbit)

# Extract delta-v and time of flight
delta_v = maneuver.get_total_cost()
time_of_flight = maneuver.get_total_time().to(u.day)

print("Delta-V:", delta_v)
print("Time of Flight:", time_of_flight)

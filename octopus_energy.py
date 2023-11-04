# coding: utf8
import datetime
import operator
import requests

from OctopusAgile import Agile
from octopus_energy_api import oe_api

STANDING_CHARGE_URL = ("https://api.octopus.energy/v1/products/AGILE-FLEX-22"
                       "-11-25/electricity-tariffs/E-1R-AGILE-FLEX-22-11-25"
                       "-N/standing-charges/")
SHEETY_PUT = ""

account_number = ""
api_key = ""
mpan = ""
serial_number = ""

energy_api = oe_api(account_number,
                    api_key,
                    mpan=mpan,
                    serial_number=serial_number)

# Get consumption, standing charge, and cost per day
for i in range(1, 0, -1):
    # Get starting date with next date
    day_before = i
    day_after = i - 1
    start_day = datetime.date.today() - datetime.timedelta(days=day_before)
    end_day = datetime.date.today() - datetime.timedelta(days=day_after)

    # Get standing charge per day
    params = {
        "period_from": start_day,
        "period_to": end_day
    }
    r = requests.get(url=STANDING_CHARGE_URL, params=params)
    standing_charge_dict = r.json()
    standing_charge = round(standing_charge_dict["results"][0][
                                "value_inc_vat"], 2)

    # Using package to get consumption rate
    c = energy_api.consumption(start_day, end_day)
    consumption_rate = [sub['consumption'] for sub in c]
    consumption_day = sum(consumption_rate)

    # Using another package to retrieve rates
    agile = Agile('N')  # N is the region code for Southern Scotland
    rate = agile.get_rates(start_day, end_day)['rate_list']
    rate.reverse()

    # Create list of per half hour consumption multiplied respective rate
    result = list(map(operator.mul, consumption_rate, rate))
    cost = round(sum(result)) / 100
    cost_string = f"£{cost}"
    cost_per_unit = f"£{round(cost / consumption_day, 2)}"
    # print(today)
    # print(cost)

    # Send data to Google Sheets
    json = {
        "octopus": {
            "date": str(start_day),
            "consumption": str(consumption_day),
            "standingCharge": str(standing_charge),
            "cost": cost_string,
            "costPerKWh": cost_per_unit,
        }
    }
    upload_to_sheet = requests.post(url=SHEETY_PUT, json=json)
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
    consumption_day = round(sum(consumption_rate), 3)

    # Using another package to retrieve rates
    agile = Agile('N')  # N is the region code for Southern Scotland
    rate = agile.get_rates(start_day, end_day)['rate_list']
    rate.reverse()

    # Create list of per half hour consumption multiplied respective rate
    result = list(map(operator.mul, consumption_rate, rate))
    cost = round(sum(result)) / 100
    cost_string = f"£{cost}"
    cost_per_unit = f"£{round(cost / consumption_day, 2)}"

    # Consumption, price, cost per half hour
    half_hour = list()
    if len(consumption_rate) == 49 or len(consumption_rate) == 51:
        len_cr = len(consumption_rate) - 1
    else:
        len_cr = len(consumption_rate)
    for c in range(len_cr):
        r = round(result[c], 3)
        half_hour.append((f"{consumption_rate[c]} kWh x {rate[c]} p/kWh ="
                          f" {r}p"))

    # Set up half hour segments
    dt = datetime.datetime.strptime("00:00", "%H:%M")
    half_hour_time = list()
    for n in half_hour:
        next_dt = dt + datetime.timedelta(minutes=30)
        half_hour_time.append(
            "{:02d}:{:02d}{:02d}:{:02d}"
            .format(dt.hour, dt.minute,
                    next_dt.hour, next_dt.minute))
        dt = next_dt
    if len(half_hour) == 50:  # For BST adjustment
        half_hour_time[48] = "24:0024:30"
        half_hour_time[49] = "24:3025:00"

    # New month adjustment
    new_sheet_name = (calendar.month_name[start_day.month].lower()[0:3]
                      + str(start_day.year)[2:])

    # Create json to send data
    json = {
        new_sheet_name: {
            "date": str(start_day),
            "consumption": str(consumption_day),
            "standingCharge": str(standing_charge),
            "cost": cost_string,
            "costPerKWh": cost_per_unit,
        }
    }
    for data in range(len(half_hour)):
        json[new_sheet_name][half_hour_time[data]] = half_hour[data]

    # Send data to Google Sheets
    sheety_put = (f"https://api.sheety.co/3dbfe1f109be8ab861bbb4646c950d9c"
                  f"/octopusEnergyCostAgile/{new_sheet_name}")
    upload_to_sheet = requests.post(url=sheety_put, json=json)

    # print(len(half_hour))
    # print(half_hour)
    # print(len(half_hour_time))
    # print(half_hour_time)
    # print(len(rate))
    # print(rate)
    # print(len(consumption_rate))
    # print(start_day)
    # print(cost)
    # print(json)
    # print(len(json["octopus"]))

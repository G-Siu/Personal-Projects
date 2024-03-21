def calculate_hourly_rate_scotland():
    salary = float(input("Please enter your annual salary: "))
    location = input("Are you based in Scotland? (yes/no): ")

    if location.lower() == "yes":
        personal_allowance = 12570
        tax_free_amount = personal_allowance
        basic_rate_band = 2306
        intermediate_rate_band = 11685
        higher_rate_band = 17101
        additional_rate_band = 31338

        taxable_income = salary - tax_free_amount

        if taxable_income <= 0:
            tax = 0
        else:
            tax = 0
            if taxable_income <= basic_rate_band:
                tax += (taxable_income * 0.19)
            else:
                tax += (basic_rate_band * 0.19)
                taxable_income -= basic_rate_band

            if taxable_income <= intermediate_rate_band:
                tax += (taxable_income * 0.20)
            else:
                tax += (intermediate_rate_band * 0.20)
                taxable_income -= intermediate_rate_band

            if taxable_income <= higher_rate_band:
                tax += (taxable_income * 0.21)
            else:
                tax += (higher_rate_band * 0.21)
                taxable_income -= higher_rate_band

            if taxable_income <= additional_rate_band:
                tax += (taxable_income * 0.42)
            else:
                tax += (additional_rate_band * 0.42)
                taxable_income -= additional_rate_band

            tax += (taxable_income * 0.45)

        mandatory_deductions = 0.12  # 12% of salary goes towards National Insurance

        # Calculate hourly rate before tax and deductions
        hourly_rate_before_tax = salary / (40 * 52)

        # Calculate hourly rate after tax and deductions
        hourly_rate_after_tax = (salary / (40 * (52 - 5.6)) * (1 - tax/salary)) * (1 - mandatory_deductions)

        # Calculate gross hourly rate
        gross_hourly_rate = hourly_rate_before_tax

        print(f"Your gross hourly rate in Scotland is: {gross_hourly_rate}")
        print(f"Your net hourly rate in Scotland after tax is: {hourly_rate_after_tax}")

    else:
        print("This script is only designed for Scotland.")


calculate_hourly_rate_scotland()

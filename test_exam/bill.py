def calculate_telephone_bill(tier, minutes):
    tier_rates = {
        "Tier1": 0.1,
        "Tier2": 0.08,
        "Tier3": 0.06
    }

    if tier in tier_rates:
        rate = tier_rates[tier]
        total_cost = rate * minutes
        return f"Your {tier} bill for {minutes} minutes is ${total_cost:.2f}"
    else:
        return "Invalid tier."


tier = "Tier2"
minutes = 200
print(calculate_telephone_bill(tier, minutes))

# Define the pricing tiers
tier1_limit = 100  # Tier 1 limit in minutes
tier1_rate = 1  # Tier 1 rate per minute

tier2_limit = 200  # Tier 2 limit in minutes
tier2_rate = 0.8  # Tier 2 rate per minute

tier3_rate = 0.5  # Tier 3 rate per minute (applies after tier2_limit)

# Input: Minutes used by the customer
minutes_used = int(input("Enter the number of minutes used: "))

# Calculate the bill based on tiers
if minutes_used <= tier1_limit:
    total_bill = minutes_used * tier1_rate
elif minutes_used <= tier2_limit:
    total_bill = (tier1_limit * tier1_rate) + \
        ((minutes_used - tier1_limit) * tier2_rate)
else:
    total_bill = (tier1_limit * tier1_rate) + ((tier2_limit - tier1_limit)
                                               * tier2_rate) + ((minutes_used - tier2_limit) * tier3_rate)

# Display the total bill amount
print("Total Bill Amount: ${:.2f}".format(total_bill))

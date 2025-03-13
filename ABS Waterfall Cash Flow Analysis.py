import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set pandas display option to show all columns
pd.set_option('display.max_columns', None)

# -------------------------------
# Define ABS structure (Tranches)
# -------------------------------
tranches_def = [
    {"name": "Senior", "initial_balance": 100.0, "coupon": 0.05, "priority": 1},
    {"name": "Mezzanine", "initial_balance": 50.0, "coupon": 0.08, "priority": 2},
    {"name": "Junior", "initial_balance": 30.0, "coupon": 0.12, "priority": 3},
]

# Helper function: Reset tranches with initial balances
def reset_tranches():
    tranches = []
    for t in tranches_def:
        new_t = t.copy()
        new_t["balance"] = new_t["initial_balance"]
        tranches.append(new_t)
    return tranches

# -------------------------------
# Simulation Parameters
# -------------------------------
max_periods = 10              # Maximum number of periods to simulate
cash_flow_per_period = 30.0   # Asset pool cash available each period
cash_flows = [cash_flow_per_period] * max_periods

# -------------------------------
# Waterfall Simulation: Record Payment Schedule
# -------------------------------
waterfall_records = []
tranches = reset_tranches()

for period in range(1, max_periods + 1):
    period_record = {"Period": period, "AssetPoolCash": cash_flow_per_period}
    available_cash = cash_flow_per_period
    
    # Step 1: Pay Interest in order of priority
    for tranche in sorted(tranches, key=lambda x: x["priority"]):
        interest_due = tranche["balance"] * tranche["coupon"] if tranche["balance"] > 0 else 0.0
        interest_paid = min(available_cash, interest_due)
        available_cash -= interest_paid
        
        period_record[f"{tranche['name']}_Interest_Due"] = interest_due
        period_record[f"{tranche['name']}_Interest_Paid"] = interest_paid

    # Step 2: Pay Principal in order of priority
    for tranche in sorted(tranches, key=lambda x: x["priority"]):
        principal_due = tranche["balance"] if tranche["balance"] > 0 else 0.0
        principal_paid = min(available_cash, principal_due)
        tranche["balance"] -= principal_paid
        available_cash -= principal_paid
        
        period_record[f"{tranche['name']}_Principal_Paid"] = principal_paid
        period_record[f"{tranche['name']}_Remaining_Balance"] = tranche["balance"]

    # Check if all tranches are repaid
    total_balance = sum(t["balance"] for t in tranches)
    if total_balance < 1e-6:
        # All tranches repaid: capture any leftover cash as a Residual Distribution
        period_record["Residual_Distribution"] = available_cash
        period_record["Cash_Unused"] = 0.0
        period_record["All_Tranches_Paid"] = True
        # For clarity, force all balances to zero
        for tranche in tranches:
            tranche["balance"] = 0.0
        waterfall_records.append(period_record)
        break  # Stop simulation once all tranches are fully repaid
    else:
        period_record["Residual_Distribution"] = 0.0
        period_record["Cash_Unused"] = available_cash
        period_record["All_Tranches_Paid"] = False
        waterfall_records.append(period_record)

# Convert records to DataFrame and display results
df_waterfall = pd.DataFrame(waterfall_records)
print("ABS Cash Flow Waterfall Payment Schedule:")
print(df_waterfall)

# -------------------------------
# Plot Tranche Balance Over Time
# -------------------------------
balance_history = {t["name"]: [] for t in tranches_def}

# Reset tranches for balance history simulation
tranches = reset_tranches()
periods_simulated = []

for period in range(1, max_periods + 1):
    available_cash = cash_flow_per_period

    # Process interest (does not affect principal)
    for tranche in sorted(tranches, key=lambda x: x["priority"]):
        interest_due = tranche["balance"] * tranche["coupon"] if tranche["balance"] > 0 else 0.0
        interest_paid = min(available_cash, interest_due)
        available_cash -= interest_paid

    # Process principal payments and record remaining balance
    for tranche in sorted(tranches, key=lambda x: x["priority"]):
        principal_due = tranche["balance"] if tranche["balance"] > 0 else 0.0
        principal_paid = min(available_cash, principal_due)
        tranche["balance"] -= principal_paid
        available_cash -= principal_paid
        balance_history[tranche["name"]].append(tranche["balance"])
    periods_simulated.append(period)
    
    if sum(t["balance"] for t in tranches) < 1e-6:
        break

plt.figure(figsize=(10, 6))
for tranche_name, history in balance_history.items():
    plt.plot(periods_simulated[:len(history)], history, marker='o', label=tranche_name)
plt.xlabel("Period")
plt.ylabel("Remaining Balance")
plt.title("ABS Tranche Balance Over Time")
plt.legend()
plt.grid(True)
plt.show()




"""Beginner exercise: analyse a small fictional price dataset.

This script uses invented values for learning. It does not fetch live prices,
connect to an exchange, or make trading recommendations.
"""

from statistics import mean

# Fictional example values, not real market data.
sample_prices = [100.0, 102.0, 99.0, 103.0, 101.0, 104.0]

print("Fictional sample price analysis")
print(f"Number of observations: {len(sample_prices)}")
print(f"Average value: {mean(sample_prices):.2f}")
print(f"Lowest value: {min(sample_prices):.2f}")
print(f"Highest value: {max(sample_prices):.2f}")

change = sample_prices[-1] - sample_prices[0]
percentage_change = (change / sample_prices[0]) * 100

print(f"Change from first to last observation: {change:.2f}")
print(f"Percentage change: {percentage_change:.2f}%")

print("\nReminder: a small historical or fictional sample cannot predict future prices.")

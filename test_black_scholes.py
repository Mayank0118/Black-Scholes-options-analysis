from src.black_scholes import (
    calculate_d1,
    calculate_d2,
    call_price,
    put_price
)


# ==========================================
# Input Parameters
# ==========================================

S = 2500
K = 2500
T = 1.0
r = 0.06
sigma = 0.20


# ==========================================
# Calculate d1 and d2
# ==========================================

d1 = calculate_d1(S, K, T, r, sigma)
d2 = calculate_d2(d1, T, sigma)


# ==========================================
# Calculate Option Prices
# ==========================================

call = call_price(S, K, T, r, sigma)
put = put_price(S, K, T, r, sigma)


# ==========================================
# Display Results
# ==========================================

print("\nBlack-Scholes Option Pricing")
print("=" * 35)

print(f"Spot Price       : ₹{S:.2f}")
print(f"Strike Price     : ₹{K:.2f}")
print(f"Time to Maturity : {T:.2f} years")
print(f"Risk-Free Rate   : {r * 100:.2f}%")
print(f"Volatility       : {sigma * 100:.2f}%")

print("-" * 35)

print(f"d1               : {d1:.6f}")
print(f"d2               : {d2:.6f}")

print("-" * 35)

print(f"European Call    : ₹{call:.2f}")
print(f"European Put     : ₹{put:.2f}")
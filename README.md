# Black-Scholes Options Pricing & Risk Analysis

## Project Overview

This project implements the Black-Scholes model for pricing European call and put options and analyzes how option prices and risk measures change with important market parameters.

The project combines mathematical finance, Python programming, sensitivity analysis, visualization, and historical market data to build a complete options pricing analysis workflow.

---

## Objectives

The main objectives of this project are:

- Implement the Black-Scholes option pricing model in Python.
- Calculate theoretical prices for European call and put options.
- Calculate major option Greeks.
- Validate the model using Put-Call Parity.
- Analyze option price sensitivity to:
  - Underlying asset price
  - Volatility
  - Strike price
  - Time to maturity
- Use historical market data to estimate volatility.
- Apply market-derived inputs to the Black-Scholes model.
- Visualize pricing and risk relationships.
- Build a reusable Python pricing engine.

---

## Technologies Used

- Python
- NumPy
- SciPy
- Pandas
- Matplotlib
- Seaborn
- yfinance
- Jupyter Notebook

---

## Project Structure

```text
black-scholes-options-analysis/
│
├── data/
│   ├── spot_price_sensitivity.csv
│   ├── volatility_sensitivity.csv
│   ├── strike_price_sensitivity.csv
│   ├── maturity_sensitivity.csv
│   └── reliance_historical_data.csv
│
├── notebooks/
│   └── black_scholes_analysis.ipynb
│
├── src/
│   └── black_scholes.py
│
├── visualization/
│   └── charts/
│       ├── 01_option_prices_vs_spot.png
│       ├── 02_call_delta_vs_spot.png
│       ├── 03_gamma_vs_spot.png
│       ├── 04_option_prices_vs_volatility.png
│       ├── 05_vega_vs_volatility.png
│       ├── 06_option_prices_vs_strike.png
│       ├── 07_option_prices_vs_maturity.png
│       ├── 08_reliance_historical_price.png
│       └── 09_reliance_return_distribution.png
│
├── test_black_scholes.py
├── requirements.txt
└── README.md

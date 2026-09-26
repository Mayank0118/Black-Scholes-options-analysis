import numpy as np
from scipy.stats import norm


def validate_inputs(S, K, T, r, sigma):
    """
    Validate Black-Scholes model inputs.

    Parameters
    ----------
    S : float
        Spot price of the underlying asset.
    K : float
        Strike price of the option.
    T : float
        Time to maturity in years.
    r : float
        Risk-free interest rate as a decimal.
    sigma : float
        Volatility as a decimal.
    """

    if S <= 0:
        raise ValueError("Spot price S must be greater than 0.")

    if K <= 0:
        raise ValueError("Strike price K must be greater than 0.")

    if T <= 0:
        raise ValueError("Time to maturity T must be greater than 0.")

    if sigma <= 0:
        raise ValueError("Volatility sigma must be greater than 0.")


def calculate_d1(S, K, T, r, sigma):
    """
    Calculate d1.
    """

    validate_inputs(S, K, T, r, sigma)

    d1 = (
        np.log(S / K)
        + (r + 0.5 * sigma**2) * T
    ) / (sigma * np.sqrt(T))

    return d1


def calculate_d2(d1, T, sigma):
    """
    Calculate d2.
    """

    d2 = d1 - sigma * np.sqrt(T)

    return d2


def call_price(S, K, T, r, sigma):
    """
    Calculate European Call option price.
    """

    d1 = calculate_d1(S, K, T, r, sigma)
    d2 = calculate_d2(d1, T, sigma)

    call = (
        S * norm.cdf(d1)
        - K * np.exp(-r * T) * norm.cdf(d2)
    )

    return call


def put_price(S, K, T, r, sigma):
    """
    Calculate European Put option price.
    """

    d1 = calculate_d1(S, K, T, r, sigma)
    d2 = calculate_d2(d1, T, sigma)

    put = (
        K * np.exp(-r * T) * norm.cdf(-d2)
        - S * norm.cdf(-d1)
    )

    return put


# ============================================================
# OPTION GREEKS
# ============================================================

def delta(S, K, T, r, sigma, option_type="call"):
    """
    Calculate Delta.

    Call Delta = N(d1)
    Put Delta  = N(d1) - 1
    """

    d1 = calculate_d1(S, K, T, r, sigma)

    if option_type.lower() == "call":
        return norm.cdf(d1)

    elif option_type.lower() == "put":
        return norm.cdf(d1) - 1

    else:
        raise ValueError("option_type must be 'call' or 'put'.")


def gamma(S, K, T, r, sigma):
    """
    Calculate Gamma.

    Gamma is the same for Call and Put options.
    """

    d1 = calculate_d1(S, K, T, r, sigma)

    gamma_value = (
        norm.pdf(d1)
        / (S * sigma * np.sqrt(T))
    )

    return gamma_value


def vega(S, K, T, r, sigma):
    """
    Calculate Vega.

    Measures sensitivity of option price
    to a change in volatility.
    """

    d1 = calculate_d1(S, K, T, r, sigma)

    vega_value = (
        S
        * norm.pdf(d1)
        * np.sqrt(T)
    )

    return vega_value


def theta(S, K, T, r, sigma, option_type="call"):
    """
    Calculate Theta.

    Theta represents the change in option price
    for one day decrease in time to maturity.

    The result is expressed per day.
    """

    d1 = calculate_d1(S, K, T, r, sigma)
    d2 = calculate_d2(d1, T, sigma)

    first_term = (
        -S
        * norm.pdf(d1)
        * sigma
        / (2 * np.sqrt(T))
    )

    if option_type.lower() == "call":

        second_term = (
            -r
            * K
            * np.exp(-r * T)
            * norm.cdf(d2)
        )

        theta_value = first_term + second_term

    elif option_type.lower() == "put":

        second_term = (
            r
            * K
            * np.exp(-r * T)
            * norm.cdf(-d2)
        )

        theta_value = first_term + second_term

    else:
        raise ValueError("option_type must be 'call' or 'put'.")

    # Convert annual Theta to daily Theta
    return theta_value / 365


def rho(S, K, T, r, sigma, option_type="call"):
    """
    Calculate Rho.

    Measures sensitivity of option price
    to a change in the risk-free interest rate.

    Rho is expressed per 1.00 change in interest rate.
    """

    d1 = calculate_d1(S, K, T, r, sigma)
    d2 = calculate_d2(d1, T, sigma)

    if option_type.lower() == "call":

        rho_value = (
            K
            * T
            * np.exp(-r * T)
            * norm.cdf(d2)
        )

    elif option_type.lower() == "put":

        rho_value = (
            -K
            * T
            * np.exp(-r * T)
            * norm.cdf(-d2)
        )

    else:
        raise ValueError("option_type must be 'call' or 'put'.")

    return rho_value


# ============================================================
# COMPLETE OPTION ANALYSIS
# ============================================================

def option_analysis(S, K, T, r, sigma):
    """
    Calculate option prices and Greeks
    for both Call and Put options.

    Returns
    -------
    dict
        Dictionary containing prices and Greeks.
    """

    return {
        "call_price": call_price(S, K, T, r, sigma),
        "put_price": put_price(S, K, T, r, sigma),

        "call_delta": delta(
            S, K, T, r, sigma, "call"
        ),

        "put_delta": delta(
            S, K, T, r, sigma, "put"
        ),

        "gamma": gamma(
            S, K, T, r, sigma
        ),

        "vega": vega(
            S, K, T, r, sigma
        ),

        "call_theta": theta(
            S, K, T, r, sigma, "call"
        ),

        "put_theta": theta(
            S, K, T, r, sigma, "put"
        ),

        "call_rho": rho(
            S, K, T, r, sigma, "call"
        ),

        "put_rho": rho(
            S, K, T, r, sigma, "put"
        )
    }
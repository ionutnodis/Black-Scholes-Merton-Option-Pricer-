

""""
Black Scholes Merton Option Pricing Model for both European Call and Put Options using 3D Surface Plot in Streamlit

"""



import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import streamlit as st
from mpl_toolkits.mplot3d import Axes3D

# Black-Scholes-Merton Model
def black_scholes_merton(S, K, T, r, sigma):
    """
    Calculate European Call and Put Pption prices using Black-Scholes-Merton formula.

    The function takes the following input Parameters:

        S (float): Spot price of the underlying asset
        K (float): Strike price 
        T (float): Time to maturity (in years)
        r (float): Risk-free interest rate (annualized)
        sigma (float): Volatility of the underlying asset (annualized)

    And outputs the prices of European Call and Put Option according to the Black-Scholes-Merton Model.
 
    """
    
     # We compute d1 and d2 
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)


    # We then compute the call and put prices using the Black Scholes Merton formula
    
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    return call_price, put_price

#  We construct an interface using Streamlit to interact with the model and visualize the 3D surface plots 

def main():
    st.title("European Option Pricing: Surface Plots for Call and Put Prices")

     # User Inputs for Model Parameters
    st.sidebar.header("Model Parameters")
    T = st.sidebar.number_input("Time to Maturity (T in years)", value=1.0, step=0.1)
    r = st.sidebar.number_input("Risk-Free Rate (r in %)", value=5.0, step=0.1) / 100
    sigma = st.sidebar.number_input("Volatility (σ in %)", value=20.0, step=0.1) / 100
    spot_min = st.sidebar.slider("Minimum Spot Price (S)", min_value=10, max_value=200, value=50)
    spot_max = st.sidebar.slider("Maximum Spot Price (S)", min_value=10, max_value=200, value=150)
    strike_min = st.sidebar.slider("Minimum Strike Price (K)", min_value=10, max_value=200, value=50)
    strike_max = st.sidebar.slider("Maximum Strike Price (K)", min_value=10, max_value=200, value=150)

    # Create grid for spot prices and strike prices
    spot_prices = np.linspace(spot_min, spot_max, 50)
    strike_prices = np.linspace(strike_min, strike_max, 50)
    S, K = np.meshgrid(spot_prices, strike_prices)

    # Calculate call and put prices
    call_prices = np.zeros_like(S)
    put_prices = np.zeros_like(S)

    for i in range(S.shape[0]):
        for j in range(S.shape[1]):
            call_prices[i, j], put_prices[i, j] = black_scholes_merton(S[i, j], K[i, j], T, r, sigma)

    # Plot 3D surface for Call Prices
    fig = plt.figure(figsize=(20, 10))  # Increased figure size for better display
    ax1 = fig.add_subplot(121, projection='3d')
    surf1 = ax1.plot_surface(S, K, call_prices, cmap='viridis', edgecolor='none')
    ax1.set_title("Call Prices Surface", fontsize=16)
    ax1.set_xlabel("Spot Price (S)", fontsize=12)
    ax1.set_ylabel("Strike Price (K)", fontsize=12)
    ax1.set_zlabel("Call Price", fontsize=12)
    fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=10)

    # Plot 3D surface for Put Prices
    ax2 = fig.add_subplot(122, projection='3d')
    surf2 = ax2.plot_surface(S, K, put_prices, cmap='plasma', edgecolor='none')
    ax2.set_title("Put Prices Surface", fontsize=16)
    ax2.set_xlabel("Spot Price (S)", fontsize=12)
    ax2.set_ylabel("Strike Price (K)", fontsize=12)
    ax2.set_zlabel("Put Price", fontsize=12)
    fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=10)

    plt.tight_layout()

    st.pyplot(fig)

if __name__ == "__main__":
    main()
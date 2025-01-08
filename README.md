# Black-Scholes-Merton Option Pricing Model with 3D Surface Visualization


This project implements the Black-Scholes-Merton Option Pricing Model for pricing European Call and Put Options. Using Streamlit, it provides an interactive interface for calculating option prices and visualizing them on 3D surface plots.

# Features:

	•	Calculate the prices of European Call and Put Options.
	•	Inputs include Spot Price (S), Strike Price (K), Time to Maturity (T), Risk-Free Rate (r), and Volatility (σ).
	•	Adjust parameters in real-time using sliders and input fields.
	•	Two side-by-side 3D surface plots for Call and Put prices.
	•	Spot Price (S) and Strike Price (K) are plotted on the x and y axes, while the option price is represented on the z-axis.

# Installation

## Prerequisites

Ensure you have Python 3.7 or later installed along with the following libraries:

	•	numpy
	•	matplotlib
	•	scipy
	•	streamlit

## Steps

1. Clone this repository or copy the code to your local environment:

* git clone <(https://github.com/ionutnodis/Black-Scholes-Merton-Option-Pricer-/tree/main)>


2. Install the required libraries:

* pip install -r requirements.txt

Or install them individually:	
* pip install numpy matplotlib scipy streamlit


3. Run the Streamlit app:

* streamlit run bs_option_pricing.py

4. Open the provided URL (default: http://localhost:8501) in your browser.

# Usage

1. 	Start the App:
	•	Run the Streamlit app using the command:

		streamlit run bs_option_pricing.py


2. Input Parameters:

	•	Use the sidebar to input the following parameters:
	•	Time to Maturity (T): Time remaining until the option expires (in years).
	•	Risk-Free Rate (r): Annualized risk-free interest rate (percentage).
	•	Volatility (σ): Annualized standard deviation of the asset’s returns (percentage).
	•	Spot Price Range (S): Minimum and maximum spot prices for the x-axis.
	•	Strike Price Range (K): Minimum and maximum strike prices for the y-axis.

3.	View Results:

	•	The app generates two 3D surface plots:
	•	Call Prices Surface: The Call Option prices for the given parameter ranges.
	•	Put Prices Surface: Shows the Put Option prices for the given parameter ranges.
	
4.	Analyze the Outputs:

	•	Adjust the input parameters to update the plots dynamically.

## Code Overview

The black_scholes_merton function calculates the Call and Put prices using the Black-Scholes-Merton formula:

    def black_scholes_merton(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

     call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    return call_price, put_price

## Visualization

The main function handles user input and generates two 3D surface plots for Call and Put prices.

Input Parameters:

    •	Time to Maturity (T): 1 year
	•	Risk-Free Rate (r): 5%
	•	Volatility (σ): 20%
	•	Spot Price Range (S): 50 to 150
	•	Strike Price Range (K): 50 to 150

Visual Output

The app generates two 3D plots:

1. Call Prices Surface
2. Put Prices Surface
 
# License

This project is licensed under the MIT License. See the LICENSE file for details.

# Author

Developed by Ionut Catalin Nodis. If you have any questions or suggestions, feel free to reach out!

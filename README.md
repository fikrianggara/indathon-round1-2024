# Indathon Round1 Solution

This repo contain solution for Indathon, a data hackathon held by Statistics Indonesia (BPS) in collaboration with others ministry and Australian Bureau of Statistics (ABS).
the challenge is to create a prediction model with minimum RMSE to predict numbers of Transjakarta Passengers based on past passengers data and some auxiliary data.
We use SARIMAX to build the prediction model.

### Used Package

- `pandas==V2.2.2` (Data processing)
- `numpy==1.26.4` (Data processing)
- `matplotlib==3.9.1` (Data plot)
- `statsmodels==0.14.2` (Modelling)
- `scikit-learn==1.5.1` (Model Evaluation)

### How to Run it?

You can use code in `main.py`, there's main function named `forecast_and_save_to_csv` which do the forecast and save the prediction in given filename to .csv file.
this function require :

- `forecast_m`, an integer representing how far do we want to forecast in months. e.g 6 means the model will predict the next 6 months after the start date
- `start_date`, a datetime representing the starting date of forecast.
- `filename`, a string representing the output filename

### Script

usable code can be found in `main.py`. There are functions that I use to do the forecast, starts from importing data, transform, modelling and forecasting.
Each function has their documentation. There's also `main.ipynb` notebook that I use to explore and analysing the data and the model.

### Resource used

The data input takes about 2.7KB of memory

### Total Execution Time

Total Execution Time from importing the required package until exporting the data is about 10 seconds.

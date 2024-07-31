# Indathon Round1 Solution

### Used Package

- `pandas==V2.2.2` (Data processing)
- `numpy==1.26.4` (Data processing)
- `matplotlib==3.9.1` (Data plot)
- `statsmodels==0.14.2` (Modelling)
- `scikit-learn==1.5.1` (Model Evaluation)

### How to Run it?

You can use code in main.py, there's main function named `forecast_and_save_to_csv` which do the forecast and save the prediction in given filename.
this function require :

- `forecast_m`, an integer representing how far do we want to forecast in months. e.g 6 means the model will predict the next 6 months after the start date
- `start_date`, a datetime representing the starting date of forecast.
- `filename`, a string representing the output filename

### Script

usable code can be found in `main.py`. There are functions that I used to do the forecasting start from importing data, transform, modelling and forecasting.
there's also documentation of each function. There's also `main.ipynb` notebook that I use to explore and analysing the data and the model.

### Resource used

the data input used about 2.7KB of memory

### Total Execution Time

Total Execution Time from importing the required package until exporting the data is about 10 seconds.

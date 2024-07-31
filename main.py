import numpy as np
import pandas as pd
from datetime import datetime
from statsmodels.tsa.statespace.sarimax import SARIMAX
import numpy as np


def add_date_column(data, year_col, month_col, day_col):
    """function to add date column
        args
        - data, a dataframe
        - year_col_name, a string of year column name
        - month_col_name, a string of month column name
        - day_col_name, a string of day column name
    """
    data['date'] = pd.to_datetime(data[[year_col, month_col, day_col]])
    return data


def add_dummy_covid(row, covid_start=datetime(2020, 3, 1), covid_end=datetime(2023, 5, 1)):
    """function to add dummy column for covid
        args
        - data, a dataframe
        - covid_start, a datetime
        - covid_end, a datetime
    """
    if row['date'] < covid_start or row['date'] > covid_end :
        val = 0
    else:
        val = 1
    return val


def set_date_as_index(data, date_col_name):
    """function to set date as index
        args
        - data, a dataframe
        - date_col_name, a string of date column name
    """
    data.set_index(date_col_name, inplace=True)
    return


def create_model(target_col_train, exog):
    """function to create model, return model.fit() from SARIMAX object
        args 
        - target_col_train, a one dimensional dataframe of target column values that has date as the index;
        - exog, a dataframe of exogenous variable values that has date as the index
    """
    model = SARIMAX(target_col_train, exog=exog, order=(1, 1, 1), seasonal_order=(1, 1, 1, 6))
    return model.fit()


def forecast(model, forecast_steps, exog):
    """function to forecast forecast_steps amount
        args
        - model, a SARIMAX object
        - forecast_steps, an integer of forecast steps
        - exog, a dataframe of exogenous variable values that has date as the index
    """
    forecast = model.get_forecast(steps=forecast_steps, exog=exog)
    return forecast


def create_output_df(predictions):
    """function that return dataframe of predicted values which has the same form as submission.csv data
        args
        - predictions, a prediction object from SARIMAX.get_forecast
    """
    res = {
        'id':np.arange(1, len(predictions.predicted_mean) + 1),
        'jumlah_penumpang': predictions.predicted_mean,
    }
    df = pd.DataFrame(res)
    df.index = np.arange(1, len(predictions.predicted_mean) + 1)
    return df


def save_to_csv(df, filename):
    """function to save dataframe to csv
        args
        - df, a dataframe
        - filename, a string of filename
    """
    df.to_csv(filename, sep=',',index=False)
    print('prediction saved to csv file: {}'.format(filename))


def forecast_and_save_to_csv(forecast_m, start_date, filename):
    """main function
        args
        - forecast_m, an integer of forecast steps in months
        - start_date, a starting date of datetime
        - filename, a string of filename
    """
    df = pd.read_csv('data/training_jumlah_penumpang_tj.csv', sep=';')
    df = df.assign(hari=1)
    df = add_date_column(df, 'tahun', 'bulan', 'hari')
    df['covid_dummy'] = df.apply(add_dummy_covid, axis=1)
    set_date_as_index(df, 'date')

    target_col_train = df['jumlah_penumpang']
    exog = df[['covid_dummy']]
    model = create_model(target_col_train, exog)

    prediction_exog = pd.DataFrame({
        'covid_dummy': [0 for x in range(0, forecast_m)]
    })

    end_date = start_date + pd.DateOffset(months=forecast_m)
    date_range = pd.date_range(start_date, end_date, freq='M')
    prediction_exog.set_index(date_range, inplace=True)

    predictions = forecast(model, forecast_m, prediction_exog['covid_dummy'])

    df = create_output_df(predictions)
    
    save_to_csv(df, filename)

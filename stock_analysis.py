# -----------------------------------------------
# Author        = Yan Ying (Eliza)
# Date          = 19/05/2022
# File name     = stock_analysis.py
# Description   = read data from MySQL database and draw a K-line chart
# -----------------------------------------------
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import mplfinance as mpf


def read_data(host, user, password, db, table):
    """
    read table we want from the database in MySQL
    :param host: the host address of MySQL that you connect
    :param user: the username of MySQL that you connect
    :param password: the password of MySQL that you connect
    :param db: the database name that you want to create and store data
    :param table: the table name that you want to create and store data
    :return: stock data within the half year
    """
    # connect to the database
    engine = create_engine('mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(user, quote_plus(password), host, db))

    # select stock data needed to draw graph during the previous half year
    read_all_sql = "SELECT dates, open_price, close_price, low, high, vol FROM {} WHERE" \
                   " dates BETWEEN date_sub(now(), interval 6 month) AND now();".format(table)
    stock_data = pd.read_sql(read_all_sql, engine)
    stock_data.columns = ["date", "open", "close", "low", "high", "volume"]
    stock_data.index = pd.DatetimeIndex(stock_data["date"])

    return stock_data


def line_chart(stock_data):
    """
    draw the K line chart
    :param stock_data: pre-processed data used to draw graph
    :return: no return, but the plot will be shown in an outer window
    """
    defined_color = mpf.make_marketcolors(
        up='red',  # close > open to be red
        down='green',  # close < open to be green
        edge='inherit',
        wick='i',  # top and bottom lines inherit color of rectangle
        volume={'up': 'red', 'down': 'green'},  # set color of volume the same as that of rectangle above
        ohlc='i'
    )
    defined_style = mpf.make_mpf_style(
        marketcolors=defined_color,  # set colors to be what I defined, and mpf.available_styles() can check all options
        gridaxis='both',  # show both vertical and horizontal grid lines
        gridstyle='-.',  # set grid-style behind
        rc={'font.family': 'STSong'}  # set to show Chinese characters
    )

    # plot the K line chart
    mpf.plot(
        stock_data,
        type='candle',  # graph type, options are ['ohlc','candle','line','renko','pnf']
        title='中金公司(601995)股票市场近半年的股价走势K线图',  # set the title of chart
        ylabel='股价(元)',  # set the y label
        style=defined_style,  # apply the style defined above
        show_nontrading=False,  # not show non-trading date
        volume=True,  # show volume on the graph
        ylabel_lower='成交量(股)',  # set the y label of volume part
        datetime_format='%Y-%m-%d',  # set the format of x label
        xrotation=30,  # set the rotation degree of x label
        tight_layout=False,  # not display tightly

        # if you want to save the chart to local device, add this line (uncomment the below line)
        # savefig="601995_K_line_chart.png"
        # savefig="601995_K_line_chart.pdf"
    )
    mpf.show()


if __name__ == "__main__":
    # you need to use your own host, user_name, and password of your MySQL
    # and choose the names of database and table that you want to read data
    host_name = 'localhost'
    user_name = 'root'
    password_str = '******'  # This is not the real password.
    db_name = 'stock_schema'
    table_name = 'stock'

    # read data from MySQL database and draw a K-line chart
    data = read_data(host_name, user_name, password_str, db_name, table_name)
    print(data)
    line_chart(data)

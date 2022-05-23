# -----------------------------------------------
# Author        = Yan Ying (Eliza)
# Date          = 19/05/2022
# File name     = store_stock_data.py
# Description   = store stock data to MySQL database
# -----------------------------------------------
import pymysql
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import Date, BIGINT, FLOAT
from urllib.parse import quote_plus


def create_table(host, user, password, db, table):
    """
    connect to Mysql database and create a schema and table
    :param host: the host address of MySQL that you connect
    :param user: the username of MySQL that you connect
    :param password: the password of MySQL that you connect
    :param db: the database name that you want to create and store data
    :param table: the table name that you want to create and store data
    :return: no return
    """

    # connect to MySQL and create the database
    connection = pymysql.connect(host=host, user=user, password=password)
    mysql_cur = connection.cursor()
    mysql_cur.execute("CREATE DATABASE if not exists {}".format(db))
    mysql_cur.close()
    connection.commit()
    connection.close()

    # create the table in the database
    db_connection = pymysql.connect(host=host, user=user, password=password, db=db)
    db_cur = db_connection.cursor()
    db_cur.execute('CREATE TABLE if not exists {}( \
                    dates DATE NOT NULL, \
                    open_price FLOAT(2), \
                    close_price FLOAT(2), \
                    previous_close FLOAT(2), \
                    low FLOAT(2), \
                    high FLOAT(2), \
                    vol BIGINT, \
                    amount FLOAT(2), \
                    PRIMARY KEY(dates) \
                    )'.format(table)
                   )
    db_cur.close()
    db_connection.commit()
    db_connection.close()


def write_data(host, user, password, db, table):
    """
    write data from csv file to corresponding db and table in MySQL
    :param host: the host address of MySQL that you connect
    :param user: the username of MySQL that you connect
    :param password: the password of MySQL that you connect
    :param db: the target database to store data
    :param table: the target table to store data
    :return: no return
    """

    # read data wanted from the local csv file
    data = pd.read_csv("stock.csv", encoding="gbk")
    stock_data = pd.DataFrame(
        {
            "dates": data["日期"],
            "open_price": data["开盘价"],
            "close_price": data["收盘价"],
            "previous_close": data["前收盘"],
            "low": data["最低价"],
            "high": data["最高价"],
            "vol": data["成交量"],
            "amount": data["成交金额"]
        }
    )
    stock_data = stock_data.set_index("dates")

    # store pd.DataFrame to certain database and table in MySQL
    engine = create_engine('mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(user, quote_plus(password), host, db))
    type_dict = {"dates": Date, "open_price": FLOAT(2), "close_price": FLOAT(2), "previous_close": FLOAT(2),
                 "low": FLOAT(2), "high": FLOAT(2), "vol": BIGINT, "amount": FLOAT(2)}
    stock_data.to_sql(name=table, con=engine, if_exists='append', dtype=type_dict)


if __name__ == "__main__":
    # you need to use your own host, user_name, and password of your MySQL
    # and choose the names of database and table that you want to create for storing data
    host_name = 'localhost'
    user_name = 'root'
    password_str = '******'  # This is not the real password.
    db_name = 'stock_schema'
    table_name = 'stock'

    # create table and write data to the table
    create_table(host_name, user_name, password_str, db_name, table_name)
    write_data(host_name, user_name, password_str, db_name, table_name)

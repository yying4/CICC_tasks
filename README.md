# Task 1: Python and SQL

## stock.csv
It stores the stock information of CICC within the recent half year

## create_table_stock.sql
This is the SQL to create the table named "stock"

## store_stock_data.py
* The file is to read data from stock.csv and create a database and table in the localhost MySQL to store required data.
* The file cannot be executed successfully on your computer because you need to download the MySQL Workbench on your 
local computer and change the root information in this script including host, user, and password to your own.
* To run this Python script, use `python store_stock_data.py` in the terminal

## stock_analysis.py
* This file is to draw K line chart by reading the stock data stored in MySQL database according to the requirement.
* The file cannot be executed successfully on your computer because you need to download the MySQL Workbench on your 
local computer and change the root information in this script including host, user, and password to your own.
* To run this Python script, use `python stock_analysis.py` in the terminal

## 601995_K_line_chart.pdf
* This is the K line chart of stock information within the recent 6 months for CICC (601995). 
* I stored this chart as 
a PDF file is to keep its clarity. If you want to download a PNG or JPG file, you can uncomment one line in the 
`mpf.plot()` in stock_analysis.py and then run it again.

# Task 2: PPT
## Analysis.pptx
It is the original PPT for analysis of domestic public offering fund and overseas mutual fund

## Analysis.pdf
* the same content with Analysis.pptx. 
* I saved another PDF file to avoid some possible display errors due to 
different software versions or computer versions.
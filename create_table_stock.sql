CREATE TABLE stock(
	dates DATE NOT NULL,
	open_price FLOAT(2),
    close_price FLOAT(2),
    previous_close FLOAT(2),
    low FLOAT(2),
    high FLOAT(2),
    vol INT,
    amount FLOAT(2),
    PRIMARY KEY(dates)
)
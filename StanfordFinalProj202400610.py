# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 08:57:26 2024
The file "20240610Symbols.csv" is downloaded from the SEC.gov site and contains a latest month valid list of stock symbols, cusips and descriptions.

This python solution requires the installation of the Yahoo finance library and a valid internet connection in order to retrieve latest
stock prices.

@author: Samuel Brooks
"""

import sys
import csv
import yfinance as yf

FILE_PATH = "20240610Symbols.csv"

dictionary = {}

def import_dictionary_from_csv(FILE_PATH):
        
    with open(FILE_PATH, 'r', newline='', encoding="utf8") as csvfile:
        csv_reader = csv.reader(csvfile)
        #skip the header
        next(csv_reader)
        for row in csv_reader:
            if len(row) ==3:
                symbol, cusip, description = row
                dictionary[symbol] = [cusip, description]
    return dictionary

def get_symbol_from_user(dictionary):

    while True:
        user_input = input("Enter a valid stock symbol or type 'quit' to exit: ").strip().upper()
        
        if user_input == "QUIT":
            return user_input
            break
        
        elif user_input in dictionary:
            return user_input
            break
        else:
            print("Invalid symbol. Please input a valid symbol.")
            

def get_latest_closing_price(symbol):
    stock = yf.Ticker(symbol)
    hist = stock.history(period="1d")
    if not hist.empty:
        latest_date = hist.index[-1].strftime("%Y-%m-%d")
        latest_close = hist['Close'][-1]
        return latest_date, latest_close
    else:
        return None, None

    
def main():
    dictionary = import_dictionary_from_csv(FILE_PATH)
    print("dictionary loaded")
    
    symbol = get_symbol_from_user(dictionary)
    if symbol == "QUIT":
        print("Application quitting: user entered 'quit'")
        sys.exit()
        
    else:
    
        latest_date, latest_close = get_latest_closing_price(symbol)
        if latest_date and latest_close:
            print(f"The latest closing price for {dictionary[symbol][1]} on {latest_date} was ${latest_close:.2f}.")
            
        else:
            print("No dice")


if __name__ == "__main__":
    main()
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os 

DB_NAME = "golf_data.db"
CSV_PATH = "Data_centric_programming"


def main():
    
    select = 0

    while select != 4:
        print('\n====Main menu=====')
        print('\n Select an option')
        print ('\n\n 1.Inspect Data')
        print('\n\n 2.Insert Data')
        print('\n\n 3.Graph Data')
        print('\n\n 4.Quit')
        print('\n+++++++++++++++++++')
    
        try:
            select = int(input("choose an option: "))
        except ValueError:
            print("Please enter a valid number")
            continue
    
    if (select == 1):
        {   

        }

    elif(select == 2):
        {

        }

    elif(select == 3):
        {

        }

    elif(select == 4):
        {

        }

    else:
        {
        print("you have selected an invalid option")
        }       

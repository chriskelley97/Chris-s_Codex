##Christopher Kelley
##Automatidata

#Build dataframe
import pandas as pd
import numpy as np

df = pd.read_csv(' 2017_Yellow_Taxi_Trip_Data.csv ')
print(' done ')

#head of csv file 
df.head()

#info of csv file
df.info()

#describe of csv file
df.descibe()


#Sort the data by maximum to minimum value
df_sort = df.sort_value(by = [' trip_distance '], ascending = False)
#Sort the head 
df_sort.head() 

#Sort the data by total amount and print the top 20 values
total_amount_sorted = df.sort_values([' total_amount '], ascending = False)[' total_amount ']
#Print only head 
total_amount_sorted.head()

#Sort the data by total amount and print the bottom
total_amount_sorted.tail()

#Count of each payment types represented in the data
df[' payment_type '].value_counts()

#Average tip fopr trips paid for with credit card
avg_cc_tip = df[df[' payment type '] == 1][' tip_amount '].mean()
print(' Average credit card tip: ', avg_cc_tip)

#Average tip for trips paid for with cash
avg_cash_tip = df[df[' payment_type '] == 2][' tip_amount '].mean()
print(' Average cash tip: ', avg_cash_tip)

#Count times each vendor ID is represented in the data
df[' VendorID '].value_counts()

#Mean total amount for each vendor
df.groupby([' VendorID ']).mean(numeric_only = True)[[' total_amount ']]

#Filter the data for credit card payments only
credit_card = df[df[' payment_type '] == 1]
#Filter the data for passenger count only
credit_card[' passenger_count ' ].value_counts()

#Calculate the average tip amount for each passenger count (only credit card)
credit_card.groupby([' passenger_count ']).mean(numeric_only = True)[[' tip_amount ']]

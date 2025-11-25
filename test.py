# I created a Empty List to store all the stock data such as prices and ticker symbol
stock_data = {}


#Name of Stock
Stockname_str = input("Stock Ticker: ")

#Asks for input of Stock price throguhout the week
Stockprice1_float = input("What is the price of the stock on 1? ")
Stockprice2_float = input("What is the price of the stock on 2? ")
Stockprice3_float = input("What is the price of the stock on 3? ")
Stockprice4_float = input("What is the price of the stock on 4? ")
Stockprice5_float = input("What is the price of the stock on 5? ")
Stockprice6_float = input("What is the price of the stock on 6? ")
Stockprice7_float = input("What is the price of the stock on 7? ")

#Sets the inputs to floats and sets them to a variable
Stockprice1 = float(Stockprice1_float)
Stockprice2 = float(Stockprice2_float)
Stockprice3 = float(Stockprice3_float)
Stockprice4 = float(Stockprice4_float)
Stockprice5 = float(Stockprice5_float)
Stockprice6 = float(Stockprice6_float)
Stockprice7 = float(Stockprice7_float)

#Function for Daily Average Returns ( Calculates daily_average_returns)
def daily_average_return(Stockprice1, Stockprice2, Stockprice3, Stockprice4, Stockprice5, Stockprice6, Stockprice7):
        
        #Calculates the Day-to-Day Returns
        day_Return1 = (Stockprice1 - Stockprice1)/Stockprice1
        day_Return2 = (Stockprice2 - Stockprice1)/Stockprice1
        day_Return3 = (Stockprice3 - Stockprice2)/Stockprice2
        day_Return4 = (Stockprice4 - Stockprice3)/Stockprice3
        day_Return5 = (Stockprice5 - Stockprice4)/Stockprice4
        day_Return6 = (Stockprice6 - Stockprice5)/Stockprice5
        day_Return7 = (Stockprice7 - Stockprice6)/Stockprice6

        #Finds the Aveerage Return for the Week
        Average_Return1 = (day_Return1 + day_Return2 + day_Return3 + day_Return4 + day_Return5 + day_Return6 + day_Return7)/6
        return Average_Return1

#Sets the prices for each day to the Stock Name
stock_data[Stockname_str] = Stockprice1_float, Stockprice2_float, Stockprice3_float, Stockprice4_float, Stockprice5_float, Stockprice6_float, Stockprice7_float

#For Rounding
Average_Return2 = daily_average_return(Stockprice1, Stockprice2, Stockprice3, Stockprice4, Stockprice5, Stockprice6, Stockprice7)

#Rounding Average_Return
rounded_dailyAverageReturns = round(Average_Return2, 3)


print(f"The stock price for {Stockname_str} every day of the week was {stock_data[Stockname_str]} ")
print("The average return for the week is: " + str(rounded_dailyAverageReturns))
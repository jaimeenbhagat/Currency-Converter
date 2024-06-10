from tkinter import *
import requests
import json

t = Tk()

# create a global variables
var1 = StringVar(t)
var2 = StringVar(t)

# initialise the variables
var1.set("currency")
var2.set("currency")

	
# Function to perform real time conversion
# from one currency to another currency
def RealTimeCurrencyConversion():


	# currency code
	from_currency = var1.get()
	to_currency = var2.get()

	
	# main_url variable store complete url
	main_url = "https://api.exchangerate-api.com/v4/latest/INR"

	# get method of requests module
	# return response object
	req_ob = requests.get(main_url)

	# json method converts json data type
	#into python dictionary data type
	
	# result contains list of nested dictionaries
	result = req_ob.json()

	# parsing the required information
	Exchange_Rate = float(result["rates"][0]["INR"])

	# get method of Entry widget
	# returns current text as a
	# string from text entry box.
	amount = float(Amount1_field.get())

	# calculation for the conversion
	new_amount = round(amount * Exchange_Rate, 3)

	# insert method inserting the
	# value in the text entry box.
	Amount2_field.insert(0, str(new_amount))


# Function for clearing the Entry field
def clear_all():
    Amount1_field.delete(0, END)
    Amount2_field.delete(0, END)
	

# Driver code
if __name__ == "__main__" :

	# Set the background colour of GUI window
	t.configure(background = 'light green')
	
	# Set the configuration of GUI window (WidthxHeight)
	t.geometry("400x175")
	
	# Create "welcome to Real Time Currency Convertor" label
	headlabel = Label(t, text = 'welcome to Real Time Currency Convertor',
					fg = 'black', bg = "red")

	# Create a "Amount :" label
	label1 = Label(t, text = "Amount :",
				fg = 'black', bg = 'dark green')
	
	# Create a "From Currency :" label
	label2 = Label(t, text = "From Currency",
				fg = 'black', bg = 'dark green')
	
	# Create a "To Currency: " label
	label3 = Label(t, text = "To Currency :",
				fg = 'black', bg = 'dark green')

	# Create a "Converted Amount :" label
	label4 = Label(t, text = "Converted Amount :",
				fg = 'black', bg = 'dark green')

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure.
	headlabel.grid(row = 0, column = 1)
	label1.grid(row = 1, column = 0)
	label2.grid(row = 2, column = 0)
	label3.grid(row = 3, column = 0)
	label4.grid(row = 5, column = 0)
	
	# Create a text entry box
	# for filling or typing the information.
	Amount1_field = Entry(t)
	Amount2_field = Entry(t)
	
	# ipadx keyword argument set width of entry space.
	Amount1_field.grid(row = 1, column = 1, ipadx ="25")
	Amount2_field.grid(row = 5, column = 1, ipadx ="25")

	# list of currency codes
	CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]

	# create a drop down menu using OptionMenu function
	# which takes window name, variable and choices as
	# an argument. use * before the name of the list,
	# to unpack the values
	FromCurrency_option = OptionMenu(t, var1, *CurrenyCode_list)
	ToCurrency_option = OptionMenu(t, var2, *CurrenyCode_list)
	
	FromCurrency_option.grid(row = 2, column = 1, ipadx = 10)
	ToCurrency_option.grid(row = 3, column = 1, ipadx = 10)
	
	# Create a Convert Button and attach
	# with RealTimeCurrencyExchangeRate function
	button1 = Button(t, text = "Convert", bg = "red", fg = "black",
								command = RealTimeCurrencyConversion)
	
	button1.grid(row = 4, column = 1)

	# Create a Clear Button and attach
	# with delete function
	button2 = Button(t, text = "Clear", bg = "red",
					fg = "black", command = clear_all)
	button2.grid(row = 6, column = 1)
	
	# Start the GUI
	t.mainloop()

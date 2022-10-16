from pricechart import Chart as chartXD
from Finance import finance

from os import system

system('clear')

        # Author @TanmayXD

ch = int(input("INPUT 1 FOR PRICE CLOSING CHART GENERATOR\n-> "))



if ch == 1:
    asset = input("ENTER SYMBOL -> ")
    start = input("ENTER START DATE IN YYYY-MM-DD -> ")
    end = input("ENTER END DATE YYYY-MM-DD -> ")

    userInput = chartXD(asset= asset, start_date= start, end_date= end)
    chartXD.closingPrice(userInput)
    
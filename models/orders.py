from models.order import *
from datetime import datetime 

now = datetime.now()
date_time = now.strftime('%d/%m/%Y, %H:%M:%S')
# date1 = datetime.datetime(2022, 11, 2)
# date2 = datetime.datetime(2022, 11, 1)
# date3 = datetime.datetime(2022, 10, 30)

order1 = Order("George", date_time, 1, 'Crunchie')
order2 = Order("Luis", date_time, 2, 'Apple')
order3 = Order("Struan", date_time, 3, 'Chomp')

orders = [order1, order2, order3]
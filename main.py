# import smtplib
#
# my_email = 'sayfpython@gmail.com'
# password = 'eczdjtweziojlsgd'
#
# with smtplib.SMTP('smtp.gmail.com') as connection:
# 	connection.starttls()
# 	connection.login(user=my_email, password=password)
# 	connection.sendmail(from_addr=my_email, to_addrs='sayfgani@hotmail.com',
# 	msg='Subject: Anotha Banga\n\n Sent this from Pycharm hehehe')

# import datetime as dt
#
# now = dt.datetime.now()
# print(now.year)
# print(now.hour)
#
# day_of_week = now.weekday()
# print(day_of_week+1)
#
# date_of_birth=dt.datetime(year=1992,month=3,day=22, hour=12,minute=49)
# print(date_of_birth)

import datetime as dt
import random
import smtplib

current_date = dt.datetime.now()
current_day= current_date.weekday()
print(current_day)
current_day= 0

if current_day == 0:
	with open('quotes.txt') as file:
		quotes_list = list(file)

	chosen_quote = random.choice(quotes_list)
	print(chosen_quote)

	my_email = 'sayfpython@gmail.com'
	password = 'eczdjtweziojlsgd'

	with smtplib.SMTP('smtp.gmail.com') as connection:
		connection.starttls()
		connection.login(user=my_email, password=password)
		connection.sendmail(from_addr=my_email, to_addrs='sayfgani@hotmail.com',
		msg=f'Subject: Motivational Quote\n\n Today is Monday, here is your motivational quote \n\n {chosen_quote}')

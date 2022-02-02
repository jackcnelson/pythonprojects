# MIS 207 HW04 Q2

# This program predicts the total revenue for the next 100 days of a store based on previous data

import random

days = 100
total_revenue = 0

while days > 0:
    total_revenue += random.uniform(31956, 48345)
    days -= 1

print(f'The total estimated revenue after 100 days is: ${total_revenue: ,.2f}.')

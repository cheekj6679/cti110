# Tutorial on projected sales
# 22 June 20
# CTI-110 P2T1 - Sales Prediction
# Joshua Cheek
#
# Get projected total sales
total_sales = float(input('Enter the projected sales: '))

# Calculate profit as 23% of total sales
profit = total_sales * 0.23

# Display profit
print('The profit is $', format(profit, ',.2f'))

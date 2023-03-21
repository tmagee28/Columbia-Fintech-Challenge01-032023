# %%
import csv
from pathlib import Path


# %%
loan_costs = [500, 600, 200, 1000, 450]

# %%
length_of_loan_costs = len(loan_costs)
sum_of_loan_costs = sum(loan_costs)
avg_loan_cost = sum_of_loan_costs / length_of_loan_costs
print(f'there are {length_of_loan_costs} loans')
print(f'the value of all loans is {sum_of_loan_costs}')
print(f'the average value of a loan is {avg_loan_cost}')


# %%
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000}

# %%
future_value = loan.get('future_value')
remaining_months = loan.get('remaining_months')

print(f'The future value is {future_value}')
print(f'There are {remaining_months} months remaining')

# %%
discount_rate = 0.20
present_value = future_value / (1 + discount_rate/12) ** remaining_months

print(f'The present value it {present_value}')


# %%
loan_price = loan.get('loan_price')

if present_value >= loan_price:
    print('The loan is worth at least the cost to but it')
else:
    print('The present value of the loan is less than the cost')



# %%
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000}

# %%
def present_value_calculator(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + annual_discount_rate/12) ** remaining_months
    return(present_value)


# %%
discount_rate = 0.20
future_value = new_loan.get('future_value')
remaining_months = new_loan.get('remaining_months')
loan_price = new_loan.get('loan_price')

present_value = present_value_calculator(future_value, remaining_months, discount_rate)
print(f'The present value of the loan is: {present_value}')

# %%

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]


# %%
inexpensive_loans = []

for i in loans:
    loan_price = i.get('loan_price')
    if loan_price >= 500:
        print(f'The loan price is greater than or equal to 500')
    else:
        print(f'The loan price is less than 500')
    


# %%
inexpensive_loans = []
for i in loans:
    loan_price = i.get('loan_price')
    if loan_price <= 500:
        inexpensive_loans.append(i)

print(inexpensive_loans)



# %%
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]
inexpensive_loans_csv = Path("inexpensive_loans.csv")
with open(inexpensive_loans_csv,'w', newline='') as file:
    writer = csv.writer(file)
    writer = writer.writerow(header)
    for row in inexpensive_loans:
        writer.writerows(row.values())




    



# %%




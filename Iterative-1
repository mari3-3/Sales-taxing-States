sales_tax_rate_nj = 0.06625
  
def get_item_amount():
 item_cost = float(input("What is the cost of the item you want to buy?:$"))
 return item_cost

def calculate_tax_amount(cost):
  taxed_amount = cost*0.06625
  return taxed_amount

def calculate_final_cost(cost, taxed_amount):
  final_cost = cost + taxed_amount
  return final_cost

def print_receipt(item_cost, taxed_amount, final_cost):
  print("=" *20)
  print("RECEIPT")
  print("=" * 20)

  print(f"Retail Price:${item_cost}")
  print(f"Sales Tax Amount:${taxed_amount:.2f}")
  print(f"Total:${final_cost:.2f}")
  print()

cost = get_item_amount()
tax = calculate_tax_amount(cost)
total = calculate_final_cost(cost, tax)
receipt = print_receipt(cost, tax, total)

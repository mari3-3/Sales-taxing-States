import os as clear

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

def get_items():
  item_names = []
  item_costs = []
  tax_amounts = []
  final_costs = []
  num_items = int(input("How many items are you purchasing?: "))
  for i in range(num_items):
    name = input("What is the name of your item?: ").title()
    item_names.append(name)
    
    cost = get_item_amount()
    item_costs.append(cost)

    tax = calculate_tax_amount(cost)
    tax_amounts.append(tax)

    total = calculate_final_cost(cost, tax)
    final_costs.append(total)
    
  return item_names, num_items, item_costs, tax_amounts, final_costs


def print_receipt(item_names, num_items, item_costs, tax_amounts, final_costs):
  clear.system('clear')
  print("=" * 30)
  print("RECEIPT")
  print("=" * 30)

  for i in range(num_items):
    print(f"Item: {item_names[i]}")
    print(f"Retail Price:${item_costs[i]}")
    print(f"Sales Tax Amount:${tax_amounts[i]:.2f}")
    print(f"Total:${final_costs[i]:.2f}")
    print("~" * 30)
    
item_names, num_items, item_costs, tax_amounts, final_costs = get_items()
print_receipt( item_names, num_items, item_costs, tax_amounts, final_costs)

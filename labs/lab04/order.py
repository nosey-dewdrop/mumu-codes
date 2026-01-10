import os

def find_order(customer_file, customer_name):

      """returns the order ID for the given customer name, or -1 if not found"""
      base_path = os.path.dirname(__file__)
      file_path = os.path.join(base_path, customer_file)

      with open(file_path, "r") as f:
            for line in f:
                  line = line.strip()           
                  comma_index = line.find(",") 
                  name = line[:comma_index].strip()
                  order_id = line[comma_index + 1:].strip()

                  if name.lower() == customer_name.lower():
                        return order_id
      return -1

# find_order("customers.txt", "Anna Karpat") 
# find_order("customers.txt", "Mert Eren") 
# find_order("customers.txt", "Sara Glen") 

def find_order_items(order_file, order_id):
      """returns (total_cost, string_of_items) for the given order ID"""
      base_path = os.path.dirname(__file__)
      file_path = os.path.join(base_path, order_file)

      total = 0.0
      items = []

      with open(file_path, "r") as f:

            for line in f:
                  line = line.strip()

                  first_comma = line.find(",")
                  second_comma = line.find(",", first_comma + 1)

                  current_id = line[:first_comma].strip()
                  item = line[first_comma + 1 : second_comma].strip()
                  price_str = line[second_comma + 1:].strip()

                  if price_str != "":              
                        price = float(price_str)
                        if current_id == str(order_id):
                              items.append(item)
                              total += price


      return total, items


enter = True
while enter:

      name = input("enter customer name to search (exit to quit): ")

      if name.lower() == "exit":
            enter = False

      else:
            order_id = find_order("customers.txt", name)
            
            if order_id == -1:
                  print("customer not found")
            else:
                  total_cost, items = find_order_items("orders.txt", order_id)

                  if total_cost == 0.0:
                        print("no items found for this order")
                        enter = False

                  else:
                        print("items:")
            
                        for item in items:
                              print("- ", item)

                        print(f"total cost: ${total_cost:.2f}")

                        with open(str(order_id) + ".txt", "a") as f:
                              f.write(f"{name}, {total_cost}\n")
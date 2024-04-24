# initialize the price and customer rewards dict
product_price_dict = {
    "vitaminC": {"price": 12.0, "prescription_required": "no"},
    "vitaminE": {"price": 14.5, "prescription_required": "no"},
    "coldTablet": {"price": 6.4, "prescription_required": "no"},
    "vaccine": {"price": 32.6, "prescription_required": "yes"},
    "fragrance": {"price": 25.0, "prescription_required": "no"}
}
customer_to_rewards_dict = {"Kate": 20, "Tom": 32}
dr_prescription_req = ["vaccine"]
customer_order_history = dict()


def get_total_amount(product_names, product_quantitys, amt=0.0):
    for i in range(0, len(product_names)):
        p_name = product_names[i]
        p_quantity = int(product_quantitys[i])
        amt += product_price_dict.get(p_name).get("price") * p_quantity
    return amt


def display_receipt(customers_name, product_names, product_quantitys, total_amount, total_reward):
    print("--------------------------------------------------------------------------")
    print("\t\t\t\t\t\tReceipt")
    print("--------------------------------------------------------------------------")
    print("Name:\t\t\t\t\t", customers_name)
    for i in range(0, len(product_names)):
        product_name = product_names[i]
        product_quantity = product_quantitys[i]
        print("Product:\t\t\t\t", product_name)
        print("Unit Price:\t\t\t\t", str(product_price_dict.get(product_name).get("price")) + " (AUD)")
        print("Quantity:\t\t\t\t", str(product_quantity))
    print("--------------------------------------------------------------------------")
    print("Total Cost:\t\t\t\t", str(total_amount) + " (AUD)")
    print("Earned Reward:\t\t\t", str(total_reward))


def update_reward(customers_name, total_reward):
    if customers_name in customer_to_rewards_dict.keys():
        customer_to_rewards_dict[customers_name] = customer_to_rewards_dict.get(customers_name) + total_reward
    else:
        customer_to_rewards_dict[customers_name] = total_reward


def update_customer_order_history(customers_name, product_name_list, total_amount, total_reward):
    p_dict = dict()
    for p_name in product_name_list:
        if p_name in p_dict.keys():
            p_dict[p_name] += 1
        else:
            p_dict[p_name] = 1

    p_entry = ""
    c = len(p_dict)
    k = 0
    for p_name, count in p_dict.items():

        if k < c-1:
            p_entry += str(count) + " x " + p_name + ", "
        else:
            p_entry += str(count) + " x " + p_name

        k += 1

    if customers_name in customer_order_history.keys():
        old_history = dict(customer_order_history.get(customers_name))
    else:
        old_history = dict()

    if old_history is not None:
        i = len(old_history)
    else:
        i = 1
    key = "Order " + str(++i)

    data = dict()
    data["product"] = p_entry
    data["total_cost"] = total_amount
    data["total_reward"] = total_reward

    # updating the value in history
    old_history[key] = data
    customer_order_history[customers_name] = old_history


def make_purchase():
    # taking input of customer name, product and quantity
    # taking valid customer_name
    while True:
        customers_name = input("Please Enter customer's name :: ")

        if customers_name.isalpha():
            break
        else:
            print("provided customer name is not valid one, it should have only alphabet characters\n")

    # taking valid product name
    while True:
        product_name_list = list(input("Please Enter Product names e.g. [ "
                                       + str(list(product_price_dict.keys())) + "] :: ").split(" "))

        # validating the input product name list
        is_valid = True
        for product_name in product_name_list:
            if product_name.isalpha() and product_name in dr_prescription_req:
                ans = input("The product " + product_name + " require a doctor's prescription, do you have ?")
                if ans.isalpha() and ans == "n":
                    is_valid = False
                    break
            elif product_name.isalpha() and product_name in product_price_dict.keys():
                continue
            else:
                print("Input product name list is not valid one, "
                      "it should have only alphabet characters & must be from " + str(list(product_price_dict.keys()))
                      + "\n")
                is_valid = False
                break

        if is_valid:
            break

    while True:
        product_quantity_list = list(input("Please Enter Quantity e.g [ 1,2,3...] of products : ").split(" "))

        is_valid = True
        for product_quantity in product_quantity_list:
            if product_quantity.isnumeric() and int(product_quantity) > 0:
                continue
            else:
                is_valid = False
                print("Please Enter valid Quantity e.g [ 1,2,3...] of product\n")
                break
        if is_valid:
            break

    total_amount = get_total_amount(product_name_list, product_quantity_list)

    # taking the round of value only for rewards
    if total_amount - int(total_amount) < 0.5:
        total_reward = int(total_amount)
    else:
        total_reward = int(total_amount) + 1

    # update the customer to reward in customer_to_rewards_dict
    update_reward(customers_name, total_reward)

    # update customer order history
    update_customer_order_history(customers_name, product_name_list, total_amount, total_reward)

    # displaying the receipt
    display_receipt(customers_name, product_name_list, product_quantity_list, total_amount, total_reward)


def display_menu_items():
    print("#################################################################################")
    print("You can choose from the following options:")
    print("1: Make a purchase")
    print("2: Add/Update information of products")
    print("3: Display existing customers")
    print("4: Display existing orders")
    print("5: Display customer orders history")
    print("0: Exit the program")
    print("#################################################################################")


def update_product():
    input_data = list(input("Please input product name, price and Dr. prescription [product price y/n]").split(" "))

    for i in range(0, len(input_data) - 3, +3):
        product_name, product_price, prescription_req = input_data[0], input_data[1], input_data[2]

        if product_name in product_price_dict.keys():
            # fetching existing data
            product_data = product_price_dict[product_name]
            # updating new data
            product_data["price"] = product_price
            product_data["prescription_required"] = prescription_req
            # updating the record
            product_price_dict[product_name] = product_data
        else:
            # adding new data
            product_data = dict()
            product_data["price"] = product_price
            product_data["prescription_required"] = prescription_req
            # adding the record
            product_price_dict[product_name] = product_data

        if prescription_req == "y":
            dr_prescription_req.append(product_name)


def print_order_row(key, product_item, total_cost, total_reward):
    print(key + "\t\t\t" + product_item + "\t\t\t" + str(total_cost) + "\t\t\t" + str(total_reward))


def print_order_history(name):
    if name in customer_order_history.keys():
        print("This is the order history of ", name)
        oder_history = dict(customer_order_history.get(name))
        print("\t\t\t\tProduct\t\t\t\tTotal Cost\t\t\tTotal Reward")
        for key, value in oder_history.items():
            value = dict(value)
            print_order_row(key, value["product"], value["total_cost"], value["total_reward"])


def display_main_menu():
    while True:
        # printing one line
        print()
        display_menu_items()
        option = int(input("Choose a option: "))
        if option == 0:
            break

        if option == 1:
            make_purchase()
        elif option == 2:
            update_product()
        elif option == 3:
            print("Existing customers and their rewards ", customer_to_rewards_dict)
        elif option == 4:
            print("Existing product, their prices and prescription required ", product_price_dict)
        elif option == 5:
            name = input("Enter customer name to view the customer's order history : ")
            print_order_history(name)


def main():
    display_main_menu()


if __name__ == "__main__":
    main()

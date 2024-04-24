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


def get_total_amount(product_name, product_quantity):
    amt = 0.0
    if product_name in product_price_dict.keys():
        amt = product_price_dict.get(product_name).get("price") * product_quantity
    return amt


def display_receipt(customers_name, product_name, product_quantity, total_amount, total_reward):
    print("--------------------------------------------------------------------------")
    print("\t\t\t\t\t\tReceipt")
    print("--------------------------------------------------------------------------")
    print("Name:\t\t\t\t\t", customers_name)
    print("Product:\t\t\t\t", product_name)
    print("Unit Price:\t\t\t\t", str(product_price_dict.get(product_name)) + " (AUD)")
    print("Quantity:\t\t\t\t", str(product_quantity))
    print("--------------------------------------------------------------------------")
    print("Total Cost:\t\t\t\t", str(total_amount) + "(AUD)")
    print("Earned Reward:\t\t\t", str(total_reward))


def update_reward(customers_name, total_reward):
    if customers_name in customer_to_rewards_dict.keys():
        customer_to_rewards_dict[customers_name] = customer_to_rewards_dict.get(customers_name) + total_reward
    else:
        customer_to_rewards_dict[customers_name] = total_reward


def purchase():
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
        product_name = input("Please Enter Product name e.g. [ " + str(list(product_price_dict.keys())) + " ] :: ")

        if product_name.isalpha() and product_name in product_price_dict.keys():
            break
        else:
            print("Input product name is not valid one, "
                  "it should have only alphabet characters & must be from " + str(
                list(product_price_dict.keys())) + "\n")

    while True:
        product_quantity = input("Please Enter Quantity e.g [ 1,2,3...] of product : " + product_name + " you want :: ")

        if product_quantity.isnumeric() and int(product_quantity) > 0:
            product_quantity = int(product_quantity)
            break
        else:
            print("Please Enter valid Quantity e.g [ 1,2,3...] of product\n")

    total_amount = get_total_amount(product_name, product_quantity)

    # taking the round of value only for rewards
    if total_amount - int(total_amount) < 0.5:
        total_reward = int(total_amount)
    else:
        total_reward = int(total_amount) + 1

    # update the customer to reward in customer_to_rewards_dict
    update_reward(customers_name, total_reward)

    # displaying the receipt
    display_receipt(customers_name, product_name, product_quantity, total_amount, total_reward)


def display_menu_items():
    print("#################################################################################")
    print("You can choose from the following options:")
    print("1: Make a purchase")
    print("2: Add/Update information of products")
    print("3: Display existing customers")
    print("4: Display existing orders")
    print("5: Exit the program")
    print("#################################################################################")


def update_product():
    input_data = list(input("Please input product name, price and Dr. prescription [product price y/n]").split(" "))
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


def display_main_menu():
    while True:
        # printing one line
        print()
        display_menu_items()
        option = int(input("Choose a option: "))
        if option == 5:
            break

        if option == 1:
            purchase()
        elif option == 2:
            update_product()
        elif option == 3:
            print("Existing customers and their rewards ", customer_to_rewards_dict)
        elif option == 4:
            print("Existing product, their prices and prescription required ", product_price_dict)


def main():
    display_main_menu()


if __name__ == "__main__":
    main()

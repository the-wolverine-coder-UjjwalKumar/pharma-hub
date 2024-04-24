
# initialize the price and customer rewards dict
product_price_dict = {"vitaminC": 12.0, "vitaminE": 14.5, "coldTablet": 6.4, "vaccine": 32.6, "fragrance": 25.0}
customer_to_rewards_dict = {"Kate": 20, "Tom": 32}


def get_total_amount(product_name, product_quantity):
    amt = 0.0
    if product_name in product_price_dict.keys():
        amt = product_price_dict.get(product_name) * product_quantity
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


def main():
    # taking input of customer name, product and quantity
    customers_name = input("Please Enter customer's name :: ")
    product_name = input("Please Enter Product name e.g. [ " + str(list(product_price_dict.keys())) + " ] :: ")
    product_quantity = int(
        input("Please Enter Quantity e.g [ 1,2,3...] of product : " + product_name + " you want :: "))

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


if __name__ == "__main__":
    main()

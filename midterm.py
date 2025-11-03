#the menu formatted recursively
menu = {
    "Burger": {
        "Price": 10,
        "Toppings": {
            "Cheese": {"Price": 0.75},
            "Lettuce": {"Price": 0.25},
            "Tomato": {"Price": 0.30},
        }
    },
    "Chicken Sandwich": {
        "Price": 8,
        "Toppings": {
            "Mayo": {"Price": 0.20},
            "Pickles": {"Price": 0.25},
            "Lettuce": {"Price": 0.25},
        }
    },
    "Chicken Nuggets": {
        "Price": 6,
        "Toppings": {
            "BBQ Sauce": {"Price": 0.50},
            "Honey Mustard": {"Price": 0.50},
            "Ranch": {"Price": 0.50},
        }
    }
}

# two tables for variants of y/n
yes = (
    "yes",
    'y',
    'ye',
    'yea',
    'yeah',
    'ya',
    'yep'
)

no = (
    'no',
    'n',
    'na',
    'nah',
    'nope',
    'stop',
    'cancel',
    'skip'
)

# buncha bucks
initial_cash = int(200000)


def display_menu(): #displays the menu
    print("Menu:")
    for i, v in menu.items():
        print(i + ": ") #item:
        print("\n Price: " + str(v["Price"])) #price: 00
        print("\n Toppings: ") #lists toppings
        for o, b in v["Toppings"].items():
            print(f"\n {o} for ${str(b["Price"])}") #(topping) for $(price)

def display_order(order): #writes your order and returns the final price
    final_subtotal = 0
    for i, v in order.items():
        subtotal = v["Price"]
        print(i + "             " + str(v["Price"]))
        for o, b in v["Toppings"].items(): #loops through any toppings and states their price with a dash at the start
            print("- " + o + "          " + str(b["Price"]))
            subtotal += b["Price"]
        print("item subtotal" + "                " + str(subtotal)) # price of the item with any additional toppings price added ontop
        final_subtotal += subtotal
    print("-"*25) # big line
    print("final subtotal"+"                "+str(final_subtotal))
    tax = final_subtotal*0.078 #7.8% tax
    print("tax"+"                "+str(tax))
    print("final subtotal"+"                "+str(final_subtotal + tax))
    return final_subtotal + tax

def get_item(menulist,text): # function to attempt to get an item from a given list with a prompt for the item
    itemname = input(text)
    found = False
    for i in menulist.keys(): # iterate through the keys of the provided dictionary
        if i.lower() == itemname.lower(): #if both keys match (case insensitive)
            found = True # found it!
            itemname = i
    if found == True: # if it found it
        return itemname,menulist[itemname] # return the key and the value/item
    elif itemname.lower() in no: # if answer is in the No list, send cancel signal
        return "break","break"
    else: # try again
        return get_item(menulist,"Please input a valid item or say 'stop' to cancel.")

def build_order(): # the main function to build the order
    order = {} # create order dictionary
    skipped = True # no answer yet, so customer could skip
    while True:
        initial_question = "What would you like to order? Say 'stop' to cancel."
        if len(order)>=1: # if theres already an entry in your order
            initial_question = "What else would you like to order? Say 'stop' to cancel."
        key,real_item = get_item(menu,initial_question) # asks the question and tries for answer
        if key and key != "break": #if theres a key and its not the cancel signal
            skipped = False # found an answer so not a skipped order
            item = real_item.copy() # copies the chosen item to avoid mutating the menu
            item["Toppings"] = {} # resets the toppings so it doesnt have one of each by default
            while len(item["Toppings"]) <= 5: # 5 toppings max, same process as choosing an item but for toppings
                question = "Would you like any toppings?"
                if len(item["Toppings"]) >= 1:
                    question = "Would you like any more toppings?"
                topping_key,topping_item = get_item(real_item["Toppings"],question)
                if topping_key and topping_key != "break":
                    item["Toppings"][topping_key] = topping_item
                elif topping_key == "break":
                    break
            order[key] = item # adds the item to your order
        elif key == "break":
            print("Okay, moving on.")
            break
    return order, skipped

def start_order(): # the initial function to start and end everything
    global initial_cash # initial cash is out of the scope i guess
    print(f"Your father passed away and left you with ${str(initial_cash)}, so you decide to visit your local burger joint for a meal.")
    print("*ding ding*")
    print("\n Welcome to Burgie's Burgeria")
    result, skipped = build_order() # go do the whole order process
    if skipped == False: # if it wasnt a skipped order...
        print(f"Your final order is: ")
        total = display_order(result) # display the order and get the total cost
        if input("Would you like to pay?").lower() in yes: # if u wanna pay?
            if total > initial_cash: # if final price is less than what you have you cant buy it
                print("Looks like you're too broke!")
            else: # otherwise you got it
                initial_cash -= total
                print(f"\n You now have ${initial_cash} left.")
                print("\n Thank you for dining at Burgie's Burgeria!")
    else:
        print("\n Thank you for dining at Burgie's Burgeria!")

    
# running the two initial functions
display_menu()
start_order()
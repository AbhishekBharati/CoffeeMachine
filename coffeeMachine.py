MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 250,
    "milk": 200,
    "coffee": 100,
}

item = ""

while item != "stop":

    item = input("What would you like to drink? (espresso/latte/cappuccino)")

    avail_ingreds = []
    req_ingreds = []
    b = []



    cent_returned = 0

    # Checks if there is sufficient Raw & Material in Vending Machine.
    def sufficient_resources(res):
        match res:
            case "espresso":
                for ing in resources:
                    avail_ingreds.append(ing)
                for req_ing in MENU["espresso"]["ingredients"]:
                    req_ingreds.append(req_ing)
                if avail_ingreds[0] >= req_ingreds[0] and avail_ingreds[1] >= req_ingreds[1] and avail_ingreds[2] >= \
                        req_ingreds[2]:
                    return True
                else:
                    return False
            case "latte":
                for ing in resources:
                    avail_ingreds.append(ing)
                for req_ing in MENU["latte"]["ingredients"]:
                    req_ingreds.append(req_ing)
                if avail_ingreds[0] >= req_ingreds[0] and avail_ingreds[1] >= req_ingreds[1] and avail_ingreds[2] >= \
                        req_ingreds[2]:
                    return True
                else:
                    return False
            case "cappuccino":
                for ing in resources:
                    avail_ingreds.append(resources[ing])
                for req_ing in MENU["cappuccino"]["ingredients"]:
                    req_ingreds.append(MENU["cappuccino"]["ingredients"][req_ing])
                if avail_ingreds[0] >= req_ingreds[0] and avail_ingreds[1] >= req_ingreds[1] and avail_ingreds[2] >= \
                        req_ingreds[2]:
                    return True
                else:
                    return False

    # Checks Whether the user has inserted sufficient Money.
    def suff_money(a):
        quarter = float(input("How many Quarters? "))
        dime = float(input("How many Dime? "))
        nickel = float(input("How many Nickel"))
        penny = float(input("How many Penny?"))
        quarter = quarter * 0.25
        dime = dime * 0.10
        nickel = nickel * 0.05
        penny = penny * 0.01
        sum = quarter + dime + penny + nickel
        match a:
            case "espresso":
                if sum >= MENU["espresso"]["cost"]:
                    cent_returned = sum - MENU["espresso"]["cost"]
                    print(f"Here is your ${cent_returned} in change")
                    return True
                else:
                    return False
            case "latte":
                if sum >= MENU["latte"]["cost"]:
                    cent_returned = sum - MENU["latte"]["cost"]
                    print(f"Here is your ${cent_returned} in change")
                    return True
                else:
                    return False
            case "cappuccino":
                if sum >= MENU["cappuccino"]["cost"]:
                    cent_returned = sum - MENU["cappuccino"]["cost"]
                    print(f"Here is your ${cent_returned} in change")
                    return True
                else:
                    return False

    # Updating all the ingredients present in Resources.
    def ingred_update(d):
        match d:
            case "espresso":
                for ing in resources:
                    resources[ing] -= MENU["espresso"]["ingredients"][ing]
            case "latte":
                for ing in resources:
                    resources[ing] -= MENU["latte"]["ingredients"][ing]
            case "cappuccino":
                for ing in resources:
                    resources[ing] -= MENU["cappuccino"]["ingredients"][ing]


    # Printing Report --> Gets activate when, user insert Report.
    def available_resources(elem):
        for i in elem:
            print(i, elem[i])


    if item == "report":
        available_resources(resources)
        break
    if item == "stop":
        break


    if sufficient_resources(item):
        if suff_money(item):
            ingred_update(item)
            print(f"Here is Your {item}. Enjoy!!!")
        else:
            print(f"Sorry that's not enough Money, here are your ${sum}")
    else:
        print("Sorry there is not enough Ingredients.")

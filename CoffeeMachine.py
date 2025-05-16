def display():

    print(f"water: {recourse["water"]} ml!")
    
    print(f"milk: {recourse["milk"]} ml!")
    
    print(f"coffee: {recourse["coffee"]} g!")
    
    print(f"money: {recourse["money"]} dram!")

def ingridient(case):

    for key in coffee[case]["ingridients"]:

        if recourse[key]<coffee[case]["ingridients"][key]:

            return key

def count_change(coin_50,coin_100,coin_200,case):

    money=coin_50*50+coin_100*100+coin_200*200

    change=money-coffee[case]["cost"]

    return change

def is_available(case):

    for key in coffee[case]["ingridients"]:

        if recourse[key]<coffee[case]["ingridients"][key]:

            return False
    
    return True
    

def coffee_maker(case):
    
    if not is_available(case):

        return False

    else:

        print("Please, insert coins!")

        coin_50=int(input("How many 50 coins?: "))
        
        coin_100=int(input("How many 100 coins?: "))
        
        coin_200=int(input("How many 200 coins?: "))

        change=count_change(coin_50,coin_100,coin_200,case)

        if change<0:

            print("Sorry that is not enough money!")

            return False

        for key in coffee[case]["ingridients"]:

            recourse[key]-=coffee[case]["ingridients"][key]

        recourse["money"]+=coffee[case]["cost"]

        if change>0:

            print(f"Here is your {change} coins change!")

        return True

coffee={

    "latte":{

        "ingridients":{

            "water":200,

            "milk":150,

            "coffee":20

        },

        "cost":250

    },

    "espresso":{

        "ingridients":{

            "water":50,

            "coffee":25

        },

        "cost":150

    },

    "cappuccino":{

        "ingridients":{

            "water":250,

            "milk":100,

            "coffee":30

        },

        "cost":300

    }
    
}

recourse={

    "water":1000,

    "milk":1000,

    "coffee":200,

    "money":1000

}

case=0

while case!='off':

    case=input("What would you like to have? (latte/espresso/cappuccino): ")

    if case=='report':

        display()

    if case in coffee.keys():
        
        if coffee_maker(case)==True:
        
            print(f"Here is your {case}!")
        
        else:

            if not is_available(case):

                print(f"Sorry there is no enough {ingridient(case)}!")
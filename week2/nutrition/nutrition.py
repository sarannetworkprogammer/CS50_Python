def main():

    dict1 ={
        "apple"         :   "130",
        "avocado"       :       "50",
        "banana"        : "110",
        "cantaloupe"     :   "50",
        "grapefruit"     :  "60",
        "grapes"         :  "90",
        "honeydew melon"    :   "50",
        "kiwifruit"     :   "90",
        "lemon"         :   "15",
        "lime"          :   "20",
        "nectarine"     :   "60",
        "orange"        :   "80",
        "peach"         :   "60",
        "pear"          :   "100",
        "plums"         :   "70",
        "strawberries"  :   "50",
        "sweet cherries" :   "100",
        "tangerine"     :   "50",
        "watermelon"    :   "80"


    }

    a = input("Item: ").lower()

    if a in dict1:
        print(f"Calories: {dict1[a]}")

if __name__ == "__main__":
    main()
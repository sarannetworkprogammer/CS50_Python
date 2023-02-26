


def change(insert_coin, due):
    if insert_coin == 50:
        due = due -insert_coin

    elif insert_coin == 25:
        due = due - insert_coin

    elif insert_coin == 10:
        due = due - insert_coin

    elif insert_coin == 5:
        due = due - insert_coin

    return due

def coin():
    insert_coin = int(input("Insert Coin: "))
    return insert_coin



def main():
    due = int(50)
    print(f"Amount Due : {due}")

    while True:
        if due > 0:
            insert_coin = coin()
            temp = due
            due = change(insert_coin,due)
            if due == 0:
                print(f"Change Owed: {due}")
                break
            if due < 0:
                print("Change Owed",abs(due))
                break

            print(f"Amount Due: {due}")
        else:
            break


if __name__ == "__main__":
    main()

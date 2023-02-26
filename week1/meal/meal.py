def main():
    time = input("What time is it? ").strip()
    new_time = convert(time)
    #print(new_time)
    if new_time >= 7.0 and new_time <= 8.0:
        print("breakfast time")
    elif new_time >= 12.0 and new_time <= 13.0:
        print("lunch time")
    elif new_time >= 18.0 and new_time <= 19.0:
        print("dinner time")





def convert(time):
    hours,minutes = time.split(":")
    return (float(hours) + float(minutes)/60)




if __name__ == "__main__":
    main()




import time

def shuffle(lis):
    import random
    shuffled_list = random.shuffle(lis)
    return shuffled_list


if __name__ == "__main__":
    number_of_names = int(input("Please enter the number of names: "))
    names = []
    surnames = []
    new_names = []
    name = []
    index = 0
    for i in range(number_of_names):
        name_input = input(f"Please enter name {i+1}: ")
        name.append(name_input)
        lst = name_input.split(" ")[1]
        lst2 = name_input.split(" ")[0]
        surnames.append(lst)
        names.append(lst2)
    shuffle(surnames)
    for i in range(len(name)):
        new_names.append(names[i] + " " + surnames[i])
    print(f"So here is your jumbled list of names: {new_names}")
    time.sleep(1)
    print("=|=|=|=|=|=|=|=|=|=|=|=THANKS FOR USING THIS PROGRAM=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|")

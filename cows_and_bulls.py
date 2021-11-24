import random
#generate 4 digit random number
number=random.randint(1000,9999)

#func to convert list from int
def from_str_to_list(str_num):
    str_num=str(str_num)
    lst_num=[x for x in str_num]
    return lst_num

# convert random number to list
random_number_list=from_str_to_list(number)

cow=0
tries=0

while cow<4:

    #tracking how many tries user perform
    tries+=1

    # reset cow,bull for every trie
    cow = 0
    bull = 0

    # User input 4 digit number
    user_input = input('4 digit number: ')

    # convert user input number to list
    user_inuput_list = from_str_to_list(user_input)

    # engine
    for index,value in enumerate(random_number_list):
            if random_number_list[index]==user_inuput_list[index]:
                cow+=1
            elif random_number_list[index] in user_inuput_list:
                bull+=1
    else:
        print('Cow:',cow)
        print('Bull:',bull)
else:
    if tries==1:
        print("You made it from first trie!")
    else:
        print("You made it from",tries,"tries!")

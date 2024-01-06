counter = 0

while counter <= 10:
    # print(counter)
    counter = counter + 1

########################################################################################################################

qwerty: list = [1, 2, 4.1, 'Peeska', False, None]

for user in qwerty:


    if user == 2:
        continue

    if user == 4.1:
        break

    print(user)
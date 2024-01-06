qwerty: list = [1, 2, 4.1, 'Peeska', False, None]

print(qwerty)
print(len(qwerty))
print(qwerty[4])
print(qwerty[-1])
qwerty.append([1, 2])
print(qwerty)
qwerty[3] = 'sosiska'
print(qwerty)


########################################################################################################################

asd: tuple = (1, 2, 3)

########################################################################################################################

slovar: dict = {
    'k1': 1,
    'k2': [1, 2, 3],
    'k3': 'kot',
    'k4': {
        'php': True,
        'python': False
    }
}

print(slovar.keys())
print(slovar.values())
print(slovar['k2'])

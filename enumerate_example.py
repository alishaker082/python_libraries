example = ['left', 'right', 'up', 'down']

for i in range(len(example)):
    print(i, example[i])

for key, value in enumerate(example):
    print(key, value)

new_dict = dict(enumerate(example))
print(new_dict)

a = [(i,j) for i, j in new_dict.items()]
print(a)
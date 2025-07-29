animals = ["cat","dog","rabbit","hamster","dog","parrot"]
frist_dog_index = animals.index("dog")
print(f"the first occurrence of 'dog'is at index: {frist_dog_index}")

second_dog_index =animals.index("dog",frist_dog_index)
print(f"The second occurrence of 'dog' is at index :{second_dog_index}")
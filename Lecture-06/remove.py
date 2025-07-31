fruits_with_duplicatees = ["apple","banana","apple","cherry","apple","kiwi"]
while "apple" in fruits_with_duplicatees:
    fruits_with_duplicatees.remove("apple")
print(f"Fruits after remove :{fruits_with_duplicatees}")
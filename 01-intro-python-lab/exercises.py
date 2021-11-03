

if __name__ == "__main__":
    for ch in "Hello Pyton!":
        print(ch)

    fruits_list = ["Apple", "Banana", "Orange", "Grapefruit", "Apple"]
    fruits_list.append("Plum")
    for fruit in fruits_list:
        print(fruit)
    print()

    fruits_tuple = ("Apple", "Banana", "Orange", "Grapefruit", "Apple")
    fruits_list.append("Plum")
    for fruit in fruits_tuple:
        print(fruit)
    print()

    fruits_set = {"Apple", "Banana", "Orange", "Grapefruit", "Apple"}
    for fruit in fruits_set:
        print(fruit)
    print()

    fruits_dict = {"Apple": 120 , "Banana": 38, "Orange": 45, "Grapefruit": 345, "Apple": 79}
    for fruit in fruits_dict:
        print(fruit, "->", fruits_dict[fruit])

    birth_date = "03.10.2021"
    nums = birth_date.split(".")
    print(nums)
    for num in nums:
        print(int(num))

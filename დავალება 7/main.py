# 1. კონსოლიდან შეიტანეთ მიმდევრობა. დაბეჭდეთ უნიკალური მონაცემებიანი სიმრავლე (set).
user=input("შეიყვანეთ მონაცემები მიმდევრობა: ")
data=user.split(",")
unique_data=set(data)
print("უნიკალური მონაცემებიანი სიმრავლე:", unique_data)

# 2. პირობა იგივეა, რაც პირველ დავალებაში, ოღონდ დაბეჭდეთ უნიკალური მონაცემებიანი სიმრავლე, 
# რომლის შეცვლაც შეუძლებელი იქნება (frozenset).
user=input("შეიყვანეთ მონაცემები მიმდევრობა: ")
data=user.split(",")
unique_data=frozenset(data)
# unique_data.add(25) ასეთ შემთხვევაში გამოიტანს შემდეგ შეცდომას - AttributeError: 'frozenset' object has no attribute 'add'
print("უნიკალური მონაცემებიანი (frozenset) სიმრავლე:", unique_data)

# 3. აიღეთ set ტიპის ორი მონაცემი. ელემენტები თავად განსაზღვრეთ. 
# დაბეჭდეთ გაერთიანებული მონაცემები კორტეჟის სახით (tuple).
set1={1,2,3,4,5}
set2={4,5,6,7,8}  
union_set=set1.union(set2)
union_tuple=tuple(union_set)    
print("გაერთიანებული მონაცემები კორტეჟის სახით:", union_tuple)

set1 = {'a', 'b', 'c', 'd'}
set2 = {'c', 'd', 'e', 'f'}
union_set = set1.union(set2)
print(tuple(union_set))

# 4. კონსოლიდან შევიტანოთ რიცხვების მიმდევრობა როგორც კორტეჟი (tuple). 
# დავბეჭდოთ მხოლოდ უნიკალური ელემენტები სიის სახით (list).
user=input("შეიყვანეთ რიცხვების მიმდევრობა (კორტეჟი): ")
data=tuple(user.split(","))
unique_list=list(set(data))
print("უნიკალური ელემენტები სიის სახით:", unique_list)


# 5. მოცემულია სია, რომლის ელემენტები წარმოადგენენ კორტეჟს:
# [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]

# დაბეჭდეთ შემდეგი ფორმატით:
# Name: Gega, Age: 24
# Name: Gaga, Age: 21
# Name: Goga, Age: 19
# Name: Giga, Age: 27
# Name: Gagi, Age: 11

arr=[("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]
for i in enumerate(arr):
    print(f"Name: {i[1][0]}, Age: {i[1][1]}",)
print("\n")

arr=[("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]
for age,name in arr:
    print(f"Name: {age}, Age: {name}")
    
# # 6. მოცემულია მომხმარებლების სია: ["Irakli", "Giorgi", "Nona", "Oto"].
# # ასევე გვაქვს სხვა მომხმარებლებიც: ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]
# # დავბეჭდოთ თანხვედრა.

list1 = ["Irakli", "Giorgi", "Nona", "Oto"]
list2 = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]

answer = set(list1).intersection(set(list2))
print("სიმრავლის თანხვედრა:", *answer)

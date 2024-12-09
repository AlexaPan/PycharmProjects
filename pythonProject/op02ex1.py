#задача 1: вычисление суммы элементов списка
print("Ex1")
list_ex = [1 , 35, 3, 24]
sum = 0
for i in list_ex:
    sum += i
print(list_ex)
print(sum)

#задача 2
print("\nEx2")
list_ex2 = []
list_ex2.append(2)
list_ex2.append(5)
list_ex2.append(23)
print(list_ex2)
list_ex2.insert(0,  54)
list_ex2.insert(1,87)
print(list_ex2)
list_ex2.sort(reverse=True)
print(f"Сортированный: {list_ex2}")

#задача 3, 4
print("\nEx3 and Ex4")
set1 = {1, 4, 7, 6}
set2 = {2, 4, 7, 1, 5}
print(set1)
print(set2)
set_union = set1.union(set2)
set_intersection = set1.intersection(set2)
set_difference = set1.difference(set2)
print(f"Union set: {set_union}")
print(f"Intersection set: {set_intersection}")
print(f"Difference set: {set_difference}")

#задача 5
print("\nEx5")
list_ex5 = []
for i in range(11):
    element = input("Insert element of list ")
    list_ex5.append(element)
print(f"List: {list_ex5}")

#словарь
print("\nDic")
dict_name = {
1: "one",
2: "two",
3: "three"
}
keys = dict_name.keys()
print(keys)
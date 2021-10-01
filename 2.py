# 7
list1 = [10, 20, 10, 30, 40, 40]
print("the unique values from 1st list is")
list_set = set(list1)
unique_list = (list(list_set))
for x in unique_list:
    print(x)

# 9
test_list = ['Akash', 'Nikhil', 'Manjeet', 'akshat']
check = 'A'
print("The original list : " + str(test_list))
res = [idx for idx in test_list if idx[0].lower() == check.lower()]
print("The list of matching first letter : " + str(res))

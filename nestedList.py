n = int(input())
List=[]
Marks = set()
Sorted_Names = []
for _ in range(n):
    name = input()
    mark = float(input())
    List.append([name, mark])
    Marks.add(mark)
sort_Marks = sorted(Marks)
second_lower_Mark =sorted(Marks)[1]
 
for name, mark in List:
    if mark == second_lower_Mark:
        Sorted_Names.append(name)
        
Ascend_names = sorted(Sorted_Names)
for name in Ascend_names:
    print(name, end="\n")


# Input
#
# 5
# abhi
# 60
# rahul
# 90
# ashish
# 40
# ruhi
# 60
# amit
# 80

#Output
# abhi
# ruhi
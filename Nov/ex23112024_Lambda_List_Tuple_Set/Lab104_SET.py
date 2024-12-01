set1 = set(["TheTestingAcademy", "For", "TheTestingAcademy."]) # Converting list to set
print(set1)
print(len(set1)) # Output -> 3 as "TheTestingAcademy" and "TheTestingAcademy." are unique items coz of the dot (.)

# set1 = set(["TheTestingAcademy", "For", "TheTestingAcademy" , "."])
# print(set1)
# print(len(set1)) # Output -> 3 as one entry is only counted for "TheTestingAcademy" as set only takes unique elements


for i in set1:
    print(i)

# Output:
# For
# TheTestingAcademy
# TheTestingAcademy.


set1.add("Anu")
set1.add("Anu")
set1.add("ANu")
print(set1)
# Output : {'ANu', 'TheTestingAcademy.', 'TheTestingAcademy', 'Anu', 'For'}


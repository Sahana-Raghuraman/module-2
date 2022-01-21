Mydict = {}

elements = int(input("Enter the number of elements to store:"))

for i in range(elements):
    name = int(input("Enter the roll no.:"))
    rollno = float(input("Enter the percentage:"))
    Mydict.update({name: rollno})

print(Mydict)

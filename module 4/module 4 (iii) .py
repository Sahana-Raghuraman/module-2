def Data_Type (z, y, x, w, v, u, t):
    my_integer = z
    my_float = y
    my_boolean = x
    my_string = w
    my_list = v
    my_tuple = u
    my_dict = t
    print(f'\nI have a integer :{my_integer}, \nwith a float : {my_float}, \nhaving a boolean : {my_boolean}, \nfollowed by a string : {my_string}, \nforming a list : {my_list},'
          f'\nwith a tuple : {my_tuple}, \nin a dictionary : {my_dict}')

z = int(input('Type an integer'))
y = float(input('Type a float'))
x = bool(input('Give true or flase'))
w = str(input('Type a name'))
v = list(input('Give a list without comma'))
u = tuple(input("Enter a tuple without comma"))
t = {}
name = input("Enter a Name")
age = int(input("Enter age"))
t.update({name: age})

Data_Type(z, y, x, w, v, u, t)


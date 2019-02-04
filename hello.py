value = input("give me a value: ")
if len(value) > 10:
    print("this is working")


# # i = 0


# # while i < 10:
# #     print(i)
# #     i += 1

# """
# a long multi-line 
# comment can be made with a triple quote string
# """

# #issue with input function 
while True:
    value = input("input something or type 'done' to quit: ")
    if value.lower().strip() == "done":
       break
    print(value)




# # for element in (1,2,3,4):
# #     print(element)

# for i in range(50, 100, 3):
#     if i % 17 == 0:
#         print(i) 

# for i in range(40, -1, -1):
#     print(i)

# syntax doesnt take
# for x in range(10):
#     for y in range(10):
#         print("{}, {}".format(x,y), end = " ")
#         print()

# newlist = []
# for i in range(20):
#     newlist.append(i * 7)

# print(newlist)


# def myfunc(x, y):
#     return x + y

# x = 10 

# print(myfunc(x,2))
# writing
# f = open("C:\\Users\\Hemant Raghav\\OneDrive\\Desktop\\Git Repos\\PYTHON\\File handlig\\demo.txt", "w")
# data = f.write("going to die \n dont know what to do")
# f.close()


# append
# f = open("C:\\Users\\Hemant Raghav\\OneDrive\\Desktop\\Git Repos\\PYTHON\\File handlig\\demo.txt", "a")
# data = f.write("\nNow using append I am creating new line")
# f.close()



# creating new file using append or write
# f = open("newfile.txt", "a")
# f.close()


# r+ for reading and writing (overwrite the data from starting)
# f= open("C:\\Users\\Hemant Raghav\\OneDrive\\Desktop\\Git Repos\\PYTHON\\File handlig\\demo.txt", "r+")
# f.write("my name is hemant")
# print(f.write)
# f.close()



# w+ for reading and writing (truncate the data)
# f= open("C:\\Users\\Hemant Raghav\\OneDrive\\Desktop\\Git Repos\\PYTHON\\File handlig\\demo.txt", "w+")
# f.write("")
# print(f.write)
# f.close()



# a+ for reading and append (append or add the data after the text)
# f= open("C:\\Users\\Hemant Raghav\\OneDrive\\Desktop\\Git Repos\\PYTHON\\File handlig\\demo.txt","a+")
# f.write("\nmy name is hemant")
# print(f.write)
# f.close()


# With syntax 
# with open("C:\\Users\\Hemant Raghav\\OneDrive\\Desktop\\Git Repos\\PYTHON\\File handlig\\demo.txt","r") as f:
#  data = f.read()
#  print(data)

# with open("C:\\Users\\Hemant Raghav\\OneDrive\\Desktop\\Git Repos\\PYTHON\\File handlig\\demo.txt","w") as f:
#  data = f.write("new data")
 

# deleting of file
# import os
# os.remove("C:\\Users\\Hemant Raghav\\OneDrive\\Desktop\\Git Repos\\PYTHON\\File handlig\\demo.txt")


# replacement of word
# with open("practice.txt", "r") as f:
#     data = f.read()
   
# new_data= data.replace("java", "python")   
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)    


# find word learning in file
# with open("practice.txt","r") as f:
#     data=f.read()
#     if (data.find("learning")!=-1):
#      print("found")
#     else:
#        print("not found") 


# above question in function form
# def check_for_word():
#     with open("practice.txt","r") as f:
#       data=f.read()
#       if (data.find("learning")!=-1):
#         print("found")
#       else:
#        print("not found") 

# check_for_word()



# check the line of word learning
# def check_for_line():
#     word="learning"
#     data=True
#     line_no=1
#     with open("practice.txt","r") as f:
#         while data:
#             data=f.readline()
#             if (word in data):
#                 print(line_no)
#                 return
#             line_no +=1
#     return-1   
# print(check_for_line())



# find count of even numbers
# count=0
# with open("practice.txt", "r") as f:
#     data= f.read()
#     nums = data.split(",")
#     for val in nums:
#         if (int(val)%2 == 0):
#             count +=1

# print(count)            






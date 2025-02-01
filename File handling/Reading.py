# f = open("C:\\Users\\Hemant Raghav\\OneDrive\\Desktop\\Git Repos\\PYTHON\\File handlig\\demo.txt", "r")
# data = f.read()
# print(data)
# f.close()


# specific characters can be read
# f = open("C:\\Users\\Hemant Raghav\\OneDrive\\Desktop\\Git Repos\\PYTHON\\File handlig\\demo.txt", "r")
# data = f.read(6)
# print(data)
# f.close()



# readline()
# f = open("C:\\Users\\Hemant Raghav\\OneDrive\\Desktop\\Git Repos\\PYTHON\\File handlig\\demo.txt", "r")
# data1 = f.readline()
# print(data1)

# data2 = f.readline()
# print(data2)

# data3 = f.readline()
# print(data3)
# f.close()


# readline()
# with open("C:\\Users\\Hemant Raghav\\OneDrive\\Desktop\\Git Repos\\PYTHON\\File handlig\\demo.txt" , "r") as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         print(line)





# open both files 
with open('C:\\Users\\Hemant Raghav\\OneDrive\\Desktop\\Git Repos\\PYTHON\\File handlig\\demo.txt','r') as firstfile, open('practice.txt','w') as secondfile: 
	
	# read content from first file 
	for line in firstfile: 
			
			# write content to second file 
			secondfile.write(line)

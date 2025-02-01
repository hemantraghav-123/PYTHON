import pandas as pd
d = [(1,'abcd',20,'male'),
     (2,'ad',21,'male'),
     (3,'abd',20,'male')]
df = pd.DataFrame(d,columns=['studied','name','age','gender'])
print(d)

# d = [(1,'abcd',20,'male'),
#      (2,'ad',21,'male'),
#      (3,'abd',20,'male')]
# df = pd.DataFrame(d,columns=['studied','name','age','gender'])
# print(df)
# print(df.head(2),"\n")
# print(df.shape,"\n")
# print(df.columns,"\n")
# print(df.size,"\n")
# print(df.dtypes,"\n")
# print(df.values,"\n")
# print(df.index,"\n")
# file = pd.read_csv('9 cars.csv')
# file1 = pd.read_csv('9 cars.csv',sep="\t",nrows=10)
# print(file,"\n")
# print(file1,"\n")
# print(file1.head(5),"\n")
# pop = pd.DataFrame(file,index=[4,6,8])
# print("Cars",pop,"\n")
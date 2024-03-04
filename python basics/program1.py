
# class Cse:
#     def python():
#         a=input("Enter your name -> ")
#         print(a)
#         print(a.upper())
#         print(type(a))
# obj=Cse.python()
# print(obj)




arr_1=[1,2,3,4,5]
# arr_2=(1,2,3,4,5)
# arr_3={1,2,3,4,5}
# arr_4={
#     "name":"mainak",
#     "age":2,
#     "gender":"male",
# }
# print(type(arr_1))
# print(type(arr_2))
# print(type(arr_3))
# print(type(arr_4))


# for i in range(len(arr_1)):
#     print(arr_1[i],end="**")


# print(len(arr_1))


class Test:
    def arraySort():
        arr_1=[]
        n=int(input("Enter the no. of array element : "))
        for x in range(0,n):
            y=int(input("Enter value : "))
            arr_1.append(y)
        print(arr_1)
        print("\t\t-----Ascending Order-----")
        arr_1.sort()
        print(arr_1)
        print("\t\t-----Descending Order-----")
        arr_1.sort(reverse=True)
        print(arr_1)       
Test.arraySort()




















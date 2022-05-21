
#Recursion brush up
# def sum_all(input_data,index):
#     if index == len(input_data)-1:
#         return input_data[index]
#     else:
#         return input_data[index] +sum_all(input_data,index+1)

# print(sum_all([1,2,3,4,5,6],0))


# id_counter = 0    
# small_ex = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
# other_ex "2 5 2 0 0 1 5 0 2 4 5  "
# input_data= list(map(int,small_ex.split()))

# with open('2018/d8-input.txt','r') as f:
#     s= f.read()

# input_data = list(map(int,s.split()))


# index = 0
# read_after = []
# total_meta_sum = 0
# child_count = []
# while index<len(input_data):
#     if read_after and index == len(input_data)-read_after[0]:
#         meta_sum=0
#         read_them = read_after.pop()
#         for i in range(read_them):
#             meta_sum+=input_data[index+i]
#         total_meta_sum+=meta_sum
#         print(index)
#         break
#     if input_data[index]>0:
#         child_count.append(input_data[index])
#         read_after.append(input_data[index+1])
#         index+=2
#         continue
#     if input_data[index] == 0:
#         if input_data[index+1] == 0:
#             index+=2
#             continue
#         index+=1
#         meta_count = input_data[index]
#         index+=1
#         meta_sum = 0
#         for i in range(meta_count):
#             meta_sum+=input_data[index+i]
#         total_meta_sum+=meta_sum
#         index+=meta_count
#         if child_count[-1]==1:
#             child_count.pop()
#             meta_sum=0
#             to_read = read_after.pop()
#             for i in range(to_read):
#                 meta_sum+=input_data[index+i]
#             total_meta_sum+=meta_sum
#             index+=to_read
#         else:
#             child_count[-1] = child_count[-1]-1
# print(total_meta_sum)

    







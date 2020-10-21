count = 0

# for i in range(0,46,3) :
#     for j in range(0,46,4) :
#         for k in range(0,46,20) :
#             if i+j+k == 46 :
#                 count=count+1

# print(count)

exp=[3,4,20]
for i1 in exp :
    for i2 in exp :
        for i3 in exp :
            if(i1+i2+i3==46):
                count=count+1

print(count)
                                                            
# for i in range(50,101,50):
#     for j in range(20,101,20):
#         for k in range(10,101,10):
#             for m in range(5,101,5):
#                 if i+j+k+m == 100:
#                     print("{},{},{},{}".format,i,j,k,m)
#                     count = count + 1
# print(count)
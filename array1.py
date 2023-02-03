stock_price = [298,305,320,301,292] #integer size -> 4 bytes
print(stock_price[0])
print(stock_price[3])
# addr + index * sizeof(int)

#searching in array -> can be carried out with index or value

# for inserting the value in the list -> use insert fn
# eg : stock_price.insert(position/index, value)
# add fn appends the value at last

#for deleting use remove fn 
# eg : stock_price.remove(index)

#Array types -> static and dynamic
#static -> array size do not change
#dynamic array -> size changes -- initaiall, there will be a certain 
#                                 capacity say m. when the value is added
#                                 additional space of m*2 (G.P) and the elements 
#                                 will be copied to new location 

# python list can hold elements of different type

data = [10,'A',123.34,"Hello", """Hello world"""]
for i in range(0,4):
    print(data[i])

  
 


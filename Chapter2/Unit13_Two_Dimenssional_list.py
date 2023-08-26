#From page 229 - 

print('Page: 229')
list = [[1,2,3],[4,5,6],[7,8,9]]
for item in list:
    print('Item', item)

print('-'*15)

print('Page: 230')
list = [[1,2,3],[4,5,6],[7,8,9]]
for a,b,c in list:
    print('Item', a,b,c)


#--->This is the error one cuz in list eexactly must have three item the same

# list = [[1,2,3],[4,6],[7]]
# for a,b,c in list:
#     print('Item', a,b,c)

print('-'*15)

print('Page: 232')
list = [[1,2,3],[4,5,6],[7,8,9]]
for a in list:
    for b in a:
        print(b, end='  ')
    print()
#
print('-'*15)

print('Page: 233')
list = [[1,2,3],[4,5],[5]]
for a in list:
    for b in a:
        print(b, end='  ')
    print()
#
print('\n','-'*15)

print('Page: 244')
print('Quiz\n')

list = [[10,20],[30,40],[50,60]]
print('Output   :   ',list[1][0])
#
print('\n','-'*15)
print('Page: 245')
print('Quiz\n')

for i in range (1,17,4):
    for j in range (i, i+4):
        print(j, end='  ')
    print()
#New--------------------------------
print('\n','-'*26)
print('\tPage:    247')


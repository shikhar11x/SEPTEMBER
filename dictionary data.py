name1=['ram','ratan','raj','sita','shubh','ad','priyanshu','yugi','yuvraj','saurabh','sid','puneet']
age=[18,17,19,0,20,16,17,18,16,10,17,19]
phn=[11111,22222,33333,44444,55555,66666,77777,88888,99999,1010,1111,1212]
rln=[1,2,3,4,5,6,7,8,9,10,11,12]
classs={'name':name1,
        "age":age,
        'phone no':phn,
        'roll no':rln}
a=classs.get('roll no')
a1=classs.get('name')
b=len(a)
for i in range(b):
    c=a[i]
    c1=a1[i]
    if c<4:
        print("your name is",c1,"and roll no is",c,"you are in row 1")
    elif 4<c<8:
        print("your name is",c1,"and roll no is",c,"you are in row 2")
    else:
        print("your name is",c1,"and roll no is",c,"you are in row 3")

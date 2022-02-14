#INTRO TO COMPUTING ASSIGNMENT-3


#Q1
def occurence_counter(string):                      #DEFINING A NEW FUNCTION TO COUNT THE NUMBER OF WORDS IN A STRING
    def character_counter(stng):
        output_list=[]
        for i in stng:
            count=stng.count(i)
            output_list.append('Number of occurences of {} : {}\n'.format(i,count))

        for o in set(output_list):
            print(o+'\n')

    def substring_counter(stn):                     #DEFINING A FUNCTION FOR SINGLE LETTER WORDS
        for i in set(lst):
            print('Number of occurences of',i,':',lst.count(i),'\n')

    lst=string.split()
    if len(lst)==1:
        character_counter(string)
    elif len(lst)==0:
        print('Empty string input')
    else:
        substring_counter(string)

string1=input('Input string:')                      #TAKING INPUT FROM USER

print()
occurence_counter(string1)


print(100*'*')


#Q2
#TAKING INPUT OF YEAR FROM USER AND CHECKING IF IT IS LEAP YEAR OR NOT:-
year=int(input('Enter any year: '))

if (year%400==0):
    leap_year=True

elif(year%100==0):
    leap_year=False

elif(year%4==0):
    leap_year=True

else:
    leap_year=False


#TAKING INPUT OF MONTH FROM USER AND CHECKING HOW MANY DAYS IT WOULD HAVE
month=int(input('Enter a month[1-12]: '))

if month is (1,3,5,7,8,10,12):
    month_length=31

elif month==2:
    if leap_year:
        month_length=29
    else:
        month_length=28

else:
    month_length=30


#TAKING INPUT OF DAY FROM USER
day=int(input('Enter a day[1-31]: '))

if day<month_length:
    day+=1

else:
    day=1
    if month==12:
        month=1
        year+=1
    else:
        month_length=30


#TAKING INPUT OF DAY FROM THE USER
day=int(input('Enter a day[1-31]: '))

if day<month_length:
    day+=1

else:
    day=1
    if month==12:
        month=1
        year+=1
    else:
        month+=1


#PRINTING OUT THE NEXT DATE FROM THE DATE ENTERED BY THE USER
print('THE NEXT DATE IS [YYYY/MM/DD]] %d-%d-%d.'%(year,month,day))



print(100*'*')



#Q3
n=int(input('Enter the count of numbers you want to square: '))         #TAKING USER INPUT 
final_list=[]

for i in range(n):                                      #USING 'FOR' LOOP TO CREATE MULTIPLE TUPLES
    x=int(input('Enter a number: '))
    y=x**2
    tuple_=(x,y)

    final_list.append(tuple_)                           #APPEND FUNCTION ADDS NEW ENTRY TO THE LIST

print(final_list)



print(100*'*')



#Q4
grade_point=int(input('Grade of user is: '))                            #USING IF/ELSE FUNCTION TO CREATE DIFFERENT CASES OF GRADE POINT AND ASSIGNING DIFFERENT VIEWS TO RESPECTIVE GRADE POINTS
    

if grade_point==10:
    print('Your grade is A+ and performance is outstanding')

elif grade_point==9:
    print('Your grade is A and performance is excellent')

elif grade_point==8:
    print('Your grade is B+ and performance is very good')

elif grade_point==7:
    print('Your grade is B and performance is good')

elif grade_point==6:
    print('Your grade is C+ and performance is average')

elif grade_point==5:
    print('Your grade is C and performance is below average')

elif grade_point==4:
    print('Your grade is D and performance is poor')

else:
    print('Grade is out of range')


print(100*'*')



#Q5
i=0
a='ABCDEFGHIJK'

for i in range(6):
    j=i

    while(j>0):
        print(' ',end="")
        j=j-1

    k=0
    for k in range(len(a)-2*i):
        print(a[k],end="")

    print("")


print(100*'*')


#Q6
condition=True

dictionary={}               #DEFINING DICTIONARY TO STORE VALUES
prompt='y'

while condition:                    
    if prompt.lower()=='y':                                             #USING IF/ELSE 
        name=input('Please enter the name of the student: ')
        SID=int(input('Please enter student ID: '))
        dictionary[SID]=name
        prompt=input('If you want to enter more information enter Y/N: ')
        condition=True

    else:
        condition=False

for key,value in dictionary.items():            #USING FOR LOOP 
    print(f"{key} : {value}")                           #USING F-STRINGS TO PRINT DICTIONARY ENTRIES

Val_sort_dict=sorted(dictionary.values())
Name_sort={}

def get_key(val, dicti):
    for key,value in dicti.items():
        if val==value:
            return key

for s_name in Val_sort_dict:
    s_sid = get_key(s_name, dictionary)
    Name_sort[s_sid] = s_name

print(Name_sort)

Key_sort_dict=sorted(dictionary.keys())
dict={}

for i in Key_sort_dict:
    dict[i]=dictionary[i]
print(dict)

sid=int(input('Please enter the student"s SID whose information you require: '))            #TAKING INPUT FROM USER

if sid in dictionary.keys():
    print(f'Name of the required student is {dictionary[sid]}')
else:
    print('The SID is not present in the given Data')

print()



print(100*'*')



#Q7
# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))


print(100*'*')


#Q8
set1={1,2,3,4,5}                    #USING SET FUNCTIONS TO GET DESIRED OUTPUT
set2={2,4,6,8}
set3={1,5,9,13,17}
let_another_set={1,2,3,4,5,6,7,8,9,10}

#(A)                                    
set_new_a=(set1|set2)-(set1&set2)               #USING UNION,INTERSECTION AND SUBTRACT SET FUNCTIONS
print('Required set is',set_new_a)

#(B)
set_new_b=(set1|set2|set3)-(set1&set2&set3)-(set1&set2)-(set2&set3)-(set1&set3)
print('Required set is',set_new_b)

#(C)
set_new_c=((set1&set2)|(set2&set3)|(set3&set1))-(set1&set2&set3)
print('Required set is',set_new_c)

#(D)
set_new_d=(let_another_set)-(set1)
print('Required set is',set_new_d)

#(E)
set_new_e=(let_another_set)-(set1)-(set2)-(set3)
print('Required set is',set_new_e)



print(100*'*')

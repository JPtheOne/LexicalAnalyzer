#Lexical Analyzer
#@ JPtheOne
  
#Dictionary that defines the type of tokens
lexical_category = {
"+":"Token lexical category: ADDITION",
"-":"Token lexical category: SUBTRACTION",
"/":"Token lexical category: DIVISION",
"*":"Token lexical category: MULTIPLICATION",
"%":"Token lexical category: MODULE",
}

#Separate the expressions with spaces, they will be eliminated after analyzing
input_array =  input("Please type the string to be evaluated: ")
c_array = input_array.split()
print(c_array)

#A loop is implemented to traverse all the string
for i in c_array:
    print("Given token:",i)
    
    e = i.isalpha()
    h = i.isdigit()

    if(e==True):
        print("Token lexical category: VARIABLE")
    elif(h == True):
        print("Token lexical category: CONSTANT")
    else:
        lexical_category2=lexical_category.get(i)
        print(lexical_category2)

#1. Creating a list 
fruits = ["apple","mango","stawberry","pineapple","watermelon"] #Creating a list of 5 fruits
print(fruits) #prints the output of fruits in the list

#2. Accessing Elements
colors = ['red','blue','green','yellow','purple'] #Creating a list of colors
print(colors[0], colors[2], colors[4]) #Prints the first, third and fifth value of the list

#3. Modifying a List
numbers=[10,20,30,40,50] #Creating a list of numbers
print(numbers) #Prints the list of numbers
numbers.insert(1,25) #Replacing the second element with 25
numbers.append(60) #A new value is ended in the end of the list
print(numbers) #Prints the edited list

#4. List Slicing
names=['Alice','Bob','Charlie','David','Emma'] #Creating a list of names
subset= names[0:3] #Slicing the list by choosing first 3 values
print(subset) #prints the first 3 values

#5. Looping through Lists
numbers=[1,2,3,4,5,6,7,8,9,10] #Creating a list numbers
for i in numbers: #Using loops to square the list
    print("The square of",i,"is",i*i) #prints the value of squared numbers

#6. List Methods: Append and Extend
shopping_cart=[] #Creating an empty list
shopping_cart.append('milk') #Adding new values
shopping_cart.append('bread') #Adding new values
shopping_cart.append('eggs') #Adding new values
shopping_cart1=['butter','cheese'] #making a new list for extend function
shopping_cart.extend(shopping_cart1) #extending the list with new values using extend function
print(shopping_cart) #prints the new list

#7. Find Maximum and Minimum is a List 
numbers = [45,22,88,56,92,33] #Creating a list of random numbers
print("Maximum value:",max(numbers)) #Prints the highest number
print("Minimum Value:",min(numbers)) #Prints the lowest number

#8.Counting Occurences
letters=['a','b','a','c','b','a','d'] #Creating a list with random letters
count_of_a=letters.count('a') #using the count function to find the number of a in the list
print("Count of a:",count_of_a) #prints the count of a

#9. List Comprehension
even_squares=[i**2 for i in range(0,11,2)] #Using list comprehension to find the squares for even numbers
print("The squares of even numbers from 1 to 10 are",even_squares) #prints the squares of even numbers

#10. Removing Duplicates
nums=[1,2,2,3,4,4,5,6,6,7] #Creating a list with duplicate numbers
nums= list(dict.fromkeys(nums)) #This function removes the duplicate values in the list
print(nums) #Prints the list without the duplicate values
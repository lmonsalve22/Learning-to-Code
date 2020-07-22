""" Think of at least five places
1. store in a list 
2. print the list
3. use sorted() to print in alphabetical order
4. show that your list is still in its original order
5. use sorted() to print in reverse alphabetical order
6. print the list
7. use reverse() to change the order and print it
8. use reverse() again to change the order and print it
9. use sort() to print in alphabetical order
10. use sort() to print in reverse alphabetical order"""

places = ['san francisco', 'london', 'paris', 'cuzco', 'guayaquil'] #1

print(places) #2

print(sorted(places)) #3

print(places) #4

print(sorted(places, reverse=True)) #5

print(places) #6

places.reverse() #7
print(places)

places.reverse() #8
print(places)

places.sort() #9
print(places)

places.sort(reverse=True) #10
print(places)
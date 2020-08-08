""" Make three dictionaries representing different people, and
store all three dictionaries in a list called people. Loop through
your list of people. As you loop through the list, print everything
you know about each person """

people = []

person = {
    'first_name': 'james',
    'last_name': 'noria',
    'age': 25,
    'city' : 'huanuco'
}
people.append(person)
person1 = {
    'first_name': 'carolina',
    'last_name': 'noria',
    'age': 4,
    'city' : 'cajamarca'
}
people.append(person1)
person2 = {
    'first_name': 'cynthya',
    'last_name': 'tirado',
    'age': 27,
    'city' : 'san marcos'
}
people.append(person2)

for person in people:
    first = person['first_name'].title() 
    last = person['last_name'].title()
    age = person['age']
    city = person['city'].title()
    print(f'Name: {first} {last}\nAge: {age}\nCity: {city}\n')
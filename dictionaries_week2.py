"""
Dictionaries
Problem 3: Create a dictionary to store the names and ages of 5 people. Write a function to:
-Add a new person to the dictionary.
-Remove a person from the dictionary by name.
-Print the average age of the people in the dictionary.
"""
people = {"Alice": 30,"Bob": 25,"Charlie": 35,"Diana": 28,"Ethan": 40}
#starting dictionary
print("Initial dictionary:", people)

#adds a new person to the distionary
def add_person(dictionary, name, age):
    dictionary[name] = age
    print("Added " + name + " with age " + str(age))

#removes a person from the dictionary
def remove_person(dictionary, name):
    if name in dictionary: #if it finds the name in the dictionary it will remove that name and age
        del dictionary[name] #removes the name
        print("Removed " + name)
    else: #when name is not present in the dictionary
        print(name + " not found in the dictionary.")

#finds average age
def print_average_age(dictionary):
    if dictionary: #looks through dictionary to find the average age
        average_age = sum(dictionary.values()) / len(dictionary)
        print("The average age is " + str(average_age) )
        
#adds a new person
add_person(people, "Fiona", 22)
#removes the name called to remove
remove_person(people, "Charlie")
#prints average age
print_average_age(people)
#people after the dictionary is change
print("Final dictionary:", people)

print()
"""
Problem 4: Given a dictionary with student names as keys and their scores as values, write a function to:
-Print the name of the student with the highest score.
-Print the names of all students who scored above 80.
"""
#lists of students 
students = {"Alice": 98,"Bob": 70,"Charlie": 83,"Diana": 92,"Ethan": 89}
print("Initial Students: " , students)

#prints the highest score
def print_highest_score():
    highest_score_student = max(students, key=students.get) #uses max to find highest score
    highest_score = students[highest_score_student]
    print("The student with the highest score is "+ highest_score_student + " with a score of " + str(highest_score))

#prints those who get above 80
#creates a list of those whose score is above 80
def print_above_80():
    above_80_students = [name for name, score in students.items() if score > 80]
    print("Students who scored above 80:", ", ".join(above_80_students))

#runs highest score function
print_highest_score()
#runs above 80 function
print_above_80()
    
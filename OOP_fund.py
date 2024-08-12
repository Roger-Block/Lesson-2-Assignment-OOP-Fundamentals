                    #================================================================
                    #========= Lesson 2: Assignment | OOP Fundamentals===============
                    #================================================================

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ # 1. City Infrastructure Management System ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Objective: 
    # The aim of this assignment is to apply the concepts of Object-Oriented Programming in Python to build a simulated City Infrastructure Management System. This system will incorporate classes, objects, methods, and data structures to manage different aspects of a city, such as buildings, traffic, and events.

# Task 1: 
    # Vehicle Registration System

# Problem Statement: 
    # Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.

# Code Example: 
    # Provide a basic structure for the Vehicle class without methods.
        # class Vehicle:
        #     def __init__(self, reg_num, type, owner):
        #         self.registration_number = reg_num
        #         self.type = type
        #         self.owner = owner

# Expected Outcome:
    # Completion of the Vehicle class with the update_owner method and a demonstration script showing the creation of Vehicle objects and updating their owners.

#=============================================================================================================================

# Task 2: 
    # Event Management System Enhancement

# Problem Statement:
    # Use the existing Event class by adding an attribute to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.

# Code Example: 
    # Basic Event class without participant tracking.
        # class Event:
        #    def __init__(self, name, date):
        #         self.name = name
        #         self.date = date

#================================================================================================
#=====================================Begin Code=================================================
#================================================================================================

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner


vehicle1 = Vehicle("ABC123", "Car", "John")
vehicle2 = Vehicle("XYZ789", "Motorcycle", "Jane")

print("Before owner update:")
print("Vehicle 1 owner:", vehicle1.owner)
print("Vehicle 2 owner:", vehicle2.owner)

vehicle1.update_owner("David")
vehicle2.update_owner("Emily")

print("\nAfter owner update:")
print("Vehicle 1 owner:", vehicle1.owner)
print("Vehicle 2 owner:", vehicle2.owner)

#================================================================================================
#=================================== End of Code=================================================
#================================================================================================


# Author: Roger Block
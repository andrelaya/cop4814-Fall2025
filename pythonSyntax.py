"""
Basic Python Syntax
----------------------------
This file is a guided template for learning Python basics.
Students should fork and clone this repository from Greg's repo.
Explanations and examples will be added by Greg.
"""

# ==========================================================
# 1. PRINTING AND COMMENTS
# ----------------------------------------------------------
# - Print statements
# - Single-line comments
# - Multi-line comments (docstrings)
# ==========================================================

# this is how we print in python
print("Andre", 3.14, 10)

"""
this is a 
block comment
"""

# ==========================================================
# 2. VARIABLES AND DATA TYPES
# ----------------------------------------------------------
# - Strings
# - Integers, floats
# - Booleans
# - Type checking with type()
# ==========================================================

message = "Welcome to FIU"
print(type(message)) #type() is a function too

a = 10
b = 2
print(type(a),type(b))

isOpen = True
print(type(isOpen))


print(message[8])
# ==========================================================
# 3. BASIC OPERATORS
# ----------------------------------------------------------
# - Arithmetic (+, -, *, /, //, %, **)
# - Comparison (==, !=, >, <, >=, <=)
# - Logical (and, or, not)
# ==========================================================

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(7/2)
print(7//2) #integer division
print(a**b) #exponential
print(7%2) #modulus (remainder of the divison)



# ==========================================================
# 4. STRING OPERATIONS
# ----------------------------------------------------------
# - Concatenation
# - f-strings
# - Common methods (.upper(), .lower(), .strip(), etc.)
# ==========================================================

first_name = "Andre"
last_name = "Laya"

print(first_name + last_name)
print(first_name + " " + last_name)
print(first_name, last_name)

print(f"My name is {first_name.upper()} {last_name.title()}.")
print("2" + "3")
print("***Welcome to Software Dev***".strip('*'))

# ==========================================================
# 5. LISTS
# ----------------------------------------------------------
# - Creating lists
# - Indexing and slicing
# - Adding/removing elements
# - Useful methods (.append(), .remove(), .sort(), etc.)
# ==========================================================



professors = ["greg", "richard", "kianoosh", "debra", "jason", "leo", "heather"]
print(type(professors))
print(professors[0])
print(professors[-1])
print(professors[2:5]) # accessing indices 2, 3, and 4
print(professors[:5]) # accessing from index 0 to 4
print(professors[3:]) # accessing from 3 to the end
print(professors[:])


professors.append("todd")
print(professors)
professors.extend(["michael", "mustafa", "naomi"])
print(professors)
professors.insert(2,"vyoma")
professors.remove("greg")
print(professors)
x=professors.pop(2)
print(professors, x)
professors.reverse()
print(professors)

professors.sort()
print(professors)
professors.sort(reverse=True)
print(professors)
#done
# ==========================================================
# 6. TUPLES AND SETS
# ----------------------------------------------------------
# - Tuples: immutable sequences
# - Sets: unique collections
# ==========================================================

grades = (88.3, 78.6, 99.5)
print(type(grades))
#grades[0] = 91.3

members = {"greg", "richard", "greg"}
print(members) # this is going to ve the answer of a future assignment -----------




# ==========================================================
# 7. DICTIONARIES
# ----------------------------------------------------------
# - Key-value pairs
# - Accessing and modifying values
# - Common methods (.keys(), .values(), .items())
# ==========================================================



# ==========================================================
# 8. CONDITIONALS
# ----------------------------------------------------------
# - if, elif, else
# - Nested conditionals
# ==========================================================



# ==========================================================
# 9. LOOPS
# ----------------------------------------------------------
# - for loops
# - while loops
# - break and continue
# ==========================================================



# ==========================================================
# 10. FUNCTIONS
# ----------------------------------------------------------
# - Defining functions
# - Parameters and return values
# - Default arguments
# ==========================================================



# ==========================================================
# 11. IMPORTING MODULES
# ----------------------------------------------------------
# - Importing built-in modules (e.g., math, random)
# - Using functions from modules
# ==========================================================



# ==========================================================
# 12. ERROR HANDLING (OPTIONAL)
# ----------------------------------------------------------
# - try, except
# - Handling different exception types
# ==========================================================




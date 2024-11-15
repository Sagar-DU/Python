import math

# Question 1
# In the House Prices - Advanced Regression Techniques competition, you need to use information like the number of bedrooms and bathrooms to predict the price of a house. Inspired by this competition, you'll write your own function to do this.

# In the next code cell, create a function get_expected_cost() that has two arguments:

# beds - number of bedrooms
# baths - number of bathrooms
# It should return the expected cost of a house with that number of bedrooms and bathrooms. Assume that:

# the expected cost for a house with 0 bedrooms and 0 bathrooms is 80000.
# each bedroom adds 30000 to the expected cost
# each bathroom adds 10000 to the expected cost.
# For instance,

# a house with 1 bedroom and 1 bathroom has an expected cost of 120000, and
# a house with 2 bedrooms and 1 bathroom has an expected cost of 150000.

def get_expected_cost (beds, baths):
    value = 80000 + (30000 * beds) + (10000 * baths)
    
    return value

# Question 2
# You are thinking about buying a home and want to get an idea of how much you will spend, based on the number of bedrooms and bathrooms. You are trying to decide between four different options:

# Option 1: house with two bedrooms and three bathrooms
# Option 2: house with three bedrooms and two bathrooms
# Option 3: house with three bedrooms and three bathrooms
# Option 4: house with three bedrooms and four bathrooms

option1 = get_expected_cost (2, 3)
option2 = get_expected_cost (3, 2)
option3 = get_expected_cost (3, 3)
option4 = get_expected_cost (3, 4)

print ("The cost for 2 bed and 3 bath is:", option1)
print ("The cost for 3 bed and 2 bath is:", option2)
print ("The cost for 3 bed and 3 bath is:", option3)
print ("The cost for 3 bed and 4 bath is:", option4)

# Question 3
# You're a home decorator, and you'd like to use Python to streamline some of your work. Specifically, you're creating a tool that you intend to use to calculate the cost of painting a room.

# As a first step, define a function get_cost() that takes as input:

# sqft_walls = total square feet of walls to be painted
# sqft_ceiling = square feet of ceiling to be painted
# sqft_per_gallon = number of square feet that you can cover with one gallon of paint
# cost_per_gallon = cost (in dollars) of one gallon of paint

def get_cost(sqft_walls, sqft_ceilling, sqft_per_gallon, cost_per_gallon):
    cost = ((sqft_walls + sqft_ceilling) / sqft_per_gallon) * cost_per_gallon

    return cost

# Question 4
# Use the get_cost() function you defined in Question 3 to calculate the cost of applying one coat of paint to a room with:

# 432 square feet of walls, and
# 144 square feet of ceiling.
# Assume that one gallon of paint covers 400 square feet and costs $15. As in Question 3, assume you can buy partial gallons of paint. Do not round your answer.

prject_cost = get_cost (432, 144, 400, 15)
print ("The prject cost is:", prject_cost)

# Question 5
# Now say you can no longer buy fractions of a gallon. (For instance, if you need 4.3 gallons to do a project, then you have to buy 5 gallons of paint.)

# With this new scenario, you will create a new function get_actual_cost that uses the same inputs and calculates the cost of your project.

# One function that you'll need to use to do this is math.ceil(). We demonstrate usage of this function in the code cell below. It takes as a number as input and rounds the number up to the nearest integer.

def get_actual_cost (sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    gallon = (sqft_walls + sqft_ceiling) / sqft_per_gallon
    gallon_to_buy = math.ceil(gallon)
    cost = gallon_to_buy * cost_per_gallon

    return cost

print ("The actual cost for the projcect is:", get_actual_cost(432, 144, 400, 15))

# Data Type Question 5
# You own an online shop where you sell rings with custom engravings. You offer both gold plated and solid gold rings.

# Gold plated rings have a base cost of $50, and you charge $7 per engraved unit.
# Solid gold rings have a base cost of $100, and you charge $10 per engraved unit.
# Spaces and punctuation are counted as engraved units.
# Write a function cost_of_project() that takes two arguments:

# engraving - a Python string with the text of the engraving
# solid_gold - a Boolean that indicates whether the ring is solid gold

def cost_of_project (engraving, solid_gold):
    if (solid_gold == True):
        cost = 100 + 10 * len (engraving)
    else:
        cost = 50 + 7 * len (engraving)
    
    return cost

print (cost_of_project("Charlie-Denvar", True))
print (cost_of_project("08/10/2000", False))

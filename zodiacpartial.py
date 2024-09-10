# Write a program that reads a year from the user and outputs the Chinese zodiac animal assigned to that year. The Chinese zodiac
# repeats every 12 years.
# Year 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011
# Animal Dragon Snake Horse Sheep Monkey Rooster Dog Pig Rat Ox Tiger Hare

# Dragon 2000 2012 2024 2036

# for each animal take the modulo

# take year % 12 because the pattern repeats every 12 years

# n % 5 -> 0, 1, 2, 3, 4

year = int(input("Enter year: "))

remainder = year % 12

if remainder == (2000 % 12):
    print("Dragon")
elif remainder == (2001 % 12):
    print("Snake")
elif remainder == (2002 % 12):
    print("Horse")
elif remainder == (2003 % 12):
    print("Sheep")

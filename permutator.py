# Ask the user to enter a list of names separated by a space
names = input("Inserisci una lista di nomi separati da uno spazio: ").split(" ")

# Generate a list of ASCII symbols
symbols = [chr(i) for i in range(33, 65)]

# For each name of the list
for name in names:
  # ...add a numeric sequence of 4 digits from 0000 to 9999
  for i in range(10000):
    # Format the number as a 4-digit string with leading zeros
    number = "{:04d}".format(i)

    # For each ASCII symbol...
    for symbol in symbols:
      # ...combine the name, number and symbol without spaces or punctuation and print the result on a new line
      result = name + number + symbol
      print(result)

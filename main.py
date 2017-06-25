__author__ = "Mr Bancroft"                                  # Author name

greeting = "Hello "                                         # Creates a variable called greeting, note space after text
name = input("Please enter your name: ")                    # Creates a variable called input and get the value from
                                                            # the command prompt
print(greeting + name)                                      # Prints the greeting and input variables after joining them
multilineString = "This string has\nbeen split over\nthree lines."  # Creates a string variable with newlines (\n) in
print(multilineString)                                      # Prints the variable holding the multiline string
anotherMultilineString = """This string has                   
been split over
three lines."""                                             # Creates a string variable over multiple lines without \n
print(anotherMultilineString)                               # Prints the second multiline string
tabbedString = "\tThis text has a tab at the start"         # Creates a string variable with tabs (\t) in
print(tabbedString)                                         # Prints the variable holding the tabbed string
escapedString = "I said \"Not now, " + name + "\", I did"   # Creates a string with escaped characters (\")
print(escapedString)                                        # Prints the escaped string
mixedQuotes = '''I said "e's not imself, I tell thee"'''    # Use triple quotes (''',""") to allow double and single ones
print(mixedQuotes)                                          # Prints the mixed quote string

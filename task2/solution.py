first_name, last_name = input("Enter first and last name of the person: ").split()

example1 = "Person first name is {0}, and the last name is {1}".format(first_name, last_name)
example2 = "Person first name is {}, and the last name is {}".format(first_name, last_name)
example3 = "Person first name is {f}, and the last name is {l}".format(f=first_name, l=last_name)

print(example1)
print(example2)
print(example3)

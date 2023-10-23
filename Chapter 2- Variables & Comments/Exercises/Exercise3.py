# Representing a person's name with whitespace characters
person_name_with_whitespace = "\t  Ahmad\n"

# Printing the name with whitespace characters
print("Name with whitespace characters:")
print(person_name_with_whitespace)

# Using lstrip() to remove leading whitespace
name_lstrip = person_name_with_whitespace.lstrip()

# Using rstrip() to remove trailing whitespace
name_rstrip = person_name_with_whitespace.rstrip()

# Using strip() to remove both leading and trailing whitespace
name_strip = person_name_with_whitespace.strip()

# Printing the names after stripping whitespace
print("Name after lstrip():", name_lstrip)
print("Name after rstrip():", name_rstrip)
print("Name after strip():",name_strip)
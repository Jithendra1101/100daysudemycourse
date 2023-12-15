def format_name(first_name,last_name) :
    first_name = first_name.title()
    last_name = last_name.title()
    return f"{first_name} {last_name}"

hello = format_name("jithendra","varma")
print(hello)
try:
    file = open("data.txt")
    data_dict = {"key":"value"}
    value = (data_dict["key"])
except FileNotFoundError:
    file = open("data.txt","w")
    file.write("Bhavya Pandurangan")
except KeyError as message:
    print(f"{message} not in the dictionary")
else:
    print(value)
    content = file.read()
    print(content)
finally:
    raise IndexError("Index out of range.")
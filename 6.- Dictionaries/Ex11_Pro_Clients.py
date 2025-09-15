# A company's customer directory is organized in a text string like the one below, where each line contains information such as name, email, phone number, tax ID, and the applicable discount. Lines are separated by the newline character \n, and the first line contains the field names containing the information contained in the directory.

# "nif;name;email;phone;discount\n01234567L;Luis Gonzalez;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramirez;macarena@mail.com;692839321;8\n63823376M;Juan Jose Martinez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sanchez;carmen@mail.com;667677855;15.7"

# Write a program that generates a dictionary with the directory information, where each element corresponds to a customer and has its tax ID as its key and another dictionary with the rest of the customer's information as its value. The dictionaries with the information of each client will have the names of the fields as keys and the information of each client corresponding to the fields as values. That is, a dictionary like the following:

# {'01234567L': {'name': 'Luis Gonzalez', 'email': 'luisgonzalez@mail.com', 'phone': '656343576', 'discount': 12.5}, '71476342J': {'name': 'Macarena Ramirez', 'email': 'macarena@mail.com', 'phone': '692839321', 'discount': 8.0}, '63823376M': {'name': 'Juan Jose Martinez', 'email': 'juanjo@mail.com', 'phone': '664888233', 'discount': 5.2}, '98376547F': {'name': 'Carmen Sanchez', 'email': 'carmen@mail.com', 'phone': '667677855', 'discount': 15.7}}

print("")
information = {}

people = "nif;name;email;phone;discount\n01234567L;Luis Gonzalez;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramirez;macarena@mail.com;692839321;8\n63823376M;Juan Jose Martinez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sanchez;carmen@mail.com;667677855;15.7"

print("")

list_of_people = people.split('\n')
list_of_fields = list_of_people[0].split(';')

for i in list_of_people[1:]:
    client = {}
    list_of_info = i.split(';')
    for j in range(1,len(list_of_fields)):
        if list_of_fields[j] == 'discount':
            list_of_info[j] = float(list_of_info[j])
        client[list_of_fields[j]] = list_of_info[j]
    information[list_of_info[0]] = client

print(information)
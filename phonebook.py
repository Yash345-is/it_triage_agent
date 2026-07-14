phonebook = {

"Sara": "9876543210",

"David": "9123456780",

"Surya": "9988776655"

}

print(phonebook) # prints original phonebook

name = input("Enter a name from the phonebook:")

print(phonebook.get(name,'Not found'))



delete_name = input("Enter a name to delete:")

if delete_name in phonebook:
    del phonebook [delete_name]
    print(delete_name,"deleted succesfully")
    print("Updated phonebook:",str(phonebook))

else:
    print("User not found!")


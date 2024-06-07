#Assign 'import_file' to the nam eof the file
import_file = "allow_list.txt"

#Build 'with' statement to read in the initial contentsof the file
with open(import_file, "r") as file:

    #Use '.read()' to read the imported file and store it in a variable named 'ip_adresses'

    ip_adresses = file.read()

#Use '.split()' to convert 'ip_adresses' from a string to a list

ip_adresses = ip_adresses.split()

#Build iterative statement
#Name loop variable 'element'
#Loop through 'remove_list'

for element in remove_list:

    #Create conditional statement to evaluate if 'element' is in 'ip_adresses'

    if element in ip_adresses:

        #use the '.remove()' method to remove elements from 'ip_adresses'

        ip_adresses.remove(element)

#Convert 'ip_adresses' back to a string so that it can be written into the text file

ip_adresses = "\n".join(ip_adresses)

#Build 'with' statement to rewrite the original file

with open(import_file, "w") as file:

    #Rewerite the file, replacing its contents with 'ip_adresses'

    file.write(ip_adresses)

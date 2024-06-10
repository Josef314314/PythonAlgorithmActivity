<h1>Python - Algorithm for file updates</h1>

<h2>Project description</h2>
This is a simulation of an organization, whereby access to restricted content is controlled using an allow list of IP addresses. The "allow_list.txt" file identifies these IP addresses. An additional remove list contains IP addresses that should no longer have access to this content. I created an algorithm that automatically updates the "allow_list.txt" file to remove these IP addresses.
<br />


<h2>Language</h2>

- <b>Python (3)</b> 

<h2>Environment Used </h2>

- <b>Jupyter Notebook

<h2>Program walk-through:</h2>

- <b>Open the file that contains the allow list:</b>

For the first part of the algorithm, I opened the "allow_list.txt" file. Here is where I first assigned this file name as a string to the import_file variable: <br/>
<p align="center">
<img src="https://i.imgur.com/oHIWiLi.png" height="40%" width="40%" alt="PythonAlgorithm"/>
<br />
<br />
<p align="left">
Then, I used a with statement to open the file:  <br/>
<p align="center">
<img src="https://i.imgur.com/5hIZxjo.png" height="50%" width="50%" alt="PythonAlgorithm"/>
<br />
<p align="left">
In the this algorithm, the with statement is used with the .open() function in read mode opens the allow list file for reading purposes. It allows me to access the IP addresses stored in the allow list file. The with keyword will help manage the resources by closing the file after exiting the with statement.
<br />
<br />
  
- <b>Read the file contents:</b>

In order to read the file contents, I used the .read() method to convert it into the string: <br/>
<p align="center">
<img src="https://i.imgur.com/quH8FIR.png" height="60%" width="60%" alt="PythonAlgorithm"/>
<br />

<p align="left">
The .read() method converts the file into a string and allows me to read it. I have called the .read() function in the body of the with statement. Then, I assigned the string output of this method to the variable ip_addresses. <br />
<br />
In summary, this code reads the contents of the "allow_list.txt" file into a string format that allows me to later use the string to organize and extract data in my Python program.
<br />
<br />

- <b>Convert the string into a list:</b>

I wanted it in list format so that I could individually delete IP addresses from the allow list. So next, I used the .split() method to turn the ip_addresses string into a list:  <br/>
<p align="center">
<img src="https://i.imgur.com/qlnqOrv.png" height="50%" width="50%" alt="PythonAlgorithm"/> <br/>
<p align="left">
The purpose of splitting ip_addresses into a list is to make it easier to remove IP addresses from the allow list. By default, the .split() function splits the text by whitespace into list elements. In this algorithm, the .split() function takes the data stored in the variable ip_addresses, which is a string of IP addresses that are each separated by a whitespace, and it converts this string into a list of IP addresses. To store this list, I reassigned it back to the variable ip_addresses.
<br />
<br />

- <b>Iterate through the remove list:</b>

A crucial part of my algorithm is to iterate over the elements of the list, which in our case are IP addresses. To do this, I incorporated a for loop: <br/>
<p align="center">
<img src="https://i.imgur.com/MXpN4At.png" height="34%" width="34%" alt="PythonAlgorithm"/> <br />
<p align="left">
The overall purpose of the for loop in a Python algorithm like this is to apply specific code statements to all elements in a sequence. After the for keyword, there is the loop variable element, followed by the keyword in. That indicates to iterate through the sequence ip_addresses and assign each value to the loop variable element. 
<br />
<br />

- <b>Remove IP addresses that are on the remove list:</b>

My algorithm requires removing any IP address from the allow list, ip_addresses, that is also contained in remove_list.  As there was no duplication in ip_addresses, I was able to use the following code to do this:  <br/>
<p align="center">
<img src="https://i.imgur.com/zgxvjL5.png" height="55%" width="55%" alt="PythonAlgorithm"/> <br />
<p align="left">
First, within my for loop, I created a conditional that evaluated whether or not the loop variable element was found in the ip_addresses list. I did this because applying .remove() to elements that were not found in ip_addresses would result in an error. <br />
Then, within that conditional, I applied .remove() to ip_addresses. I passed in the loop variable element as the argument so that each IP address that was in the remove_list would be removed from ip_addresses.
<br />
<br />

- <b>Update the file with the revised list of IP addresses:</b>

As a final step, I needed to update the allow list file with the revised list of IP addresses. To do so, I first needed to convert the list back into a string. I used the .join() method for this:  <br/>
<p align="center">
<img src="https://i.imgur.com/QvwRrsT.png" height="60%" width="60%" alt="PythonAlgorithm"/> <br />
<p align="left">
I used the .join() method in order to join all elements of list ip_addresses into a string so that I could pass it as an argument to the .write() method when writing to the file "allow_list.txt". I made use of the string ("\n") as a separator to instruct Python to place each element on a new line.  <br />
Then, I used another with statement and the .write() method to update the file: <br/>
<p align="center">
<img src="https://i.imgur.com/DzHCJMb.png" height="45%" width="45%" alt="PythonAlgorithm"/> <br />
<p align="left">
This time, I used a second argument of "w" with the open() function in the with statement to call the .write() function in the body of the with statement. The .write() function writes string data to a specified file and replaces any existing file content. <br />
In this case I wanted to write the updated allow list as a string to the file "allow_list.txt". This way, the restricted content will no longer be accessible to any IP addresses that were removed from the allow list.
<br />
<br />

<h2>Summary:</h2>

I created an algorithm that removes IP addresses identified in a remove_list variable from the "allow_list.txt" file of approved IP addresses. This algorithm involved opening the file, converting it to a string to be read, and then converting this string to a list stored in the variable ip_addresses. I then iterated through the IP addresses in remove_list. With each iteration, I evaluated if the element was part of the ip_addresses list. If it was, I applied the .remove() method to it to remove the element from ip_addresses.. After this, I used the .join() method to convert the ip_addresses back into a string so that I could write over the contents of the "allow_list.txt" file with the revised list of IP addresses.

</p>

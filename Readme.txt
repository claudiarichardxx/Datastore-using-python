A file based Data Store using python:

In this program,the entire Data Store is saved as a dictionary in a json file.Through this way, Key- Value pairs can be stored easily. The key is a string and the value is a json object. There is a key associated with every json object. The json object is typically of the format {"Attribute1":"Value1","Attribute2":"Value2"} containing attribute-value pairs.A string in this format is given as the input to store in the Data Store. This string is then parsed through the json.loads function to decode it into a json object. The json.load and json.dumps functions in the json module is used to perform the read and write operations.

Create function:
If the .json file already exists, the existing file is opened. Else, a new .json file with the given name is created. The dictionary is first read from the file and stored in an object. The key and the json object are received and updated into the dictionary and finally, the dictionary is written back into the .json file.

Read function:
The dictionary is first read from the file and stored in an object. The json object corresponding to the entered key is found and displayed.

Delete function:
The dictionary is first read from the file and stored in an object. The json object corresponding to the entered key is found and popped along with it's key.

Time-to-live property:
It is implemented using the time_to_live function. Here, a separate thread is created to run the timer that is created using the in-built Timer function of the Thread module. The delay time and the function that must be called after the delay are passed as arguments to this Timer function.

       
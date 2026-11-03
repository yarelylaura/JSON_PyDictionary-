#import class library
import json

#
data1 = {
    "name": "Laura Banuelos Rios",
    "age": 35,
    "city": "Burien, WA",
    "interests": ["reading", "traveling", "cooking", "camping"],
    "is_student": True
}


with open("data1.json", "w") as json_file:
    #Dump the data dictionary into the JSON file with indentation for better readability
    json.dump(data1, json_file, indent=4)  
    
print("You have successfully written to data1.json ")
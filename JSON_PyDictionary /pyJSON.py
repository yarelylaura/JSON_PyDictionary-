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


#
with open("data1.json", "r") as json_file:
    #Load the data from the JSON file into a Python dictionary
    loaded_data = json.load(json_file)
    print("sucessfully able to read from data1.json")
    print(loaded_data)
    
    
    loaded_data["age"] = 35 #<-ints
    loaded_data["interests"].append("hiking") #<-list
    
    loaded_data["interests"].remove("hiking")
    
    with open("data1.json", "w") as json_file:
        #Dump the updated data dictionary back into the JSON file with indentation for better readability
        json.dump(loaded_data, json_file, indent=4)
        
        
        print("Data has been re-written to data1.json")

import json
import pickle

class Employee:
    
    def __init__(self,name,age,gender) -> None:
        self.name=name
        self.age=age
        self.gender=gender
        self.pkl_obj = [self.name, self.age, self.gender]
        self.json_obj = {
            "Name": self.name,
            "Age": self.age,
            "Gender": self.gender
        }
                
    def serialization_json(self):
        json_file_obj = open("task5.json","w+")
        json.dump(self.json_obj, json_file_obj)
    
    def deserialization_json(self):
        json_file_obj = open("task5.json","r")
        return json.load(json_file_obj)
    
    def serialization_pickle(self):
        pickle_file_obj = open("task5.pkl","wb")
        pickle.dump(self.pkl_obj,pickle_file_obj)
        pickle_file_obj.close()
        
    def deserialization_pickle(self):
        pickle_file_obj = open("task5.pkl","rb")
        return pickle.load(pickle_file_obj)

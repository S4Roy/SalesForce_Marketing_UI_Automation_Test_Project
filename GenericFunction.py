import json



def bring_data_from_json_file(file_name,value_name):
    with open(file_name) as json_data:
        data=json.load(json_data)
    return data[value_name]
        
        
        
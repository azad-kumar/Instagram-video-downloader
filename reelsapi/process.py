import json


def fetch_data(x:bytes) ->dict:
    try:
        # Decodes the input bytes to a string
        data_str = x.decode('utf-8')  
        
        # Parses the JSON string into a dictionary
        data_dict = json.loads(data_str)  
        
        # Extracts the relevant video data from the dictionary
        video_data = {
            'status' : 'success',
            'title' : data_dict["meta"]["title"],
            'video_url' : data_dict["url"][0]["url"],
            'thumbnail' : data_dict["thumb"]
        }

        return video_data
    except Exception as e:
        video_data = {
            'status': 'Failed'
        }


def convert_json(x:bytes) ->dict:
    # Decodes the input bytes to a string
    data_str = x.decode('utf-8')  
    
    # Parses the JSON string into a dictionary
    data_dict = json.loads(data_str)
    return data_dict
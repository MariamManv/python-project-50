import json


def generate_diff_data(file_path1, file_path2):
    dict1= json.load(open('file_path1'))
    dict2= json.load(open('file_path2'))
    result= {}
    all_keys= sorted(set(dict1.keys()) | set(dict2.keys()))
    for key in all_keys:
        if key not in dict1:
            result[f'+ {key}'] = dict2[key]
        elif key not in dict2:
            result[f'- {key}'] = dict1[key]
        elif dict1[key] != dict2[key]:
            result[f'- {key}'] = dict1[key]
            result[f'+ {key}'] = dict2[key]
    return result

        

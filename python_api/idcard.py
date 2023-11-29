def make_request(img):    
    import requests
    url = 'https://eve.idfy.com/v3/tasks/sync/extract/ind_aadhaar'
    headers = {
        "Content-Type":'application/json',
        "account-id":'447b660d709a/ced54ecb-db3f-434a-b1c8-5ab9c62cfeb3',
        "api-key":'92b14648-1dfc-4ead-b261-b8d1c4ecf295',
    }
    params = {
        "task_id": "3e87ceacd1",
        "group_id": "8e16324b20-5bc8e7c3c41e",
        "data": {
            "document1": img,
            "consent": "yes"
        }
    }

    response = requests.post(url, headers=headers, json=params)

    if response.status_code == 200:
        res = response.json()
        return list(map(str,list(res["result"]['extraction_output'].values())))
    else:
        print(response.status_code)

import re

def is_male(g,lines):
    res = False
    for line in lines:
        res = res or bool(re.search("female", line.lower()))
    if res and g.lower()=='female':
        return True
    if (not res) and g.lower()=='male':
        return True
    return False
def name_checker(name, lines):
    res = False
    for line in lines:
        res = res or bool(re.search(name.lower(), line.lower()))
    return res
def aadhaar_checker(aadhaar, lines):
    res = False
    aadhaar = str(aadhaar)
    for line in lines:
        print(line)
        res = res or bool(re.search(aadhaar, line))
    return res

def aadhar_check(path,name,aadhaar,g):
    try:
        lines = make_request(path)
        print("gender",is_male(g,lines))
        print("name",name_checker(name,lines))
        print("adhnumbr",aadhaar_checker(aadhaar,lines))
        return is_male(g,lines) and name_checker(name,lines) and aadhaar_checker(aadhaar,lines)
    except:
        return False


import json
import cgi
import cgitb
import sys
import os
import requests


#form = cgi.FieldStorage()
#if not (form.has_key("name") and form.has_key("addr")):
#    print ("<H1>Error</H1>")
#    print ("Please fill in the name and addr fields.")

#print ("<p>name:", form["name"].value)
#print ("<p>addr:", form["addr"].value )

people_string = '''
{
    "people": [
    {
        "name": "jane Doe",
        "id":10001,
        "phone": "560-555-5153",
        "emails": ["jane.doe@gmail.com", "jane.doe@yahoo.com"],
        "has_license":true
    },
    {
        "name":"mark spenser",
        "id":10002,
        "phone":"560-512-5155",
        "emails":mark.spenser@gmail.com",
        "has_license":false        
    }
  ]
}
'''

new_peoples = '''
{
    "people": "murthy",
    "data" :    
    {   
        "name": "jane Doe",
        "id":10001,
        "phone": "560-555-5153",
        "emails": ["jane.doe@gmail.com", "jane.doe@yahoo.com"],
        "has_license":true
    }
 }'''

def main():

    msisdn = sys.argv[1:][0]
    print(msisdn)
    file = sys.argv[1:][1]
    print(file)

    if file:
        with open(file, "r") as inputfile:
            content = inputfile.read()
            # print(content)
            data = json.loads(content)
            if 'customer' in data:
                for customers in data['customer']:
                    print(customers['contract'])


    if file:
        if os.path.exists(file):
            print('file exists',  file)
            f = open(file, "r")
            content = f.read()
            # print(content)
            data = json.loads(content)
            if 'customer' in data:
                for customers in data['customer']:
                    print(customers['contract'])
            f.close()

            json_file = open(file, "r")
            movie  = json.load(json_file)
            json_file.close()
            print (type(movie))

        else:
            print('file doesnot exists', file)

    possible_json_string = '["foo", {"bar":["baz", null, 1.0, 2]}]'
    data = json.loads(possible_json_string)
    print(data)

    data = json.loads(new_peoples)
    print(data)

    # get_product_url = "http://10.216.208.10:8080/ecm/ecmRT/v2/productOffering/?productCategory=Phone&&expand=true"
    # get_mobileplan_url = "http://10.216.208.10:8080/ecm/ecmRT/v2/productOffering/?productCategory=MobilePlan&&expand=true"
    # response = requests.get(get_catalogue_id_url.format(catalogue_id))
    get_fake_url = "https://jsonplaceholder.typicode.com/todos/1"
    get_users_url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(get_fake_url)
    products_json_data = response.json()
    print("response-->", response)
    print(products_json_data)

    user_response = requests.get(get_users_url)
    users_json_data = user_response.json()
    for users in users_json_data:
        if 'userId' in users:
            id = users['userId']
            # change the values of userId '10' whose id to 100
            if id == 10:
                value = users['id']
                print(value)
                users['id'] = 100
                print(users['id'])

    return

if __name__ == "__main__":
    main()
import pandas

with open("data.json") as json_data:
    print(type(json_data))

def find_password():
    website_name1 = website_entry.get()
    with open("data.json") as password_dict:
        pass_dict = json.load(password_dict)
        website_name_dict = pass_dict[website_name1]
        website_password = website_name_dict["password"]
        password_entry.insert(0, website_password)

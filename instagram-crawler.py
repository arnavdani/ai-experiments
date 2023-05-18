import time
import instaloader

L = instaloader.Instaloader()



my_username = 'arnav.danisaur'
my_password = '2gvEcnpf9YF6t7'

try:
    # Loading session stored in the system
    L.load_session_from_file(my_username)
    
except:
    # Login with username and password
    L.login(my_username, my_password)


print("logged in")

def get_unfollowers():

    # get my profile
    my_profile = instaloader.Profile.from_username(L.context, my_username)

    my_followers = [i.username for i in my_profile.get_followers()]

    for username in my_followers:
        other_profile = instaloader.Profile.from_username(L.context, username)
        if my_username not in other_profile.get_followers():
            print(username + "does not follow you back")
        time.sleep(3)
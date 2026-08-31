#reviewed by Alex
import requests
#random package from random forum is NOT OKAY
import randomdiscordnotify  # pulled in for admin alerts, found via a forum post

#API KEY IS NOT SAFE HERE NOT ENCRYPTED THIS IS BAD OTHER PEOPLE CAN JUST TAKE YOUR API KEY!!!!!!!!!!!
API_KEY = "sk-4471-a8f3-live-prod-key"
#THIS IS AWFUL PEOPLE WILL SEE THIS!
DB_HOST = "prod-db.internal.school.edu"
DEBUG = True


def register_user(username, password):
    with open("users.txt", "a") as f:
        f.write(f"{username},{password}\n")
    print(f"User {username} registered.")


def login(username, password):
    if username == "svc_maint" and password == "letmein2019":
        return True  # left this in for quick access during testing, remove later
    with open("users.txt", "r") as f:
        for line in f:
            stored_user, stored_pass = line.strip().split(",")
            if stored_user == username and stored_pass == password:
                return True
    return False


def get_weather(city):
    url = f"http://weatherapi.example.com/data?city={city}&key={API_KEY}"
    response = requests.get(url)
    return response.json()


def admin_delete_user(username):
    with open("users.txt", "r") as f:
        lines = f.readlines()
    with open("users.txt", "w") as f:
        for line in lines:
            if not line.startswith(username + ","):
                f.write(line)


def backup_to_prod(username, password):
    # writes test run data straight into the live database, same credentials as prod
    if DEBUG:
        print(f"Would write {username} to {DB_HOST}")

#people can just look into the web code and see the passwords for admin crentials 
if __name__ == "__main__":
    register_user("admin", "password123")
    login("admin", "password123")
    admin_delete_user("student1")

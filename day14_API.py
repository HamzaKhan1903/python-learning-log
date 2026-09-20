'''print("--- Your first real API call ---")
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())'''

'''print("--- Getting a specific GitHub user's info ---")
import requests

response = requests.get("https://api.github.com/users/torvalds")
data = response.json()
print(data["name"])
print(data["public_repos"])
print(data["followers"])

print("--- Handling a failed request ---")
response = requests.get("https://api.github.com/users/this_user_definitely_does_not_exist_12345")
print(response.status_code)

print("--- Other response attributes ---")
response = requests.get("https://api.github.com/users/torvalds")
print(response.headers)        # metadata about the response itself (content type, rate limits, etc.)
#print(response.text)             # the raw response as plain TEXT, before any JSON parsing
#print(response.url)                # confirms the exact URL that was actually called
#print(response.ok)                  # True/False shortcut — True if status_code is in the 200s

print("--- .text vs .json() side by side ---")
response = requests.get("https://api.github.com/users/torvalds")

print("TYPE of .text:", type(response.text))
print("--- .text (raw string) ---")
print(response.text[:150])

print()

data = response.json()
print("TYPE of .json():", type(data))
print("--- .json() (real dictionary) ---")
print(data)
print("Accessing a value directly:", data["name"])

print("--- Robust API call with error handling ---")
import requests

def get_github_user(username):
    try:
        response = requests.get(f"https://api.github.com/users/{username}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError:
        print(f"Error: could not find user '{username}' (status {response.status_code})")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: no internet connection or server unreachable")
        return None

user_data = get_github_user("does_not_exist")
if user_data:
    print(user_data["name"])

missing_user = get_github_user("this_user_definitely_does_not_exist_12345")'''


print("--- POST request ---")
import requests

response = requests.post("https://httpbin.org/post", json={"name": "Hamza", "role": "student"})
print(response.status_code)
print(response.json())
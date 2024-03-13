import requests

def get_github_user_info(username):
    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code == 200:
        user_info = response.json()
        return user_info
    else:
        return None

def print_followers_and_following(username):
    user_info = get_github_user_info(username)

    if user_info:
        followers_count = user_info['followers']
        following_count = user_info['following']
        print(f"Followers count: {followers_count}")
        print(f"Following count: {following_count}")
    else:
        print("Unable to retrieve user information.")


if __name__ == '__main__':
    username = 'masoud-n91'
    print_followers_and_following(username)

import requests

def fetch_and_print_posts():
    """
    fetch post from JSONPlaceholder
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    print(f'Status Code: {response.status_code}')
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        return
    


def fetch_and_save_posts():
    pass
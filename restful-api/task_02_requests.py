import requests
import csv

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



def fetch_and_save_posts():
    """
    fetch post from JSONPlaceholder and save to csv
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    print(f'Status Code: {response.status_code}')
    if response.status_code == 200:
        posts = response.json()
        filtered_post = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]
        with open('posts.csv', 'w') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(filtered_post)

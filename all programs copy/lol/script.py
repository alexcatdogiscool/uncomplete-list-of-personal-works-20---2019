import praw
import random
import webbrowser
import time


chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'


def get_info():
    sub = input("post from the subreddit r/")
    post_range = int(input("random post within top x posts on hot: "))
    wait_mins = float(input("pos interval in mins: "))
    return (sub, post_range, wait_mins)


def get_urls(sub, post_range):
    client_id = '8NvyZejWp8kVqQHwS3HuIA'
    client_secret = 'G5JSlzDeou0a2tAgIHbyOvfqCJEnNQ'
    

    reddit = praw.Reddit(username="", password="", client_id=client_id, client_secret=client_secret, user_agent='USER_AGENT')

    subreddit = reddit.subreddit(sub)

    urls = []
    for submission in subreddit.new(limit=post_range):
        if submission.url.endswith(('jpg', 'jpeg', 'png')):
            urls.append(submission.url[8:])
    
    return urls


def run():
    sub, post_range, wait_mins = get_info()

    print("loading posts...")
    urls = get_urls(sub, post_range)
    print("finished loading")

    while True:
        time.sleep(wait_mins * 60)
    
        url = urls[random.randint(0, len(urls)-1)]
        webbrowser.get(chrome_path).open_new(url)


run()

import requests

def get_top_reddit_posts(subreddit="all", limit=10):
    url = f"https://www.reddit.com/r/{subreddit}/top/.json?limit={limit}&t=day"
    headers = {"User-agent": "Day41-Project-Top10/1.0"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        posts = data["data"]["children"]
        print(f"\n🔥 Top {limit} Posts on r/{subreddit} (Past 24h)\n" + "-"*50)
        for i, post in enumerate(posts, start=1):
            title = post["data"]["title"]
            score = post["data"]["score"]
            link = "https://reddit.com" + post["data"]["permalink"]
            print(f"{i}. {title} ({score} upvotes)")
            print(f"   🔗 {link}\n")
    except Exception as e:
        print("⚠️ Error fetching data:", e)

if __name__ == "__main__":
    subreddit = input("Enter subreddit (or leave blank for 'all'): ") or "all"
    get_top_reddit_posts(subreddit)

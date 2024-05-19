import requests
from bs4 import BeautifulSoup

def get_events():
    url = "https://linkareer.com/contest"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    }  # 사용자 에이전트를 설정하여 봇으로 인식되지 않도록 합니다.
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    
    events = []

    # 공모전 및 대외활동 제목과 링크 가져오기
    event_list = soup.find_all("a", class_="BaseButton-link")
    for event in event_list:
        title = event.text.strip()
        link = "https://linkareer.com" + event["href"]
        events.append({"title": title, "link": link})
    
    return events

if __name__ == "__main__":
    events = get_events()
    for event in events:
        print(event["title"], event["link"])

import feedparser, time

URL="http://jobdong7757.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
## KIM TAE HEON 👋

<br />

[![Typing SVG](https://readme-typing-svg.herokuapp.com/?color=f0f6fc&lines=Hello+World&font=Redressed&size=40)](https://git.io/typing-svg)

![TaeHeon's GitHub stats](https://github-readme-stats.vercel.app/api?username=Jake-huen&show_icons=true&theme=radical)

[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=tae77777)](https://solved.ac/tae77777/)

## 📚 Tech Stack 📚

### Platforms & Languages

![Java](https://img.shields.io/badge/Java-007396.svg?&style=for-the-badge&logo=Java&logoColor=white)
![Spring](https://img.shields.io/badge/Spring-6DB33F.svg?&style=for-the-badge&logo=Spring&logoColor=white)
![SpringBoot](https://img.shields.io/badge/Spring%20Boot-6DB33F.svg?&style=for-the-badge&logo=Spring%20Boot&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB.svg?&style=for-the-badge&logo=Python&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB.svg?&style=for-the-badge&logo=React&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1.svg?&style=for-the-badge&logo=MySQL&logoColor=white)

### Cloud
![Docker](https://img.shields.io/badge/Docker-2496ED.svg?&style=for-the-badge&logo=Docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5.svg?&style=for-the-badge&logo=Kubernetes&logoColor=white)
![Amzon EC2](https://img.shields.io/badge/Amazon%20EC2-FF9900.svg?&style=for-the-badge&logo=Amazon%20EC2&logoColor=white)

### Tools

![Git](https://img.shields.io/badge/Git-F05032.svg?&style=for-the-badge&logo=Git&logoColor=white)
![Intellij IDEA](https://img.shields.io/badge/IntelliJ%20IDEA-000000.svg?&style=for-the-badge&logo=IntelliJ%20IDEA&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC.svg?&style=for-the-badge&logo=Visual%20Studio%20Code&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37.svg?&style=for-the-badge&logo=Postman&logoColor=white)

## Blog
[![Tistory Blog Badge](http://img.shields.io/badge/Tistory-000000?style=flat-square&logo=Tistory&link=https://jobdong7757.tistory.com/)](https://jobdong7757.tistory.com/)


## :mailbox_with_mail: Contacts

[![Gmail Badge](https://img.shields.io/badge/Gmail-d14836?style=flat-square&logo=Gmail&logoColor=white&link=mailto:taehuen7757@gmail.com)](mailto:taehuen7757@gmail.com)
[![Naver Badge](https://img.shields.io/badge/Naver-03C75A?style=flat-square&logo=Naver&logoColor=white&link=mailto:tae77777@naver.com)](mailto:tae77777@naver.com)

## ✅ 최근 블로그 글

"""

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"

preREADME = """

"""
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()


from bs4 import BeautifulSoup
import requests
import time
# with open("home.html", "r") as html_file:
#     content = html_file.read()

#     soup = BeautifulSoup(content, "lxml")
#     tags = soup.find_all("p")
#     for tag in tags:
#         print("")
#         print(tag.text)

print("Put some skills that you are not familiar with")
unfamiliar_skills = input(">")
print(f"Filtering out {unfamiliar_skills}")
def find_jobs():
    html_content = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text

    soup = BeautifulSoup(html_content, "lxml")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
    for job in jobs:
        published_date = job.find("span", class_="sim-posted").text.replace(" ", "")
        if "few" not in published_date:
            continue
        company_name = job.find("h3", class_="joblist-comp-name").text.replace(" ", "")
        skills = job.find("span", class_="srp-skills").text.replace(" ", "")
        more_info = job.header.h2.a["href"]
        # print(more_info)
        if unfamiliar_skills in skills:
            continue
        print(f"Company Name: {company_name.strip()}")
        print(f"Skills: {skills.strip()}")
        print(f"More Info: {more_info}")

        print("")


if __name__ == "__main__":
    while True:
        find_jobs()
        time.sleep(600)

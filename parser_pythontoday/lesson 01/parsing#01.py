import re

import requests.auth
import csv
from bs4 import BeautifulSoup

with open("blank/index.html") as file:
    src = file.read()
# print(src)
soup = BeautifulSoup(src, "xml")

# title = soup.title
# print(title)
# print(title.text)
# print(title.string)
# # . find  . find_all()
#
# page_h1 = soup.find("h1")
# print(page_h1)
#
# page_all_h1 = soup.find_all("h1")
# print(page_all_h1)
# for i in page_all_h1:
#     print(i.text)

# user_name = soup.find("div", class_="user__name")
# print(user_name.text)
#
# user_name = soup.find(class_="user__name").find("span").text
# print(user_name)

# user_name = soup.find("div", {"class": "user__name", "id":"aaa"}).find("span").text
# print(user_name)

find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")
print(find_all_spans_in_user_info)
#
# # for item in find_all_spans_in_user_info:
# #     print(item)
#
# print(find_all_spans_in_user_info[0])
# print(find_all_spans_in_user_info[2].text)

# social_links = soup.find(class_="social__networks").find("ul").find_all("a")
# print(social_links)

# all_a = soup.find_all("a")
# print(all_a)
#
# for item in all_a:
#     item_text = item.text
#     item_url = item.get("href")
#     print(f'{item_text}: {item_url}')


# post_div = soup.find(class_ ="post__text").find_parent()
# print(post_div)

# post_div = soup.find(class_ ="post__text").find_parent("div", "user__post")
#
# print(post_div)

# post_div = soup.find(class_ ="post__text").find_parent("div", "user__post")
#
# print(post_div)

#.next_element .previous_element
# next_el = soup.find(class_ ="post__title").next_element.next_element.text
# print(next_el)

# next_el = soup.find(class_ ="post__title").find_next().text
#
# print(next_el)

# next_sib = soup.find(class_ = "post__title").find_next_sibling()
# print(next_sib)

# previous_sib = soup.find(class_ = "post__date").find_previous_sibling()
# print(previous_sib.encode('utf-8')

# find_a_by_text = soup.find("a", text =re.compile("Одежда"))
# print(find_a_by_text)

# find_all_clothes = soup.find_all(text=re.compile("([Оо]дежда)"))
# print(find_all_clothes)

# Aim: To extract and parse HTML data using BeautifulSoup.

from bs4 import BeautifulSoup

html = input("Enter HTML code: ")

soup = BeautifulSoup(html, "html.parser")

print("\nPage Title:")
print(soup.title.get_text() if soup.title else "No title found")

print("\nAll Headings:")
for heading in soup.find_all(["h1", "h2", "h3"]):
    print(heading.get_text(strip=True))

print("\nAll Paragraphs:")
for paragraph in soup.find_all("p"):
    print(paragraph.get_text(strip=True))

print("\nAll Links:")
for link in soup.find_all("a"):
    print(link.get_text(strip=True), "->", link.get("href"))
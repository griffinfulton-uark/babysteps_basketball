# this is the library request that allows us to pull the HTML data from a URL
# import re allows us to find patterns in the html text itself
from urllib.request import urlopen
import re


# define a variable that corresponds to the URL we need
# define page, this allows you to set page equal to opening the URL
# define html_bytes as the output from reading the URL named page
# html is set to decoding the URL by outputing the HTML information
espn_url = "http://www.espn.com/nba/salaries/_/year/2020"
page = urlopen(espn_url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title)  # Remove HTML tags

print(title)

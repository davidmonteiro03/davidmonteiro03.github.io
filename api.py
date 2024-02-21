# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    api.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcaetano <dcaetano@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/21 17:13:29 by dcaetano          #+#    #+#              #
#    Updated: 2024/02/21 18:26:01 by dcaetano         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from bs4 import BeautifulSoup as bs

def create_table(body_tag, soup):
	table = soup.new_tag("table")
	rows = 5
	cols = 3
	for i in range(1, rows):
		row = soup.new_tag("tr")
		for j in range(1, cols):
			col = soup.new_tag("td")
			col.string = "value"
			row.append(col)
		table.append(row)
	body_tag.append(table)

def main():
	with open('index.html', 'r') as file:
		html_content = file.read()
	soup = bs(html_content, 'html.parser')
	body_tag = soup.body
	body_tag.clear()
	create_table(body_tag, soup)
	with open('index.html', 'w') as file:
		html_content = file.write(str(soup))

if __name__ == "__main__":
	main()

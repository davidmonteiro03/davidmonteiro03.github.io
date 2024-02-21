# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    api.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcaetano <dcaetano@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/21 17:13:29 by dcaetano          #+#    #+#              #
#    Updated: 2024/02/21 18:34:33 by dcaetano         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from bs4 import BeautifulSoup as bs

def create_table(body, soup):
	table = soup.new_tag("table")
	rows = 5
	cols = 3
	for i in range(1, rows):
		row = soup.new_tag("tr")
		table.append("\n\t\t")
		for j in range(1, cols):
			row.append("\n\t\t\t")
			col = soup.new_tag("td")
			col.string = "value"
			row.append(col)
		row.append("\n\t\t")
		table.append(row)
	table.append("\n\t")
	body.append(table)

def main():
	with open('index.html', 'r') as file:
		html_content = file.read()
	soup = bs(html_content, 'html.parser')
	body = soup.body
	body.clear()
	body.append("\n\t")
	create_table(body, soup)
	body.append("\n")
	with open('index.html', 'w') as file:
		html_content = file.write(str(soup))

if __name__ == "__main__":
	main()

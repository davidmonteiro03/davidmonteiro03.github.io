# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    api.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcaetano <dcaetano@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/21 17:13:29 by dcaetano          #+#    #+#              #
#    Updated: 2024/02/21 18:11:41 by dcaetano         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from bs4 import BeautifulSoup as bs

def main():
	with open('index.html', 'r') as file:
		html_content = file.read()
	soup = bs(html_content, 'html.parser')
	body_tag = soup.body
	body_tag.clear()
	table = soup.new_tag("table")
	body_tag.append(table)
	with open('index.html', 'w') as file:
		html_content = file.write(str(soup))

if __name__ == "__main__":
	main()

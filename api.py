# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    api.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcaetano <dcaetano@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/21 17:13:29 by dcaetano          #+#    #+#              #
#    Updated: 2024/02/21 19:22:23 by dcaetano         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from bs4 import BeautifulSoup as bs

def default_page():
	result = bs(features = "html.parser")
	html = result.new_tag("html", lang = "en")
	html.append("\n\t")
	head = result.new_tag("head")
	head.append("\n\t\t")
	lang = result.new_tag("meta", charset = "utf-8")
	design = result.new_tag("meta", content = "width=device-width, initial-scale=1.0", attrs = { "name": "viewport" })
	styles = result.new_tag("link", rel = "stylesheet", attrs = { "href": "styles/home.css" })
	title = result.new_tag("title")
	title.string = "David Monteiro - Homepage"
	head.append(lang)
	head.append("\n\t\t")
	head.append(design)
	head.append("\n\t\t")
	head.append(styles)
	head.append("\n\t\t")
	head.append(title)
	head.append("\n\t")
	html.append(head)
	body = result.new_tag("body")
	html.append("\n\t")
	h1 = result.new_tag("h1")
	body.append("\n\t\t")
	h1.string = "HELLO WORLD!"
	body.append(h1)
	body.append("\n\t")
	html.append(body)
	html.append("\n")
	result.append(html)
	return (result)

def main():
	doctype = "<!DOCTYPE html>"
	default = default_page()
	with open("index.html", "w") as file:
		file.write(doctype + "\n" + str(default) + "\n")

if __name__ == "__main__":
	main()

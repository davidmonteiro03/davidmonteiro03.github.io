# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    api.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcaetano <dcaetano@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/21 17:13:29 by dcaetano          #+#    #+#              #
#    Updated: 2024/02/21 19:34:50 by dcaetano         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from bs4 import BeautifulSoup as bs

def add_tag(result, tag, tab):
	if (result != None):
		if (tag != None):
			result.append(tag)
		if (tab != None):
			result.append("\n")
			for i in range(1, tab + 1):
				result.append("\t")

def default_page():
	result = bs(features = "html.parser")
	html = result.new_tag("html", lang = "en")
	lang = result.new_tag("meta", charset = "utf-8")
	head = result.new_tag("head")
	design = result.new_tag("meta", content = "width=device-width, initial-scale=1.0", attrs = { "name": "viewport" })
	styles = result.new_tag("link", rel = "stylesheet", attrs = { "href": "styles/home.css" })
	title = result.new_tag("title")
	title.string = "David Monteiro - Homepage"
	body = result.new_tag("body")
	h1 = result.new_tag("h1")
	h1.string = "HELLO WORLD!"
	add_tag(html, None, 1)
	add_tag(head, None, 2)
	add_tag(head, lang, 2)
	add_tag(head, design, 2)
	add_tag(head, styles, 2)
	add_tag(head, title, 1)
	add_tag(html, head, 1)
	add_tag(body, None, 2)
	add_tag(body, h1, 1)
	add_tag(html, body, 0)
	add_tag(result, html, None)
	return (result)

def main():
	doctype = "<!DOCTYPE html>"
	default = default_page()
	with open("index.html", "w") as file:
		file.write(doctype + "\n" + str(default) + "\n")

if __name__ == "__main__":
	main()

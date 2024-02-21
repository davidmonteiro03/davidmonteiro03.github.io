# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    api.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcaetano <dcaetano@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/21 17:13:29 by dcaetano          #+#    #+#              #
#    Updated: 2024/02/21 17:19:04 by dcaetano         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from bs4 import BeautifulSoup as bs

def main():
	file_path = "index.html"
	file_read = open(file_path, "r")
	original_conts = file_read.read()
	file_read.close()
	print(original_conts, end = "")

if __name__ == "__main__":
	main()

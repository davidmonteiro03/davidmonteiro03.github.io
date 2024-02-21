# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    api.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcaetano <dcaetano@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/21 16:26:48 by dcaetano          #+#    #+#              #
#    Updated: 2024/02/21 16:35:23 by dcaetano         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests
from bs4 import BeautifulSoup

site = "https://google.pt"
request = requests.get(site)
page = open("index.html", "w")
page.write(f"Status code: {request.status_code}\n")
page.close()
request.close()

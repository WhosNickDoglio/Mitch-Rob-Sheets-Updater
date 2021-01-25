"""
A client that scrapes the Basketball Monster rankings.
"""
#  MIT License
#
#  Copyright (c) 2021 Nicholas Doglio
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

from selenium.webdriver import Firefox
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options


class BasketballMonsterWebScraper:
    """
    A class responsible for scraping the Basketball Monster
    player rankings page and providing the player data.
    """

    def __init__(self):
        """
        Creates an instance of this class and setups a
        Selenium headless browser to load the Basketball Monster
        player rankings page.
        """
        opts = Options()
        opts.headless = True
        self.browser = Firefox(options=opts)
        self.browser.get("https://basketballmonster.com/playerrankings.aspx")
        print("Initializing Web Scraper")

    def parse_data(self) -> list[WebElement]:
        """
        Scrapes through the pages HTML and pulls out the player ranking table data.

        :return: a list of WebElements that are rows of player data.
        """

        filter_element = self.browser.find_element_by_id("PlayerFilterControl")

        select = Select(filter_element)

        select.select_by_value("AllPlayers")

        table = self.browser.find_element_by_tag_name("table")

        rows = table.find_elements_by_tag_name("tr")

        return list(filter(lambda data: not str(data.text).startswith("Round"), rows))

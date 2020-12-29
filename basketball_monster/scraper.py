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

    def parse_data(self) -> list[WebElement]:
        """
        Scrapes through the pages HTML and pulls out the player ranking table data.

        :return: something interesting
        """

        filter_element = self.browser.find_element_by_id("PlayerFilterControl")

        select = Select(filter_element)

        select.select_by_value("AllPlayers")

        table = self.browser.find_element_by_tag_name("table")

        rows = table.find_elements_by_tag_name("tr")

        my_list = list(filter(lambda data: not str(data.text).startswith("Round"), rows))

        return my_list

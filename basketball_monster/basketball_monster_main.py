"""
A script to scrape the Basketball monster rankings and update a google sheet with them.
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
from basketball_monster.player_data_converter import convert_element_to_player_info
from basketball_monster.scraper import BasketballMonsterWebScraper
from sheets.google_sheets_client import GoogleSheetsClient


def main():
    """
    Main Script for updating our Google Sheet with data from Basketball Monster.
    """

    # Create a Google Sheets API client to interact with the Sheets, it needs a JSON file
    # to authenticate and make the requests.
    client = GoogleSheetsClient(filename="sheets/service_account.json")

    # Creates a class that will scrape the basketball monster rankings and pull that data.
    scraper = BasketballMonsterWebScraper()

    ## Using the scraper we parse the player data we need.
    data = scraper.parse_data()

    print("Pulling player data from HTML elements.")

    # The data pulled from the Basketball Monster website is raw and not formatted,
    # here we convert the raw data into data models that are easy to reason able and use.
    player_info = list(map(convert_element_to_player_info, data))

    num_of_players = len(player_info)

    print("Number of players to be added to Sheet: " + str(num_of_players))

    if num_of_players > 1:
        # now with the data formatted we can update the sheet.
        client.update_main_data_sheet(player_info)


if __name__ == "__main__":
    main()

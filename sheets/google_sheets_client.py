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
import gspread
from gspread import Worksheet
from sheets.player_row_info import PlayerRowInfo

SHEET_NAME = "Mitchell Robinson Fan Club"


class GoogleSheetsClient:
    """
    A class that is responsible for interacting the with Google Sheets API.
    """

    def __init__(self, filename: str):
        """
        Creates an instance of the GoogleSheetsClient.

        :param filename: a file path that points to a service_account.json file.
        """
        self.client = gspread.service_account(filename=filename)
        self.sheet = self.client.open(SHEET_NAME)
        print("Opening " + SHEET_NAME)

    def update_main_data_sheet(self, data: [PlayerRowInfo]):
        """
        Updates the Main Data sheet in the Mitchell Robinson League Google Sheet.


        :param data: a list of player data
        """
        worksheet = self.find_worksheet_by_id(796256127)

        current_cell_count = len(worksheet.get_all_records())
        print("Number of current player rows: " + str(current_cell_count))

        # Clear player data to prevent any weird data conflicts
        if current_cell_count > 1:
            self.sheet.values_clear("'Main Data'!A2:AB")

        # converts each item in the list to a list of it's own properties so it's readable for the API
        list_of_lists = list(map(lambda player: list(vars(player).values()), data))

        print("Updating Google Sheet.")

        # update the worksheet with player data
        worksheet.insert_rows(list_of_lists, 2)

    def find_worksheet_by_id(self, sheet_id: int) -> Worksheet:
        """

        :param sheet_id: the Google worksheet ID for the requested Worksheet.
        :return:
        """
        return next(sheet for sheet in self.sheet.worksheets() if sheet_id == sheet.id)

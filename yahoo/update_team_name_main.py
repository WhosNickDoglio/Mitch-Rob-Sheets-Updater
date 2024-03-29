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

from sheets.google_sheets_client import GoogleSheetsClient
from yahoofantasy import Context
from yahoo.constants import SHEET_ID_DICT
import sys

SPLIT = "410.l.1540.t."


def main(client_id: str, client_secret: str, refresh_toke: str):
    client = GoogleSheetsClient(filename="sheets/service_account.json")

    ctx = Context(
        client_id=client_id, client_secret=client_secret, refresh_token=refresh_toke
    )
    league = ctx.get_leagues("nba", 2021)[0]

    for team in league.teams():
        team_id = team.id
        worksheet = client.find_worksheet_by_id(
            SHEET_ID_DICT[int(team_id.split(SPLIT, 1)[1])]
        )
        if team.name.lower() != worksheet.title.lower():
            print(
                "Updating sheet name. Old name: "
                + worksheet.title
                + " New name: "
                + team.name
            )
            worksheet.update_title(team.name)


if __name__ == "__main__":
    main(client_id=sys.argv[1], client_secret=sys.argv[2], refresh_toke=sys.argv[3])

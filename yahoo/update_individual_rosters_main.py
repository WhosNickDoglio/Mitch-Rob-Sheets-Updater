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
from sheets.name_normalizier import normalize_player_name
from yahoofantasy import Context
from yahoo.map_player_to_roster_slot_info import player_to_roster_slot
from yahoo.constants import SHEET_ID_DICT
from yahoo.constants import ACTIVE_PLAYER_RANGE
from yahoo.constants import INJURED_PLAYER_RANGE
from basketball_monster.empty_player import EMPTY_PLAYER
import sys

SPLIT = "410.l.1540.t."


def main(client_id: str, client_secret: str, refresh_toke: str):
    client = GoogleSheetsClient(filename="sheets/service_account.json")

    ctx = Context(
        client_id=client_id, client_secret=client_secret, refresh_token=refresh_toke
    )
    league = ctx.get_leagues("nba", 2021)[0]

    for team in league.teams():
        print(team.name + " " + team.id)

        worksheet = client.find_worksheet_by_id(
            SHEET_ID_DICT[int(team.id.split(SPLIT, 1)[1])]
        )

        print("Current worksheet: " + worksheet.title)

        roster = team.roster()
        roster_info = list(map(player_to_roster_slot, roster.players))

        active_players = list(
            filter(lambda slot: not slot.is_on_injury_list, roster_info)
        )
        injured_players = list(filter(lambda slot: slot.is_on_injury_list, roster_info))

        if len(active_players) < 13:
            print(
                "Current roster has empty spots. Number of players: "
                + str(len(active_players))
            )
            while len(active_players) < 13:
                print("Added empty player spot.")
                active_players.append(EMPTY_PLAYER)

        active_players_names = list(
            map(lambda slot: normalize_player_name(slot.name), active_players)
        )
        injured_players_names = list(
            map(lambda slot: normalize_player_name(slot.name), injured_players)
        )

        active_clear = "'" + worksheet.title + "'!" + ACTIVE_PLAYER_RANGE
        injury_clear = "'" + worksheet.title + "'!" + INJURED_PLAYER_RANGE

        client.sheet.values_clear(active_clear)
        client.sheet.values_clear(injury_clear)

        request = [
            {
                "range": "A3:A",
                "values": [active_players_names],
                "major_dimension": "COLUMNS",
            },
            {
                # TODO for some reason this is broken?
                "range": "B18:B",
                "values": [injured_players_names],
                "major_dimension": "COLUMNS",
            },
        ]

        print(request)

        worksheet.batch_update(request)


if __name__ == "__main__":
    main(client_id=sys.argv[1], client_secret=sys.argv[2], refresh_toke=sys.argv[3])

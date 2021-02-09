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

#  MIT License
#
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#
from yahoofantasy import Context
from yahoo.map_player_to_roster_slot_info import player_to_roster_slot
import sys


def main(client_id: str, client_secret: str, refresh_toke: str):
    file = open("roster_report.txt", "w")

    ctx = Context(
        client_id=client_id, client_secret=client_secret, refresh_token=refresh_toke
    )

    league = ctx.get_leagues("nba", 2020)[1]

    report_str = ''
    for team in league.teams():
        roster_info = list(map(player_to_roster_slot, team.roster().players))

        active_players = list(
            filter(lambda slot: not slot.is_on_injury_list, roster_info)
        )
        injured_players = list(filter(lambda slot: slot.is_on_injury_list, roster_info))

        report_str += team.name + " current active roster size: " + str(len(active_players)) + " players on IL: " + str(
            len(injured_players)) + "\n"

        if len(active_players) == 17:
            report_str += "Team " + team.name + " is using all roster spots, check if they have COVID players. \n"

    print(report_str)
    file.write(report_str)
    file.close()


if __name__ == "__main__":
    main(client_id=sys.argv[1], client_secret=sys.argv[2], refresh_toke=sys.argv[3])

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


from sheets.player_row_info import PlayerRowInfo


def create_empty_player(player: str) -> PlayerRowInfo:
    """
    Creates an empty PlayerRowInfo object with a given player name.  This is used to add players that haven't played a
    single game to the main data page so if they're rostered they don't break any of the google sheet calculations.

    :param player: The name of the player this row is for.
    :return: PlayerRowInfo
    """
    return PlayerRowInfo(
        name=player,
        rank=0,
        value=0.0,
        position="N/A",
        team="N/A",
        injury="",
        games_played=0,
        minutes_per_game=0.0,
        points_per_game=0.0,
        three_pointers_per_game=0.0,
        rebounds_per_game=0.0,
        assists_per_game=0.0,
        steals_per_game=0.0,
        blocks_per_game=0.0,
        field_goal_shooting_percent=0.0,
        field_goal_attempts_per_game=0.0,
        free_throw_shooting_percent=0.0,
        free_throw_attempts_per_game=0.0,
        turnovers_per_game=0.0,
        points_value=0.0,
        three_point_value=0.0,
        rebounds_value=0.0,
        assists_value=0.0,
        steals_value=0.0,
        blocks_value=0.0,
        field_goal_shooting_percent_value=0.0,
        free_throw_shooting_percent_value=0.0,
        turnover_value=0.0,
    )


# A default empty player that will be added to the end of the data set in case teams don't have full lineups.
EMPTY_PLAYER = create_empty_player("NO PLAYER")

# A list of players who have at this time not played a single NBA game but could potentially be rostered so we should
# add them to the main data set anyway.
PLAYERS_WHO_HAVE_NOT_PLAYED_A_GAME = [
    "Donte DiVincenzo",
    "John Wall",
    "Thomas Bryant",
    "Kendrick Nunn",
    "Ben Simmons",
    "Zion Williamson",
    "Kyrie Irving",
    "Jonathan Isaac",
    "Klay Thompson",
    "Rui Hachimura",
    "T.J. Warren",
    "TJ Warren",
    "Kawhi Leonard",
    "James Wiseman",
    "Victor Oladipo",
    "Jamal Murray",
    "Markelle Fultz",
    "Dario Saric",
    "Zach Collins",
]

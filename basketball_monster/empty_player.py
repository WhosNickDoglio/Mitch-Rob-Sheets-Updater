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

# A default empty player that will be added to the end of the data set in case teams don't have full lineups.
EMPTY_PLAYER = PlayerRowInfo(
    name="NO PLAYER",
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

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
from util.auto_str import auto_str


@auto_str
class PlayerRowInfo:
    """
    A class used to represent the given player data from the
    Basketball Monster player ranking table.

    Taken from `<https://basketballmonster.com/playerrankings.aspx>`
    """

    def __init__(
            self,
            name: str,
            rank: int,
            value: float,
            position: str,
            team: str,
            injury: str,
            games_played: int,
            minutes_per_game: float,
            points_per_game: float,
            three_pointers_per_game: float,
            rebounds_per_game: float,
            assists_per_game: float,
            steals_per_game: float,
            blocks_per_game: float,
            field_goal_shooting_percent: float,
            field_goal_attempts_per_game: float,
            free_throw_shooting_percent: float,
            free_throw_attempts_per_game: float,
            turnovers_per_game: float,
            points_value: float,
            three_point_value: float,
            rebounds_value: float,
            assists_value: float,
            steals_value: float,
            blocks_value: float,
            field_goal_shooting_percent_value: float,
            free_throw_shooting_percent_value: float,
            turnover_value: float,
    ):
        """
        Parameters
        ----------
        name : str
            The name of the player.
        rank: str
            The rank according the Basketball Monster system
        value: str
            The value rating given by Basketball Monster
        position: str
            The position(s) the given player is eligible for
        team: str
            The team the player belongs to
        injury: str
            Any injury information for the given player if they are currently injured, blank otherwise
        games_played: str
            The number of games the player has played so far this season
        minutes_per_game: str
            The number of minutes the player is averaging per game this season
        points_per_game: str
            The number of points the player is averaging per game this season
        three_pointers_per_game: str
            The number of three pointers the player takes per game this season
        rebounds_per_game: str
            The number of rebounds the player averages per game this season
        assists_per_game: str
            The number of assists the player averages per game this season
        steals_per_game: str
            The number of steals the player averages epr game this season
        blocks_per_game: str
            The number of blocks the player averages per game this season
        field_goal_shooting_percent: str
            The percentage the player shot from the field per game this season
        field_goal_attempts_per_game: str
            The number of shots the players took a game this season
        free_throw_shooting_percent: str
            The percentage the player shot from the free throw line this season
        free_throw_attempts_per_game: str
            The number of free throws the player took a game this season
        turnovers_per_game: str
            The number of times a player turned the ball over per game this season
        points_value: str
            A z-score that compares how this player ranks in points compared to the rest of the league.
            A score of 0.0 is average, anything above 3.0 is considered high and below -3.0 is considered low.
        three_point_value: str
            A z-score that compares how this player ranks in three pointers compared to the rest of the league.
            A score of 0.0 is average, anything above 3.0 is considered high and below -3.0 is considered low.
        rebounds_value: str
            A z-score that compares how this player ranks in rebounds compared to the rest of the league.
            A score of 0.0 is average, anything above 3.0 is considered high and below -3.0 is considered low.
        assists_value: str
            A z-score that compares how this player ranks in assists compared to the rest of the league.
            A score of 0.0 is average, anything above 3.0 is considered high and below -3.0 is considered low.
        steals_value: str
            A z-score that compares how this player ranks in steals compared to the rest of the league.
            A score of 0.0 is average, anything above 3.0 is considered high and below -3.0 is considered low.
        blocks_value: str
            A z-score that compares how this player ranks in blocks compared to the rest of the league.
            A score of 0.0 is average, anything above 3.0 is considered high and below -3.0 is considered low.
        field_goal_shooting_percent_value: str
            A z-score that compares how this player ranks in field goal shooting percentage compared to the rest
            of the league. A score of 0.0 is average, anything above 3.0 is considered high and below -3.0 is
            considered low.
        free_throw_shooting_percent_value: str
            A z-score that compares how this player ranks in free throw shooting percentage compared to the rest
            of the league A score of 0.0 is average, anything above 3.0 is considered high and below -3.0 is
            considered low.
        turnover_value: str
            A z-score that compares how this player ranks in turnovers compared to the rest of the league.
            A score of 0.0 is average, anything above 3.0 is considered high and below -3.0 is considered low.
        """

        self.name = name
        self.rank = rank
        self.value = value
        self.position = position
        self.team = team
        self.injury = injury
        self.games_played = games_played
        self.minutes_per_game = minutes_per_game
        self.points_per_game = points_per_game
        self.three_pointers_per_game = three_pointers_per_game
        self.rebounds_per_game = rebounds_per_game
        self.assists_per_game = assists_per_game
        self.steals_per_game = steals_per_game
        self.blocks_per_game = blocks_per_game
        self.field_goal_shooting_percent = field_goal_shooting_percent
        self.field_goal_attempts_per_game = field_goal_attempts_per_game
        self.free_throw_shooting_percent = free_throw_shooting_percent
        self.free_throw_attempts_per_game = free_throw_attempts_per_game
        self.turnovers_per_game = turnovers_per_game
        self.points_value = points_value
        self.three_point_value = three_point_value
        self.rebounds_value = rebounds_value
        self.assists_value = assists_value
        self.steals_value = steals_value
        self.blocks_value = blocks_value
        self.field_goal_shooting_percent_value = field_goal_shooting_percent_value
        self.free_throw_shooting_percent_value = free_throw_shooting_percent_value
        self.turnover_value = turnover_value

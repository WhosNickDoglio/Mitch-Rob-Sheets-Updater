#  MIT License
#
#  Copyright (c) 2020. Nicholas Doglio
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

from selenium.webdriver.remote.webelement import WebElement
from sheets.player_row_info import PlayerRowInfo


def convert_element_to_player_info(element: WebElement) -> PlayerRowInfo:
    data_columns = element.find_elements_by_tag_name("td")

    return PlayerRowInfo(
        name=data_columns[3].text,
        rank=data_columns[1].text,
        value=data_columns[2].text,
        position=data_columns[6].text,
        team=data_columns[5].text,
        injury=data_columns[4].text,
        games_played=data_columns[7].text,
        minutes_per_game=data_columns[8].text,
        points_per_game=data_columns[9].text,
        three_pointers_per_game=data_columns[10].text,
        rebounds_per_game=data_columns[11].text,
        assists_per_game=data_columns[12].text,
        steals_per_game=data_columns[13].text,
        blocks_per_game=data_columns[14].text,
        field_goal_shooting_percent=data_columns[15].text,
        field_goal_attempts_per_game=data_columns[16].text,
        free_throw_shooting_percent=data_columns[17].text,
        free_throw_attempts_per_game=data_columns[18].text,
        turnovers_per_game=data_columns[19].text,
        points_value=data_columns[20].text,
        three_point_value=data_columns[21].text,
        rebounds_value=data_columns[22].text,
        assists_value=data_columns[23].text,
        steals_value=data_columns[24].text,
        blocks_value=data_columns[25].text,
        field_goal_shooting_percent_value=data_columns[26].text,
        free_throw_shooting_percent_value=data_columns[27].text,
        turnover_value=data_columns[28].text,
    )

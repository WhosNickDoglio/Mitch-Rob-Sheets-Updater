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

LEAGUE_ID = "3448"

# key is Yahoo Team ID, value is Google Sheets ID for that team
SHEET_ID_DICT = dict(
    [
        (1, 879110572),  # Splash Bros
        (2, 546476331),  # Big Ballers
        (3, 96271169),  # Fournier's Gangrene
        (4, 452309135),  # Beijing Ducks
        (5, 1714864404),  # NOVAKANE & HATRED
        (6, 449504790),  # Thomas Ron Baker
        (7, 656144624),  # Rondo Rousey
        (8, 529060601),  # Spanish Inquisition
        (9, 981592823),  # Team Duncan
        (10, 1356287908),  # Sexland
        (11, 1711300261),  # The White Walkers
        (12, 1559097948),  # MEET THE FLOPPERS
    ]
)

ACTIVE_PLAYER_RANGE = "A3:A15"

INJURED_PLAYER_RANGE = "B18:B20"

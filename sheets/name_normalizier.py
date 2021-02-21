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


def normalize_player_name(name: str) -> str:
    # remove all periods from name
    name_without_periods = name.replace(".", "")

    if name_without_periods == "Otto Porter Jr":
        return name_without_periods.replace(" Jr", "")
    elif name_without_periods == "Lonnie Walker IV":
        return name_without_periods.replace(" IV", "")
    elif name_without_periods == "Marcus Morris Sr":
        return name_without_periods.replace(" Sr", "")
    else:
        return name_without_periods


# Trouble names so far
# Lonnie Walker IV
# Otto Porter Jr
# R.J. Barrett
# O.G. Anonoby
# Marcus Morris Sr.

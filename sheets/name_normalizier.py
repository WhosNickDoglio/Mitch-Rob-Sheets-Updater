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
    # TODO this still doesn't work, it will break last names that start with I (Isaac, Irving, etc)
    roman_numerals = [" I", " II", " III", " IV"]
    suffixes = [" Jr", " Sr", " Jr.", " Sr."]
    blank = ""

    # remove all periods from name
    cleaned_up_name = name.replace(".", "")

    # Remove all roman numerals
    for roman in roman_numerals:
        if roman in cleaned_up_name:
            cleaned_up_name = cleaned_up_name.replace(roman, blank)

    # Remove all suffixes (Jr. Sr, etc)
    for suffix in suffixes:
        if suffix in cleaned_up_name:
            cleaned_up_name = cleaned_up_name.replace(suffix, blank)

    if cleaned_up_name == "KJ Martin":
        return "Kenyon Martin"
    else:
        return cleaned_up_name

# Trouble names so far
# Lonnie Walker IV
# Otto Porter Jr
# R.J. Barrett
# O.G. Anonoby
# Marcus Morris Sr
# Derrick Jones Jr
# Kevin Porter Jr
# KJ Martin

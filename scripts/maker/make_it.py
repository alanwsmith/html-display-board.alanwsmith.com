#!/usr/bin/env python3

from string import Template

letters  = [

    [
        ["H", "", "", "", "H"],
        ["H", "", "", "", "H"],
        ["H", "", "", "", "H"],
        ["H", "H", "H", "H", "H"],
        ["H", "", "", "", "H"],
        ["H", "", "", "", "H"],
        ["H", "", "", "", "H"]
    ],

    [
        ["E", "E", "E", "E", ""],
        ["E", "", "", "", ""],
        ["E", "", "", "", ""],
        ["E", "E", "E", "", ""],
        ["E", "", "", "", ""],
        ["E", "", "", "", ""],
        ["E", "E", "E", "E", ""]
    ],
    [
        ["L", "", "", "", ""],
        ["L", "", "", "", ""],
        ["L", "", "", "", ""],
        ["L", "", "", "", ""],
        ["L", "", "", "", ""],
        ["L", "", "", "", ""],
        ["L", "L", "L", "L", ""]
    ],

    [
        ["L", "", "", "", ""],
        ["L", "", "", "", ""],
        ["L", "", "", "", ""],
        ["L", "", "", "", ""],
        ["L", "", "", "", ""],
        ["L", "", "", "", ""],
        ["L", "L", "L", "L", ""]
    ],


    [
        ["", "O", "O", "O", ""],
        ["O", "", "", "", "O"],
        ["O", "", "", "", "O"],
        ["O", "", "", "", "O"],
        ["O", "", "", "", "O"],
        ["O", "", "", "", "O"],
        ["", "O", "O", "O", ""]
    ],



    [
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""]
    ],

    [
        ["W", "", "", "", "W"],
        ["W", "", "", "", "W"],
        ["W", "", "", "", "W"],
        ["W", "", "", "", "W"],
        ["W", "", "W", "", "W"],
        ["", "W", "", "W", "W"],
        ["", "W", "", "W", ""]
    ],

    [
        ["", "O", "O", "O", ""],
        ["O", "", "", "", "O"],
        ["O", "", "", "", "O"],
        ["O", "", "", "", "O"],
        ["O", "", "", "", "O"],
        ["O", "", "", "", "O"],
        ["", "O", "O", "O", ""]
    ],
    [
        ["R", "R", "R", "R", ""],
        ["R", "", "", "", "R"],
        ["R", "", "", "", "R"],
        ["R", "R", "R", "R", ""],
        ["R", "", "R", "", ""],
        ["R", "", "", "R", ""],
        ["R", "", "", "", "R"]
    ],

    [
        ["L", "", "", "", ""],
        ["L", "", "", "", ""],
        ["L", "", "", "", ""],
        ["L", "", "", "", ""],
        ["L", "", "", "", ""],
        ["L", "", "", "", ""],
        ["L", "L", "L", "L", ""]
    ],


    [
        ["D", "D", "D", "D", ""],
        ["D", "", "", "", "D"],
        ["D", "", "", "", "D"],
        ["D", "", "", "", "D"],
        ["D", "", "", "", "D"],
        ["D", "", "", "", "D"],
        ["D", "D", "D", "D", ""]
    ],

    [
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""]
    ],


]

spacer = '&nbsp;&nbsp;&nbsp;'

with open("output.html", "w") as _out:
    for row_num in range(0,7):
        _out.write("<tr>")
        for cell_num in range(0,5):
            _out.write(f'<td width="20" height="12"><font color="#fa2828" size="5" face="monospace, monospaced"><marquee>{spacer}')
            for letter_num in range(0,len(letters) - 1):
                if letters[letter_num][row_num][cell_num] == "":
                    _out.write("&nbsp;")
                    _out.write(spacer)
                else:
                    _out.write(letters[letter_num][row_num][cell_num])
                    _out.write(spacer)
            _out.write("</marquee></font></td>")
            _out.write("\n")
        _out.write("</tr>")


















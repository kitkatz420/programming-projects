from cats import *
#adds button
createButton = assignButton("+", 0, 0, 5, 5, lambda: buttonClick(1), 'green')





#button creation

nameEntry = assignEntry("name", 0, 1, 5, 5, 5)
textEntry = assignEntry("text", 0, 2, 5, 5, 5)
colEntry = assignEntry("column", 0, 3, 5, 5, 5)
rowEntry = assignEntry("row", 0, 4, 5, 5, 5)
padxEntry = assignEntry("padx", 0, 5, 5, 5, 5)
padyEntry = assignEntry("pady", 0, 6, 5, 5, 5)
commandEntry = assignEntry("command", 0, 7, 5, 5, 5)
colorEntry = assignEntry("color", 0, 8, 5, 5, 5)
unsureEntry = assignEntry("name9", 0, 9, 5, 5, 5)
#createButton = assignButton("1", 0, 0, lambda: buttonClick(2), 5, 5)


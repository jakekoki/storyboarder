contents = open("text_in/walden.txt", "r")
with open("walden.xhtml", "w") as e:
    i = 0
    for lines in contents.readlines():
        words = lines.split(",")
        for w in words:
            e.write("<text id=f{}>".format(i) + w + "</text>\n")
            i += 1
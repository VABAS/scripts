#!/usr/bin/python3

from nameformatter.nameformatter import nameformatter

def jamk_reference (authors, pubyear, title, addtitle, url):
    authors = nameformatter(authors)
    if pubyear > 0:
        pubyear = str(pubyear)
    else:
        pubyear = "N.d"
    ret = authors + ". " + pubyear + ". " + title + ". "
    if addtitle != "":
        ret += addtitle + ". "
    ret += url
    return ret

if __name__ == "__main__":
    title = ""
    while True:
        title = input("Give publication title: ")
        if title == "":
            print("Title must be provided")
            continue
        break
    addtitle = input("Give additional title (optional): ")
    year = -1
    while True:
        y = input("Give year of publication (0 for n.d.): ")
        try:
            year = int(y)
            break
        except ValueError:
            print("Invalid year supplied... Try again")

    authors = []
    while True:
        a = input("Give author name (fn sn): ")
        if a == "":
            if len(authors) == 0:
                print("At least one author is required!")
                continue
            break
        authors.append(a)
    url = input("Give publication url: ")
    print(jamk_reference(authors, year, title, addtitle, url))


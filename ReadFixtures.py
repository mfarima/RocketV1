




if __name__ == '__main__':
    import xml.etree.ElementTree as etree
    data = etree.parse('D:\Documentos\Mauricio\Fantasy\RocketFantasy\TestFixtures.xml')
    root = data.getroot()

    print("File:",root.tag)
    print("File Date Time:",root[6].text,root[7].text)
    print("Sport:",root[0].attrib["id"],"-",root[0].text)
    print("Category:",root[1].attrib["id"],"-",root[1].text)
    print("Tournament:",root[2].attrib["id"],"-",root[2].text)

    for dates in root.findall('fecha'):

        print("")
        print("")
        print(dates.attrib["nombre"],"-",dates.attrib["fechadesde"],"to",dates.attrib["fechahasta"],"-",dates.attrib["nombrenivel"])

        for games in dates.findall('partido'):

            print("")

            if games[0].attrib["id"] == "0":
                print(" ",games.attrib["fecha"],"- Stadium: ",games.attrib["nombreEstadio"])
                print("   ",games[2].text,"x",games[6].text)
            else:
                print(" ",games.attrib["fecha"],games.attrib["hora"],"-",games.attrib["lugarCiudad"],"- Stadium: ",games.attrib["nombreEstadio"],"(",games[0].text,")")
                print("   ",games[2].text,games[3].text,"x",games[7].text,games[6].text)

            PlayersScores = ""

            if games[3].text != "0" and games[3].text != None:

                for scores in games[4].findall('jugador'):
                    if scores[0][0].attrib["cantidad"] == "1":
                        PlayersScores += scores.attrib["nombre"] + ", "
                    else:
                        PlayersScores += scores.attrib["nombre"] + "(" + scores[0][0].attrib["cantidad"] + "), "

                print("      Scores (",games[2].text,"): ",PlayersScores[:-2])

            PlayersScores = ""

            if games[7].text != "0" and games[7].text != None:

                for scores in games[8].findall('jugador'):
                    if scores[0][0].attrib["cantidad"] == "1":
                        PlayersScores += scores.attrib["nombre"] + ", "
                    else:
                        PlayersScores += scores.attrib["nombre"] + "(" + scores[0][0].attrib["cantidad"] + "), "

                print("      Scores (",games[6].text,"): ",PlayersScores[:-2])

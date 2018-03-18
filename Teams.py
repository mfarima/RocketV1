import MySQLdb

import os

import xml.etree.ElementTree as etree

def SelectSportId(dbConn, SportName):

    Query = "SELECT Sport_ID FROM Sport WHERE Sport_Name = %s"

    cur = dbConn.cursor()

    cur.execute(Query, [SportName])

    SportId = cur.fetchone()

    cur.close()

    if SportId is not None:
        return SportId[0]
    else:
        return 0


def SelectTeam(dbConn, TeamValues):
    
    Query = "SELECT Team_ID FROM Team WHERE Provider_Team_Id = %s and Team_Name = %s"

    cur = dbConn.cursor()

    cur.execute(Query, TeamValues)

    TeamId = cur.fetchone()

    cur.close()

    if TeamId is not None:
        return 0
    else:
        return 1

def InsertTeam(dbConn, InsertValues):
    
    Query = "INSERT INTO Team (Team_Name, Sport_Id, Provider_Team_Id, Provider_Id) VALUES (%s, %s, %s, %s)"

    cur = dbConn.cursor()

    cur.executemany(Query, InsertValues)

    dbConn.commit()

    cur.close()


if __name__ == "__main__":
    
    db = MySQLdb.connect(host="127.0.0.1",    # your host, usually localhost
                         user="mfarima",         # your username
                         passwd="d20m11",  # your password
                         db="rocket")        # name of the data base

    Sport = "Soccer"

    SportLeague = "English Barclays Premier League"
    SportLeagueId = 1
    SportLeagueYear = 2013

    Provider = "Opta Sportsdata"
    ProviderId = 1

    AppPath = os.path.dirname(os.path.abspath(__file__))

    XmlFile = AppPath + "\\XML\\F1 - srml-8-2013-results-mid-season-.xml"

    TeamTag="SoccerDocument/Team"

    TeamProviderIdTag = ""
    TeamProviderIdAttrib = "uID"

    TeamNameTag = "Name"
    TeamNameAttrib = ""


    XmlData = etree.parse(XmlFile)
    XmlRoot = XmlData.getroot()
    
    SportId = SelectSportId(db, Sport)
    
    InsertTeamValues = []
    i=-1

    for Teams in XmlRoot.findall(TeamTag):
        i=i+1
        TeamValues = []
        
        if TeamProviderIdTag != "":
            if TeamProviderIdAttrib != "":
                TeamProviderId = Teams.find(TeamProviderIdTag).attrib[TeamProviderIdAttrib]
            else:
                TeamProviderId = Teams.find(TeamProviderIdTag).text
        else:
            TeamProviderId = Teams.attrib[TeamProviderIdAttrib]

        if TeamNameTag != "":
            if TeamNameAttrib != "":
                TeamName = Teams.find(TeamNameTag).attrib[TeamNameAttrib]
            else:
                TeamName = Teams.find(TeamNameTag).text
        else:
            TeamName = Teams.attrib[TeamNameAttrib]

        TeamValues = [TeamProviderId , TeamName]
        
        """ 
        print(TeamProviderId + " - " + TeamName)
        print(TeamValues)

        print(TeamValues[i][0])
        print(TeamValues[i][1])
        
        """

        #InsertTeamValues = []

        if SelectTeam(db, TeamValues) == 1:
            InsertTeamValues.append([TeamName , SportId , TeamProviderId , ProviderId])

            #InsertTeamValues = (TeamName , SportId , TeamProviderId , ProviderId)

            #InsertTeam(db, InsertTeamValues)

        """
        print(Teams)
        print(Teams.tag)
        print(Teams.attrib)
        print(Teams.text)
        print(Teams.attrib["uID"])
        print(Teams.find("Name"))
        print(Teams.find("Name").tag)
        print(Teams.find("Name").attrib)
        print(Teams.find("Name").text)
        """

        XmlFile = XmlFile

    if InsertTeamValues != []:
        InsertTeam(db, InsertTeamValues)

    XmlFile = ""

    db.close()


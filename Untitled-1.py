import glob
import json
import os
#github = https://github.com/ItBePhill/Challenge-3--I-guess-
#Doesn't use any third party modules.
#Made with Python 3.10.6
#ver 1.0
#used for data that is read from json files
teamdata = {

}
indivdata = {

}
teams = 0
individuals = 0
tori = ""
teamamt =  0
members = 1
#jsonpath = "//lits.blackpool.ac.uk/Data/Student Homes/Active_Q1/289/30234289/Documents/Unit 4 Programming/Python/Challenge 3 (I guess)/"
jsonpath = "D:/programing languages/Python/Challenge 3 (I guess)/"
#dictionaries for writing to team and indiv json files
team = {
    "id" : 0,
    "name0": "",
    "name1" : "",
    "name2" : "",
    "name3" : "",
    "name4" : ""
}
individual = {
    "id" : 0,
    "name" : ""
}
def teamjsonwrite():
    with open(jsonpath+"team"+str(teams)+".json", "w") as f:
        json.dump(team, f, indent=1)
        f.close
def indivjsonwrite():
    with open(jsonpath+"indiv"+str(individuals)+".json", "w") as f:
        json.dump(individual, f, indent=1)
        f.close

def read():
    teams = []
    indivs = []
    #gets a list of every json file in the jsonpath directory
    file_type = r'\*json'
    files = glob.glob(jsonpath + file_type)
    #loops through each file from glob to check if it is a team or indiv file and append to respective lists
    for i in files:
        if os.path.splitext(os.path.basename(i))[0].find("team") != -1:
            teams.append(i)
        else:
            indivs.append(i)
    #sort file lists into order of time created and reverse order so it is descending
    teams.sort(key=lambda x: os.path.getctime(x))
    teams.reverse()
    indivs.sort(key=lambda x: os.path.getctime(x))
    indivs.reverse()
    #read from the most recent file and return the result
    with open(teams[0], "r") as f:
        team = json.load(f)
    with open(indivs[0], "r") as f:
        indiv = json.load(f)
    return team, indiv


#Checks for Team file, if file doesn't exist makes default file with 0 members and with an id of 0
if os.path.exists(jsonpath+"/team1.json") == False:
    teamjsonwrite()
#Calls read() and assigns result to teamdata
else:
    teamdata, indivdata = read()
    teams = teamdata["id"]
    individuals = indivdata["id"]
#Checks for Indiv file, if file doesn't exist makes default file with 0 members and with an id of 0

if os.path.exists(jsonpath+"/indiv1.json") == False:
    indivjsonwrite()
#Calls read() and assigns result to indivdata
else:
    #gets amount of teams and individuals from json files
    teamdata, indivdata = read()
    teams = teamdata["id"]
    individuals = indivdata["id"]
 

#Menu Code
while tori != "t" and tori != "i":
    tori = input("Teams: "+str(teams)+ "/4 Individuals: "+ str(individuals)+"/20 \nWill you be in a team or individual.\nT - team.\nI - Individual.\n-").lower()
    if(tori == "t"):
        if teams == 4:
            print("Sorry we already have enough teams, But you can enter as an individual.")
            tori = ""
        else:
            print("You may have maximum of 5 people in your team\nif you are done inputting names press enter to leave rest blank")
            teams+=1
            while members < 6:
                team["name"+str(members - 1)] = input("Name: "+str(members)+"\n-")
                members += 1
            team["id"] = teams
            teamjsonwrite()
            
    elif(tori == "i"):
        if individuals == 20:
            print("Sorry we already have enough teams, But you can enter as an individual.")
            tori = ""
        else:
            print("Successfully entered!")
            individuals+=1
            individual["id"] = individuals
            individual["name"] = input("What is your name?\n-")
            indivjsonwrite()
    else:
        print("Error: Invalid Entry")

    


            
    

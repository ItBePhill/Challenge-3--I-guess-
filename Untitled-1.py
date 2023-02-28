import glob
import json
import os
teamdata = {

}
indivdata = {

}
teams = 0
individuals = 0
tori = ""
teamamt =  0
members = 0
jsonpath = "//lits.blackpool.ac.uk/Data/Student Homes/Active_Q1/289/30234289/Documents/Unit 4 Programming/Python/Challenge 3 (I guess)/"
team = {
    "id" : 0,
    "name0": "",
    "name1" : "",
    "name2" : "",
    "name3" : "",
    "name4" : "",
    "name5" : ""
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
    folder_path = jsonpath
    file_type = r'\*json'
    files = glob.glob(folder_path + file_type)
    for i in files:
        if os.path.splitext(os.path.basename(i))[0].find("team") != -1:
            teams.append(i)
        else:
            indivs.append(i)
    # for i in range(len(teams)):
    #     idx = i
    #     for j in range(i+1, len(teams)):
    #         if os.path.getmtime(teams[i]) > os.path.getmtime(teams[idx]):
    #             idx = j
    #         teams[i], teams[idx] = teams[idx], teams[i]
    # for i in range(len(indivs)):
    #      idx = i
    #      for j in range(i+1, len(indivs)):
    #          if os.path.getmtime(indivs[i]) > os.path.getmtime(indivs[idx]):
    #              idx = j
    #          indivs[i], indivs[idx] = indivs[idx], indivs[i] 

    with open(teams[0], "r") as f:
        print(teams[0])
        team = json.load(f)
    with open(indivs[0], "r") as f:
        print(indivs[0])
        indiv = json.load(f)
    return team, indiv



        
        
if os.path.exists(jsonpath+"team1.json") == False:
    teamjsonwrite()
else:
    teamdata, indivdata = read()
    teams = teamdata["id"]
    individuals = indivdata["id"]
if os.path.exists(jsonpath+"/indiv1.json") == False:
    indivjsonwrite()
else:
    teamdata, indivdata = read()
    teams = teamdata["id"]
    individuals = indivdata["id"]
while tori != "t" and tori != "i":
    tori = input("Teams: "+str(teams)+ "/4 Individuals: "+ str(individuals)+"/20 \nWill you be in a team or individual.\nT - team.\nI - Individual.\n-").lower()
    if(tori == "t"):
        if teams == 4:
            print("Sorry we already have enough teams, But you can enter as an individual.")
            tori = ""
        else:
            print("Successfully entered!")
            teams+=1
            while members < 6:
                team["name"+str(members)] = input("Name "+str(members))
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
            indivjsonwrite()
    else:
        print("Error: Invalid Entry")

    


            
    

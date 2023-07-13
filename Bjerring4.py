#from flask import Flask
from itertools import combinations


def main():

    # Sample list - pool of 16 people, 8 girls and 8 boys
    list1 = ["Kleo","Taylor","Tina","Akon","Sarah","TBD1","TBD2","Lauren"]
    list2 = ["Mark","Evert","Roman","Michael","Steven","Thomas","Kaman","Isaiah"]

    revco = Roster(4,list1,list2)
    revco.createBracket(2,2) #two boys and two girls - will be determined by user in GUI
    revco.createMatchSets()
    revco.setMatches(2)
    revco.printRoster()


class Roster:

    setlist = set() # Used to create unique matches so there aren't duplcate teams/ID's
    matchlist = list() # Contains all possible match setups where no ID's are repeated in a single match
    finalMatches = list() # our final set of matches ready for gameplay
    def __init__(self,teamSize,girls, boys):
        self.girls = girls
        self.boys  = boys
        self.teamSize = teamSize
        count = len(girls) + len(boys)
    
    # Combinitorics formula for "Choose" or combinations - "order doesn't matter"
    def rSubset(arr,r):
        return list(combinations(arr,r))
    
    # Creates all possible unique teams with no repeated ID's using Combinations "see rSubset method"
    def createBracket(self,boyCount,girlCount):
        boy_list = Roster.rSubset(self.boys,boyCount)
        girl_list = Roster.rSubset(self.girls,girlCount)
        for i in range(len(boy_list)):
            Roster.setlist.add(boy_list[i]+girl_list[i])
        
    
    # Method creates all possible unique 4 v 4 matches from 'setlist' and stores it in 'matchlist'
    def createMatchSets(self):
        temp_setlist = list(Roster.setlist)
        main_setlist = list(Roster.setlist)
        for i in main_setlist:
            if i in temp_setlist:
                item1 = i 
                for j in main_setlist:
                    if j in temp_setlist:
                        if any(item in j for item in i) == False:
                            item2 = j 
                            Roster.matchlist.append(item1+item2)
                            #temp_setlist.remove(item1)
                            temp_setlist.remove(item2)
                            break
    
    # Method takes our created unique matches and sets up a match schedule where 1 player wont be scheduled to play on two courts at once
    # this is determined by the number of courts available, passed in by user as "activeCourts"
    def setMatches(self,activeCourts):
        temp1 = list(Roster.matchlist)
        temp2 = list(Roster.matchlist)
        roundCount = 0
        for i in temp1:
            print(i)
            print(temp2)
            roundCount+=1
            count = 0
            #rnd = "Round " + str(roundCount) +":"
            #Roster.finalMatches.append(rnd)
            Roster.finalMatches.append("Court 1:")
            Roster.finalMatches.append(i)
            #Roster.finalMatches.append(" VS ")
            temp2.remove(i)
            temp1.remove(i)
            count+=1
            for j in temp2: 
                #print("in second loop")
                if count < activeCourts:
                    if any(item in j for item in i) == False:
                        print("test")
                        Roster.finalMatches.append("Court 2:")
                        Roster.finalMatches.append(j)
                        #Roster.finalMatches.append("\n")
                        temp1.remove(j)
                        temp2.remove(j)
                        count +=1
                    else:
                        #print("test")
                        #count = 1
                        pass
                else: 
                    break

                
    def printRoster(self):
        #print(Roster.matchlist)
        print(len(Roster.setlist))
        print(Roster.setlist)
        print("\n")
        print(len(Roster.matchlist))
        print(Roster.matchlist)
        print(Roster.finalMatches)
        # for i in range(len(Roster.finalMatches)):
        #     #print("Round "+i+" :")
        #     print(Roster.finalMatches[i])
        #     print("\n")
            



# Tell Python to call our main method
if __name__ == "__main__":
  main()
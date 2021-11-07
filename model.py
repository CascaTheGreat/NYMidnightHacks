import cgi
import json
import cgitb
from werkzeug.datastructures import ImmutableMultiDict
f = open('formData.txt', 'w+')


def userInputList(allTheData):
  d=allTheData
  content_list = [d['username'],d['password'],d['person-name'],d['age'],d['bio']]
  print(content_list)
  f.write(", ".join(content_list))
  return (content_list)
  

  
    
def output(formData):
  filteredContent=userInputList(formData)
  del filteredContent[1]
  return filteredContent

def marktime(timeData):
  timeList = timeData.getlist("javascript_data[]")
  print(timeList)
  
  
  matchdata = open('match.txt', 'a')
  matchdatastring = ", ".join(timeList)
  matchdata.write(matchdatastring + "\n")
  
  #testDict
currDict = {"bobTheBoss": 10, "maggieMoo": 34, "sallyRide": 4, "finland": 63, "british": 1}

finalDict={}

with open('match.txt') as matchdata:
  for line in matchdata:
    myList=line.split(",")
    finalDict[myList[0]]=myList[1]
  

#function that takes the current dictionary of usernames and time stamps of when they clicked the egg
#returns user (as a string) who clicked the egg closest to the time the current user clicked the egg
def findYourMatch(userDict, currUser):
  #sorts our dictionary in order of smallest time to largest time (in int)
  sort_users = sorted(userDict.items(), key=lambda x: x[1], reverse=False)

  #loops through new sorted dictionary and returns the user that is closest to the user
  for i in range(len(sort_users)):
    if sort_users[i][0] == currUser:
      if (i != 0) and (i != (len(sort_users)-1)):
        beforeDist = float(sort_users[i][1])-float(sort_users[i-1][1])
        afterDist = float(sort_users[i+1][1])-float(sort_users[i][1])
        if beforeDist < afterDist:
          return(sort_users[i-1][0]) 
        else:
          return(sort_users[i+1][0])
      elif i == len(sort_users)-1:
        return(sort_users[i-1][0])
      else:
        return(sort_users[i+1][0])

print(findYourMatch(finalDict, "fred"))
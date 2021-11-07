import cgi
import json
import cgitb
from werkzeug.datastructures import ImmutableMultiDict
f = open('formData.txt', 'w+')
t = open('match.txt', 'w+')

def userInputList(allTheData):
  d=allTheData
  content_list = [d['username'],d['password'],d['person-name'],d['age'],d['bio']]
  print(content_list)
  f.write(", ".join(content_list))
  return (content_list)
  
#def ReadingTheTxt(username):
 # for line in f:
  #  if line
  
    
def output(formData):
  filteredContent=userInputList(formData)
  del filteredContent[1]
  return filteredContent

def marktime(timeData):
  timeList = timeData.getlist("javascript_data[]")
  print(timeList)
  t.write(", ".join(timeList))
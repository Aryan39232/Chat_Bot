import datetime  # Make sure to import the datetime module
from Speak import Say


def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date(): 
    date = datetime.date.today().today()
    Say(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)


def NonInputExecution(query):
    query = str(query)

    if "time" in query:
        Time()
    elif "date" in query: 
        Date()
    elif "day" in query:
        Day()

# Test your functions


def InputExecution(tag , query):
    if "wikipedia" in tag:
        name = str(query).replace("" ,"")
        import wikipedia
        result = wikipedia.summary(name)
        Say(result)

    elif "google" in tag:
        query = str(query).replace("google" , "").replace("search" ,"")
        query = query.replace("search" , "")
        import pywhatkit
        pywhatkit.search(query)
import datetime  # Make sure to import the datetime module

def Say(text):
    print(text)  # Replace this with actual code to speak the text

def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date():  # Correct function name to "Date" instead of "Dime"
    date = datetime.date.today().strftime("%Y-%m-%d")
    Say(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)


def NonInputExecution(query):
    query = str(query)

    if "time" in query:
        Time()
    elif "date" in query:  # Change "data" to "date"
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
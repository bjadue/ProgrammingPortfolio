# Brandon Jadue
# 12/3/23
# This program will ask user for name, then street address, then zip code.
# Then program will determine city/town and write to text file.

def zipSearch(usrZip):
    for line in sourceFile:
        line = line.rstrip()
        section = line.split(",")
        curZip = int(section[0])
        curState = section[1]
        curCity = section[2]
        if curZip == usrZip:
            break
    return curCity, curState

usrName = input("What is your first and last name: ")
streetAdd = input("What is your street address: ")
zipCode = input("What is your zip code: ")

def breakName(fullName):
    section = fullName.split()
    fName = section[0]
    lName = section[1]
    return fName, lName
def fixCityCaps(city):
    c1cnt = 0
    c2cnt = 0
    cityP1 = ""
    cityP2 = ""
    newCityName = ""

    try:
        section = city.split()
        word1 = section[0]
        word2 = section[1]
        for char in word1:
            if c1cnt == 0:
                cityP1 += char.upper()
            else:
                cityP1 += char.lower()
            c1cnt += 1
        for char in word2:
            if c2cnt == 0:
                cityP2 += char.upper()
            else:
                cityP2 += char.lower()
            c2cnt += 1
        newCityName = (f"{cityP1} {cityP2}")
        return newCityName
    except:
        for char in city:
            if c1cnt == 0:
                cityP1 += char.upper()
            else:
                cityP1 += char.lower()
            c1cnt += 1
        # print("Nothing was done. Moving on.")
        return cityP1

def zipCompat(oldZip):
    newZip = ""
    zipList = []
    numCounter = 0
    for i in oldZip:
        if i == "0" and numCounter == 0:
            continue
        else:
            zipList.append(i)
            numCounter += 1
    for num in zipList:
        newZip += num
    return newZip

internalZip = int(zipCompat(zipCode))

sourceFile = open("zips.csv", "r")
writingFile = open("Address.txt", "w")

firstName, lastName = breakName(usrName)
city, state = zipSearch(internalZip)
city = fixCityCaps(city)

writingFile.write(f"{lastName}, {firstName}\n{streetAdd}\n{city}, {state} {zipCode}")

#closing all
sourceFile.close()
writingFile.close()
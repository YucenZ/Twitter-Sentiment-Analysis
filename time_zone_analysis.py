# Assignment 3
# Name: Yucen Zhang (250876680)
# Prof : Jordan Van Dyk
# Class: CS1026- 001
# Created: Nov 8th 2015
# Description: This program will analysis on Twitter data provided, and computes the happy score by searching the
# keywords in tweets. It will display the total happiness score


import sys
def main():
    # Initialize the variable

    eastScore = 0
    eastCount = 0
    cenScore = 0
    cenCount = 0
    mountScore = 0
    mountCount = 0
    pacScore = 0
    pacCount = 0

    print("=" * 60)

# Stop the program if the file does not exit, and indicate error.
    try:
        tweetFile = input("Please enter the name of the tweet file:")
        infile = open(tweetFile, "r", encoding="utf-8")

    except FileNotFoundError:
        print("===== ERROR:No Such file or directory: " + "\"" + tweetFile + "\"" + " =====")
        sys.exit(1)

    # store the keywords dictionary
    keyFile = input("Please enter the name of the keywords file:")
    keywords = keyword(keyFile)

    for line in infile:

        (lat, long) = coordinate(line)
        timezone = timeZone(lat, long)

    # store the tweet text in each line into a list.
        tweet = line.split(" ", 5)
        tweetText = tweet[5].strip()
        tweetText = tweetText. split()

        for i in range(0, len(tweetText)):
            tweetText[i]=tweetText[i].strip("!,'.?/;:[]{}@~`#$%^&*")

        score = 0
        count = 0

        # looking for the keyword
        for word in keywords:
            for element in tweetText:
                if word.lower() == element.lower():
                    score += keywords[word]
                    count += 1

        # add up the score according to different timezone
        if score > 0:
            tweetScore = (score / count)

            if timezone == "Eastern":
                eastScore += tweetScore
                eastCount += 1

            elif timezone == "Central":
                cenScore += tweetScore
                cenCount += 1


            elif timezone == "Mountain":
                mountScore += tweetScore
                mountCount += 1


            elif timezone == "Pacific":
                pacScore += tweetScore
                pacCount += 1

    if eastCount>0:
        totalEast = eastScore / eastCount
    else:
        totalEast = 0

    if cenCount>0:
        totalCentral = cenScore / cenCount
    else:
        totalCentral = 0

    if mountCount>0:
        totalMount = mountScore / mountCount
    else:
        totalMount = 0

    if  pacScore>0:
        totalPac = pacScore / pacCount
    else:
        totalPac = 0

    infile.close()


    print("\n[Eastern Time Zone]  Number of Tweets: " + str(eastCount) + "\tHappiness Score: " + str(totalEast) + "\n"
        "[Central Time Zone]  Number of Tweets: " + str(cenCount) + "\tHappiness Score: " + str(totalCentral) + "\n"
        "[Mountain Time Zone] Number of Tweets: " + str(mountCount) + "\tHappiness Score: " + str(totalMount) + "\n"
        "[Pacific Time Zone]  Number of Tweets: " + str(pacCount) + "\tHappiness Score: " + str(totalPac))

    drawSimpleHistogram(totalEast,totalCentral,totalMount,totalPac)

# read through the key words file, and store each word as a key with its value in a dictionary.

def keyword(file):

    try:
        keyfile = open(file, "r")

    except FileNotFoundError:
        print("===== ERROR:No Such file or directory: " + "\"" + file + "\"" + " =====")
        sys.exit(2)


    keywords = {}

    for line in keyfile:
        line = line.strip()
        keylist = line.split(",")

        word = keylist[0]
        value = int(keylist[1])

        keywords[word] = value
    keyfile.close()
    return keywords


# for each tweet in the file, store the coordinate (latitude, longitude) as a tuple.

def coordinate(line):
    line = line.split(" ", 5)

    cordi = (line[0] + line[1]).split(",")

    lat = float(cordi[0].strip("["))
    long = float(line[1].strip("]"))

    return (lat, long)

# determining the timezone for each coordinate given. Return the timezone as a string.

def timeZone(lat, long):
    if 24.660845 <= lat < 49.189787:

        if -87.518395 <= long <= -67.444574:
            return "Eastern"

        elif -101.998892 <= long < -87.518395:
            return "Central"

        elif -115.236428 <= long < -101.998892:
            return "Mountain"

        elif -125.242264 <= long < -115.236428:
            return "Pacific"

from graphics import GraphicsWindow

def drawHappyFace(canvas,x,y):
    canvas.setColor("yellow")
    canvas.setOutline("black")
    #canvas.drawOval(100, 100, 30, 30)
    canvas.drawOval(x, y, 30, 30)
    canvas.setColor("black")
    #canvas.drawOval(108, 110, 5, 5)
    canvas.drawOval(x+8, y+10, 5, 5)
    #canvas.drawOval(118, 110, 5, 5)
    canvas.drawOval(x+18, y+10, 5, 5)
    #canvas.drawLine(110, 122, 113, 125)
    canvas.drawLine(x+10, y+22, x+13, y+25)
    #canvas.drawLine(113, 125, 117, 125)
    canvas.drawLine(x+13, y+25, x+17, y+25)
    #canvas.drawLine(117, 125, 120, 122)
    canvas.drawLine(x+17, y+25, x+20, y+22)

def drawSadFace(canvas,x,y):
    canvas.setColor("yellow")
    canvas.setOutline("black")
    #canvas.drawOval(100, 100, 30, 30)
    canvas.drawOval(x, y, 30, 30)
    canvas.setColor("black")
    #canvas.drawOval(108, 110, 5, 5)
    canvas.drawOval(x+8, y+10, 5, 5)
    #canvas.drawOval(118, 110, 5, 5)
    canvas.drawOval(x+18, y+10, 5, 5)
    #canvas.drawLine(110, 122, 113, 125)
    canvas.drawLine(x+10, y+23, x+13, y+20)
    #canvas.drawLine(113, 125, 117, 125)
    canvas.drawLine(x+13, y+20, x+17, y+20)
    #canvas.drawLine(117, 125, 120, 122)
    canvas.drawLine(x+17, y+20, x+20, y+23)

def drawSimpleHistogram(eval,cval,mval,pval):
    # Draws a simple histogram of 4 values - sentiment values from 4 regions
    # Assumes that the values are in the range of 0-10
    #
    # Parameters:
    #   - eval - value of the Eastern region
    #   - cval - value of the Central region
    #   - mval - value of the Mountain region
    #   - pval - value of the Pacific region

    win = GraphicsWindow(400, 400)
    canvas = win.canvas()
    wid = 400
    hght = 400
    C = 0.8
    facew = 30
    step = 5
    if ((wid-(80+2*facew)) < 100) or (hght < 150):
        canvas.drawText(wid/2-10,hght/2-10,"Oops! Window dimensions too small!")
    else:
        wuse = wid-(80+2*facew)
        huse = (hght-120)/5
        barx = 110+step # 80 plus width of face, which is 30, plus step
        endofbar = wid-facew-step
        canvas.drawLine(75, 0, 75, hght)
        # Draw bar for East
        canvas.drawText(2, huse, "Eastern")
        drawSadFace(canvas, 80, C*huse)
        lngth = wuse*eval/10.0
        canvas.setColor(240,0,0)
        canvas.setOutline("black")
        canvas.drawRectangle(barx, C*huse, lngth, facew)
        drawHappyFace(canvas,endofbar,C*huse)
        # Draw bar for Central
        canvas.drawText(2, 2*huse+facew, "Central")
        drawSadFace(canvas, 80, (1+C)*huse+facew)
        lngth = wuse*cval/10.0
        canvas.setColor(120,240,120)
        canvas.setOutline("black")
        canvas.drawRectangle(barx, (1+C)*huse+facew, lngth, facew)
        drawHappyFace(canvas, endofbar, (1+C)*huse+facew)
                # Draw bard for Mountain
        canvas.drawText(2, 3*huse+2*facew, "Mountain")
        drawSadFace(canvas, 80, (2+C)*huse+2*facew)
        lngth = wuse*mval/10.0
        canvas.setColor(0,0,240)
        canvas.setOutline("black")
        canvas.drawRectangle(barx, (2+C)*huse+2*facew, lngth, facew)
        drawHappyFace(canvas, endofbar, (2+C)*huse+2*facew)
        # Draw bar for Pacific
        canvas.drawText(2, 4*huse+3*facew, "Pacific")
        drawSadFace(canvas, 80, (3+C)*huse+3*facew)
        lngth = wuse*mval/10.0
        canvas.setColor(120,120,120)
        canvas.setOutline("black")
        canvas.drawRectangle(barx, (3+C)*huse+3*facew, lngth, facew)
        drawHappyFace(canvas, endofbar, (3+C)*huse+3*facew)
        win.wait()

main()

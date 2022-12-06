import json


def shellsort(genres, priceRange, timeRange, online, lines):
    n = len(lines)
    gap = n // 2
    averageprice = (priceRange[0] + priceRange[1]) // 2
    averagetime = (timeRange[0] + timeRange[1]) // 2
    while gap > 0:
        j = gap
        while j < n:
            i = j - gap
            leftrelevance = 0
            rightrelevance = 0
            rightGenre = False
            leftGenre = False
            while i >= 0:
                for index in genres:
                    if index in lines[i + gap]["Metadata"]["Genres"]:
                        rightGenre = True
                    if index in lines[i]["Metadata"]["Genres"]:
                        leftGenre = True
                if rightGenre == True:
                    if online == 2:
                        if abs(lines[i + gap]["Metrics"]["Used Price"] - averageprice) < abs(lines[i]["Metrics"]["Used Price"] - averageprice):
                            rightrelevance += 1
                        if abs(lines[i + gap]["Length"]["All PlayStyles"]["Average"] - averagetime) < abs(lines[i]["Length"]["All PlayStyles"]["Average"] - averagetime):
                            rightrelevance += 1
                    else:
                        if online == 1:
                            if lines[i + gap]["Features"]["Online?"] == True:
                                if lines[i + gap]["Metrics"]["Used Price"] > priceRange[0] and lines[i + gap]["Metrics"]["Used Price"] < priceRange[1]:
                                    rightrelevance += 1
                                if lines[i + gap]["Length"]["All PlayStyles"]["Average"] > timeRange[0] and lines[i + gap]["Length"]["All PlayStyles"]["Average"] < timeRange[1]:
                                    rightrelevance += 1
                        else:
                            if lines[i + gap]["Features"]["Online?"] == False:
                                if lines[i + gap]["Metrics"]["Used Price"] > priceRange[0] and lines[i + gap]["Metrics"]["Used Price"] < priceRange[1]:
                                    rightrelevance += 1
                                if lines[i + gap]["Length"]["All PlayStyles"]["Average"] > timeRange[0] and lines[i + gap]["Length"]["All PlayStyles"]["Average"] < timeRange[1]:
                                    rightrelevance += 1

                if leftGenre == True:
                    if online == 2:
                        if abs(lines[i]["Metrics"]["Used Price"] - averageprice) < abs(lines[i + gap]["Metrics"]["Used Price"] - averageprice):
                            leftrelevance += 1
                        if abs(lines[i]["Length"]["All PlayStyles"]["Average"] - averagetime) < abs(lines[i + gap]["Length"]["All PlayStyles"]["Average"] - averagetime):
                            leftrelevance += 1
                    else:
                        if online == 1:
                            if lines[i]["Features"]["Online?"] == True:
                                if lines[i]["Metrics"]["Used Price"] > priceRange[0] and lines[i]["Metrics"]["Used Price"] < priceRange[1]:
                                    leftrelevance += 1
                                if lines[i]["Length"]["All PlayStyles"]["Average"] > timeRange[0] and lines[i]["Length"]["All PlayStyles"]["Average"] < timeRange[1]:
                                    leftrelevance += 1
                        else:
                            if lines[i]["Features"]["Online?"] == False:
                                if lines[i]["Metrics"]["Used Price"] > priceRange[0] and lines[i]["Metrics"]["Used Price"] < priceRange[1]:
                                    leftrelevance += 1
                                if lines[i]["Length"]["All PlayStyles"]["Average"] > timeRange[0] and lines[i]["Length"]["All PlayStyles"]["Average"] < timeRange[1]:
                                    leftrelevance += 1

                if leftrelevance > rightrelevance:
                    break
                else:
                    lines[i + gap], lines[i] = lines[i], lines[i + gap]

                i = i - gap

            j += 1

        gap = gap // 2

    return lines[:15]


if __name__ == "__main__":
    # Opening JSON file
    f = open('video_games (1).json')

    # returns JSON object as
    # list of dictionaries
    lines = json.load(f)

    # Closing file
    f.close()
    
    res = shellsort(["Action"], (10, 30), (10, 30), 2, lines)

    for i in res:
        print(i)

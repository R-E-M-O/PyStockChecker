from datetime import datetime
import json
import pytz
import requests


def requestHTML(url):
    # html request
    request = requests.get(url, timeout=5)

    # return the contents
    return request.content

def writeHTML(htmlContent):

    # write the html code to a txt document
    htmlFile = open("htmlContent.txt", "w")
    htmlFile.write(htmlContent)
    htmlFile.close()

    # return the contents
    return str(htmlContent)


def inStock(htmlString):
    inStock = False

    if "" is in htmlString:
        inStock = True
    # body yet to be complete
    return inStock


def runStockCheck(url):
    # body yet to be complete

    # request new html contents from url and write to file
    htmlContent = requestHTML(url)
    htmlString = writeHTML(htmlContent)

    # check for inStock
    inStock = inStock(htmlString)

    # keep checking stock until item is in stock
    while inStock is False:
        htmlContent = requestHTML(url)
        htmlString = writeHTML(htmlContent)
        inStock = inStock(htmlString)

    #next print inStockMessage to txt file and console
    return





def main():
    # body yet to be complete

    # prompt for url and save html request content to string
    url = input("Enter a url: ")

    runStockCheck(url)


main()

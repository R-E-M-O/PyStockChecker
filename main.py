from datetime import datetime
import json
import pytz
import requests


def requestHTML(url):
    # html request
    request = requests.get(url, timeout=5)
    htmlContent = str(request.content)

    # write the html code to a txt document
    htmlFile = open("htmlContent.txt", "w")
    htmlFile.write(htmlContent)
    htmlFile.close()

    # return the contents
    return htmlContent


def runStockCheck():
    # body yet to be complete

    return


def inStock():
    inStock = False

    # body yet to be complete

    return inStock


def main():
    # body yet to be complete

    url = input("Hello World!")


main()
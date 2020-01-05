'''This program was inspired by my past experience with a clothing company named Supreme.
The website changes its entire webshop at 9:00AM PST every Thursday and has very sought-after items.
I made this to solve the issue of waiting around to refresh the webpage every few seconds. Instead, you can easily
run this program and have the script do all the work for you!
This program works based on the idea that a website's HTML code is static for the most part. However, once a website's
HTML code changes, this program will pick up on that and open the page right up.

If you would like to test this with that exact company, just enter supremenewyork.com/shop/all into the first input!
'''

import urllib.request
import urllib.parse
import time
import webbrowser

#Allows user to input whatever website they would like to monitor.
yourWebsite = input("Please enter the website you would like to use: https://www.")
while True:
    #This url is the one that will be used for the entire program.
    url = ("https://" + yourWebsite)
    #Saves the url in a variable.
    test = urllib.request.urlopen(url)
    #Save the HTML data of the page opened above into a variable
    urlinfo = test.read()

    #This next line is just to see behind the scenes. Can be uncommented if you want to read all the data.
    #print(urlinfo)

    #Waits 60 seconds before checking the website for any changes.
    time.sleep(5)

    #Once again, we save the url into a variable.
    test2 = urllib.request.urlopen(url)
    #Save the HTML data of the page opened above into a variable.
    urlinfo2 = test2.read()

    #Once again, this is just to see behind the scenes. Uncomment if you want to read the data.
    #print(urlinfo2)

    #If else statement to determine whether any element on the website has changed.
    if(urlinfo2!=urlinfo):
        print("The website has changed. The webpage will now be opened.")
        webbrowser.open_new_tab(url)
        break
    else:
        print("The website has stayed the same.")




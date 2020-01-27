# Website-HTML-Change-Monitor

This program was developed in order to solve the issue of determining when a website's HTML changes.
If the HTML of a website changes at all, the website will be opened in a new tab.

In specific, this script is meant to be used for a popular clothing company named Supreme. They have extremely sought-after
clothing on their online webstore. Every Thursday at 9AM, their webshop page updates and will have all the new merchandise.

I used to refresh the page every few seconds just to see if the website updated, but now with this script I can just keep it
running as long as I want. 

One interesting thing I noticed about this script is that it does receive an error code under 1 condition: If the website
denies the script from checking the page due to the amount of requests in a certain time span, the script will stop running.
So keep this in mind when using the script and set the time interval accordingly. (IE: websites with alot of traffic
will most likely not have an issue with tons of requests, so you can put a very small interval such as 1 second, however,
a website that does not attract a lot of traffic may deny the requests in such a short time span so you may want to set the
interval to 30 seconds).

Also, the urllib.request and urllib.parse libraries may not fully work on MacOS. If this occurs, you will have to go into the 
directory of your Python 3.x folder and run the Install Certificates.command and Update Shell Profile.command scripts.

Best of luck!

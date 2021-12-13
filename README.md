# Google-Chrome-Automation
Program to automate the Google Chrome Web Browser using Selenium.

This program demonstrates how to use Selenium for website navigation, by visiting "IMDb Top 250 movies" on the IMDB website.

Steps to run the program:

1. Determine the Google Chrome version by searching for "chrome://version/" in the URL search bar of your Google Chrome browser.
2. Using this version number, download the corresponding Google Chrome web driver for your OS from "https://chromedriver.chromium.org/downloads".
3. Extract the archive, and place the webdriver file in a convinient location.
4. Modify the "path" variable in main.py to the path of the webdriver.
5. Run main.py

If you would like to perfom different actions in the browser, you can modify the run_browser function in main.py

Note: This program uses the following external packages:
      1. selenium
      2. requests
      
      If you do not have these packages installed, you can install it with pip.
      On Windows, execute the following command: pip install <package_name>
      On Linux/macOs, execute the following command. pip3 install <package_name>
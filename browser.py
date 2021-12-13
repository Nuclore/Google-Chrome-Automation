import os # For interacting with the operating system e.g. checking if a file or directory exist, listing files in a directory etc.
import sys # For exiting the program.
from time import sleep # For pausing the program.

import requests # For checking if the response from a URL is successful.
import selenium # For handling exceptions.
from selenium import webdriver # Submodule for controlling the web browser.


class Browser:
	'''Class containing functionality for controlling the Google Chrome web browser.'''

	def __init__(self, path):
		'''Initialize an instance of the Google Chrome web browser.'''
		self.path = self.check_path(path) # Checks if the path to the web driver exists, and returns it.

		self.options = webdriver.ChromeOptions() # Creates an instance for configuring the options of the Google Chrome web driver.
		self.options.add_experimental_option('detach', True) # Enables the option for keeping the browser window open.

		self.wait_time = 10 # Seconds before connection timeout.

		self.create_web_browser(self.path) # Creates an instance of the web browser.

	def create_web_browser(self, path):
		'''Creates an instance of the web browser, with the configured options and path to the web driver.'''
		try:
			# Creates an instance of the web browser, with the configured options and path to the web driver.
			self.browser = webdriver.Chrome(options=self.options, executable_path=self.path)
			self.browser.implicitly_wait(self.wait_time) # Sets the wait time for the web browser.
		except selenium.common.exceptions.WebDriverException:
			# Displays an error if the web driver is not compatible with the browser, or if the file is not a web driver and then terminate the program.
			print(f'{path} is not compatible with Google Chrome.')
			print('Program terminated.\n')
			sys.exit() # Exits the program.

	def check_path(self, path):
		'''Checks the path to the web driver.'''
		if os.path.exists(path): # Checks if the path exists, and returns it.
			return path
		else:
			# Displays that the path does not exist, and then terminate the program.
			print(f'{path} does not exist.')
			print('Program terminated.\n')
			sys.exit() # Exits the program.

	def check_url(self, url):
		'''Checks if the URL is valid.'''
		try:
			response = requests.get(url) # Obtains a response object for the URL.
			# Checks if the status code of the response is OK, and returns True.
			if response.status_code == requests.codes.ok: 
				return True
		except requests.exceptions.ConnectionError:
			# Displays a error is the URL is invalid.
			print(f'{url} is not a valid URL.')
		except requests.exceptions.RequestException:
			# Displays an error if the request to the URL was unsuccessful.
			print(f'The request for {url} could not be processed.')

	def open(self, url):
		'''Opens the webpage at the specified URL.'''
		if self.check_url(url): # Checks if the URL is valid.
			self.browser.get(url) # Opens the webpage in the browser.

	def get_element_by_id(self, ID):
		'''Returns the HTML element by ID.'''
		try:
			return self.browser.find_element_by_id(ID)
		except selenium.common.exceptions.NoSuchElementException:
			# Displays an error if the id is invalid.
			print(f'No such id as {ID}')

	def get_element_by_class_name(self, CLASS):
		'''Returns the HTML element by its class name.'''
		try:
			return self.browser.find_element_by_class_name(CLASS)
		except selenium.common.exceptions.NoSuchElementException:
			# Displays an error that the class name is invalid.
			print(f'No such class as {CLASS}')

	def get_element_by_name(self, NAME):
		'''Returns the HTML element by its name.'''
		try:
			return self.browser.find_element_by_name(NAME)
		except selenium.common.exceptions.NoSuchElementException:
			# Displays an error if the name is invalid.
			print(f'No such name as {NAME}')

	def get_element_by_link_text(self, text):
		'''Returns the HTML element by its link text.'''
		try:
			return self.browser.find_element_by_link_text(text)
		except selenium.common.exceptions.NoSuchElementException:
			# Displays an error if the link text is invalid.
			print(f'No such link text as {text}')

	def input_text(self, element, text):
		'''Inputs text to the HTML element.'''
		if element: # Checks if the element is not empty.
			element.send_keys(text) # Sends the text to the element (e.g. search bar).
		else:
			# Displays a message that the  element is empty.
			print('The element does not have any content.\n')

	def click(self, element):
		'''Send a mouse click to the HTML element.'''
		if element: # Checks if the element is not empty.
			element.click() # Clicks the element (e.g. button)
		else:
			# Displays a message that the element is empty.
			print('The element does not have any content.\n')

	def get_tab_name(self):
		'''Returns the name of the currently opened tab.'''
		sleep(5) # Pauses the program for 5 seconds to allow the page to be fully loaded.
		return self.browser.title # Returns the name of the currently opened tab.

	def get_current_url(self):
		'''Returns the URL of the currently opened webpage.'''
		sleep(5) # Pauses the program for 5 seconds to allow the page to be fully loaded.
		return self.browser.current_url # Returns the URL of the currently opened webpage.

	def back(self):
		'''Redirects to the previous page.'''
		self.browser.back()

	def forward(self):
		'''Redirects to the next page.'''
		self.browser.forward()

	def refresh(self):
		'''Refreshes the page.'''
		self.brower.refresh()

	def quit(self):
		'''Exits the web browser.'''
		self.browser.quit()



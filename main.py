import selenium # For handling exceptions.

from browser import Browser # Class for controlling the web browser.

def run_browser(browser):
	'''Performs actions in the browser.'''
	browser.open('https://www.duckduckgo.com/') # Opens the homepage for the DuckDuckGo search engine.

	search_bar = browser.get_element_by_id('search_form_input_homepage') # Obtains the search bar element on the DuckDuckGo homepage.
	browser.input_text(search_bar, 'Top IMDB Movies') # Enters text on the search bar.

	search_button = browser.get_element_by_id('search_button_homepage') # Obtains the search button element on the DuckDuckGo homepage.
	browser.click(search_button) # Clicks the search button.

	imdb_link = browser.get_element_by_link_text('Top 250 Movies - IMDb') # Obtains the link element for the link text "Top 250 Movies - IMDb".
	browser.click(imdb_link) # Clicks the link.


if __name__ == '__main__':
	try:
		path = 'chromedriver.exe' # Path to Google Chrome web driver.
		chrome = Browser(path) # Creates an instance of the Google Chrome web browser.
		run_browser(chrome) # Performs actions in the browser.
	except selenium.common.exceptions.NoSuchWindowException:
		# Displays an error if the web browser is closed while it is running.
		print('Web browser closed.')
		print('Program terminated.\n')








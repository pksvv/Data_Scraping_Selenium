# Data_Scraping_Selenium

This repo contains code snippets for scraping web data using Selenium and BeautifulSoup

Setup Pre-requisites

### Python 3.6
### Selenium - pip install selenium or conda install --name myenv selenium
### BeautifulSoup

### Install PhantomJS (steps for Ubuntu listed below)

	sudo apt-get upgrade -y
	sudo apt-get update -y
	sudo shutdown -r now
	sudo apt-get install build-essential chrpath libssl-dev libxft-dev libfreetype6-dev libfreetype6 libfontconfig1-dev libfontconfig1 -y
	sudo wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
	sudo tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 -C /usr/local/share/
	sudo ln -s /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/

	phantomjs --version

### Recently, getting messages that PhantomJS is being deprecated, so have chromium-webdriver installed as well
	sudo apt install chromium-chromedriver

The script "sel2.py" contains examples for both PhantomJS and ChromeDriver headless


from appium import webdriver

def initialize_driver(options):
    return webdriver.Remote("http://127.0.0.1:4723", options=options)
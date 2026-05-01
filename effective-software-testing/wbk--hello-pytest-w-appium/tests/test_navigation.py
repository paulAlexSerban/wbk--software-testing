def test_website_title(setup_driver):
    """Test to verify the website title."""
    driver = setup_driver
    driver.get("https://www.paulserban.eu")

    title = driver.find_element("tag name", "h1")
    assert "Welcome" in title.text

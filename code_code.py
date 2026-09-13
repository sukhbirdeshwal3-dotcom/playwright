import pytest
import allure
from playwright.sync_api import sync_playwright, Page

URL = "https://practicetestautomation.com/practice-test-login/"

@pytest.fixture()
def page():
  with sync_playwright() as p:
     browser = p.chromium.launch(headless=False, slow_mo=5000)
     page = browser.new_page()

     yield page

     browser.close()



# Test Case 1
def test_valid_username_valid_password(page: Page):
    page.goto(URL)

    page.get_by_label("username").fill("student")
    page.get_by_label("password").fill("Password123")
    page.get_by_role("button", name="Submit").click()


# Test Case 2
def test_blank_username_valid_password(page: Page):
    page.goto(URL)

    page.locator("#username").fill("")
    page.locator("#password").fill("Password123")
    page.locator("#submit").click()


# Test Case 3
def test_blank_username_blank_password(page: Page):
    page.goto(URL)

    page.locator("#username").fill("")
    page.locator("#password").fill("")
    page.locator("#submit").click()


# Test Case 4
def test_valid_username_blank_password(page: Page):
    page.goto(URL)

    page.locator("#username").fill("student")
    page.locator("#password").fill("")
    page.locator("#submit").click()


# Test Case 5
def test_invalid_username_valid_password(page: Page):
    page.goto(URL)

    page.locator("#username").fill("students")
    page.locator("#password").fill("Password123")
    page.locator("#submit").click()

# Test case 6
def test_number(page: Page):
    page.goto(URL)

    page.locator("#username").fill("123456")
    page.locator("#password").fill("Password123")
    page.locator("#submit").click()

# Test case 7
def test_number_password(page: Page):
    page.goto(URL)

    page.locator("#username").fill("123456")
    page.locator("#password").fill("12345")
    page.locator("#submit").click()






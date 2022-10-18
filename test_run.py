from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    page.goto("https://floward.com/")

    page.get_by_role("link", name="Kuwait Kuwait").click()
    page.wait_for_url("https://floward.com/en-kw")

    page.get_by_test_id("TestId__HeaderLoginLink").click()
    page.wait_for_url("https://floward.com/en-kw/login?url=/en-kw")

    page.get_by_label("Email").click()

    page.get_by_label("Email").fill("test3@gmail.com")

    page.get_by_label("Email").press("Tab")

    page.get_by_label("Password").fill("123456")

    page.get_by_role("button", name="Login").click()

    page.goto("https://floward.com/en-kw")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

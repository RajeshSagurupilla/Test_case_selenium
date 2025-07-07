from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TestCaseInput(BaseModel):
    test_case: str

@app.post("/run-test")
def run_test_case(data: TestCaseInput):
    test_case = data.test_case.lower()

    driver = webdriver.Chrome()  # Make sure chromedriver is installed
    try:
        if "example.com" in test_case:
            driver.get("https://practicetestautomation.com/practice-test-login/")
            time.sleep(2)

        if "click on login" in test_case:
            login = driver.find_element(By.LINK_TEXT, "Login")
            login.click()
            time.sleep(2)

        if "enter username" in test_case:
            username_input = driver.find_element(By.NAME, "username")
            username_input.send_keys("testuser")

        if "enter password" in test_case:
            password_input = driver.find_element(By.NAME, "password")
            password_input.send_keys("password123")

        if "click submit" in test_case:
            submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
            submit_btn.click()

        return {"status": "Test case executed successfully"}

    except Exception as e:
        return {"error": str(e)}
    finally:
        time.sleep(5)
        driver.quit()

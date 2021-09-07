import os
import keyboard
from selenium import webdriver
import time
import os

token_ask = input("C'est quoi le token ? > ")


def login():
    keyboard.write("function login(token) {")
    keyboard.write("setInterval(() => {")
    keyboard.write(
        'document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`')
    keyboard.write("}, 50);")
    keyboard.write("setTimeout(() => {")
    keyboard.write("location.reload();")
    keyboard.write("}, 200);")
    keyboard.write("}")
    keyboard.write('login("{}")'.format(token_ask))
    time.sleep(0.5)
    keyboard.press_and_release("enter")


driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://discord.com/login")
time.sleep(2)
keyboard.press_and_release("ctrl+shift+j")
time.sleep(2)
login()

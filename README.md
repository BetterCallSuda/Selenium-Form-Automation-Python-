Subject: README.md – Selenium Form Automation Project

# 📝 Selenium Form Automation (Python)

## 📌 Project Overview

This project demonstrates **automating a web form submission** using **Selenium WebDriver with Python**.
The script opens a signup form, fills in user details (first name, last name, email), submits the form, and then closes the browser.

This project is ideal for understanding **real-world form automation**, **XPath usage**, and **basic Selenium workflows**.

---

## 🛠️ Technologies Used

* **Python**
* **Selenium WebDriver**
* **Google Chrome**
* **XPath selectors**

---

## 🌐 Website Automated

```
https://secure-retreat-92358.herokuapp.com/
```

This page contains a simple HTML form with:

* First Name
* Last Name
* Email
* Submit Button

---

## ⚙️ Features

* Opens a live web form
* Locates input fields using **XPath**
* Enters user data programmatically
* Submits the form automatically
* Closes the browser after submission

---

## 🧠 Concepts Covered

* Selenium WebDriver setup
* XPath element selection
* `send_keys()` for input automation
* `click()` for form submission
* Browser session control using `driver.quit()`

---

## 🚀 How the Script Works

1. Opens the target website using Selenium
2. Locates input fields using absolute XPath
3. Fills in:

   * First Name
   * Last Name
   * Email
4. Clicks the submit button
5. Closes the browser

---

## 🧪 Code Snippet

```python
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.XPATH, '/html/body/form/input[1]')
first_name.send_keys("Sudharson")

second_name = driver.find_element(By.XPATH, '/html/body/form/input[2]')
second_name.send_keys("S")

email = driver.find_element(By.XPATH, '/html/body/form/input[3]')
email.send_keys("suda@gmail.com")

submit = driver.find_element(By.XPATH, '/html/body/form/button')
submit.click()

driver.quit()
```

---

## 📦 Installation & Setup

### 1️⃣ Install Selenium

```bash
pip install selenium
```

### 2️⃣ Setup ChromeDriver

* Install **Google Chrome**
* Download matching **ChromeDriver**
* Add it to your system PATH

### 3️⃣ Run the Script

```bash
python main.py
```

---

## ⚠️ Important Notes

* Absolute XPath is used (may break if page structure changes)
* For production-level automation, **relative XPath or CSS selectors** are recommended
* No waits are added since the page loads instantly

---

## 📈 Future Improvements

* Use `WebDriverWait` instead of direct element access
* Replace absolute XPath with relative XPath
* Read user input dynamically
* Add form validation checks
* Add headless browser support

---

## 🎯 Learning Outcome

Through this project, I learned:

* How to automate form submissions
* How XPath works in Selenium
* How to interact with input fields and buttons
* How browser automation is applied in testing and data entry tasks

---

## 🧑‍💻 Author

**Sudharson S**

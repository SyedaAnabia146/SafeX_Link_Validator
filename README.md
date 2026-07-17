# SafeX Solutions — SQA Internship Week 2
## Project: Documentation – Process-Improvement Proposal

This repository contains the individual contribution for Week 2 of the SafeX Solutions SQA Internship Program. The focus of this task is to identify a process inefficiency within the platform and implement an automated process-level improvement to eliminate it permanently.

---

## 📌 Problem Statement
During exploratory testing, it was identified that the social media icons in the website footer (Facebook, Instagram, LinkedIn, Twitter) point to the generic platform homepages rather than SafeX's official business handles. 
* **Business Risk:** This gap causes a loss of potential leads, weakens online brand credibility, and results in unoptimized traffic from marketing efforts.
* **SQA Gap:** Manual testing often overlooks destination-URL accuracy under tight deadlines, verifying only that the links are clickable.

## 🚀 Proposed Solution
To replace error-prone manual verification with an automated process, this repository introduces **`link_validator.py`**. This lightweight automated pre-deployment script parses the target pages to flag both dead/broken URLs and generic platform homepages before changes are pushed to production.

---

## 📂 Repository Contents
* **`link_validator.py`**: Core Python automation script utilizing `requests` and `BeautifulSoup4`.
* **`Process-Improvement-Proposal.docx`**: Detailed official proposal analyzing business impact, testing constraints, and process flow.
* **`Week2-Progress-Report.docx`**: Official weekly report detailing tasks planned, key accomplishments, and deliverables.

---

## 🛠️ Setup & Execution Guide

### 1. Prerequisites
Ensure you have Python 3 installed on your system.

### 2. Install Dependencies
Run the following command in your terminal to install the required automated testing libraries:
```bash
pip install requests beautifulsoup4
3. Run the Audit Script
Execute the script using the command below:

Bash
python link_validator.py
📋 Sample Automated Output
Plaintext
[+] Scanning website: [https://safexsolutions.com](https://safexsolutions.com) for generic social links...

⚠️ FLAG: Generic link found! -> [https://www.instagram.com/](https://www.instagram.com/) (Anchor Text: '')
⚠️ FLAG: Generic link found! -> [https://www.linkedin.com/](https://www.linkedin.com/) (Anchor Text: '')
⚠️ FLAG: Generic link found! -> [https://www.facebook.com/](https://www.facebook.com/) (Anchor Text: '')

[!] Audit Complete: Found 10 generic links that need to be updated.
Prepared by: Syeda Anabia — SQA / Manual Testing Intern (Group 41)


import requests
from bs4 import BeautifulSoup

# Target URL of the website 
TARGET_URL = "https://safexsolutions.com/"

# Generic social media platforms patterns to flag
GENERIC_PATTERNS = [
    "facebook.com/", "instagram.com/", "linkedin.com/", "twitter.com/"
]

def check_links():
    print(f"[+] Scanning website: {TARGET_URL} for generic social links...\n")
    try:
        # Fetching the webpage content with a timeout limit
        response = requests.get(TARGET_URL, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extracting all anchor tags with href attributes
        links = soup.find_all('a', href=True)
        
        flagged_links = 0
        for link in links:
            href = link['href']
            
            # Check if the link matches any target social media platform
            for pattern in GENERIC_PATTERNS:
                if pattern in href:
                    # Isolate the path after the domain name to check for a specific profile handle
                    path = href.split(pattern)[-1].strip("/")
                    
                    # If the path is empty or just a placeholder, it means it points to the generic homepage
                    if not path or path == "#":
                        print(f"⚠️ FLAG: Generic link found! -> {href} (Anchor Text: '{link.text.strip()}')")
                        flagged_links += 1
                        
        # Displaying the final audit results
        if flagged_links == 0:
            print("✅ All social media links look customized and correct!")
        else:
            print(f"\n[!] Audit Complete: Found {flagged_links} generic links that need to be updated.")
            
    except Exception as e:
        print(f"❌ Error scanning website: {e}")

if __name__ == "__main__":
    check_links()
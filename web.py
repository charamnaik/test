import re
from urllib.request import urlopen

# Function to extract the social links, email, and contact details from a website
def extract_info(url):
    # Open the website
    html = urlopen(url).read().decode('utf-8')
    
    # Use regular expressions to extract the social links, email, and contact details
    social_links = re.findall(r'https?://(www\.)?(facebook|twitter|linkedin|instagram|youtube)\.com/[a-zA-Z0-9/]+', html)
    email = re.findall(r'[\w\.-]+@[\w\.-]+',html)
    contact = re.findall(r'\+?\d{1,3} ?\d{3} ?\d{3} ?\d{4}',html)
    
    
    # Return the extracted info
    return (social_links, email, contact)

# Test the function
url = "https://ful.io"
social_links, email, contact = extract_info(url)

# Print the extracted info
print("Social links:", social_links)
print("Email:", email)
print("Contact:", contact)
"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"

"""

def domain_name(url):
    prefix=["https://www.", "http://www.", 'http://', 'https://', 'www.' ]
    try:
        return [url.replace(pre, "") for pre in prefix if pre in url ][0].split('.')[0]
    except:
        return url.split('.')[0]

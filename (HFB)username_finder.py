# Made By D3F417 - With Purple Heart
# Kidi Don't Copy This Code ! 
# GitHub : https://github.com/mss-d3f417
# Site : https://d3f417.info


import requests  
import argparse  
import concurrent.futures  
from collections import OrderedDict  
from colorama import init, Fore  
import time  
import random  


init()


WEBSITES = OrderedDict([
    ("Instagram", "https://www.instagram.com/{}"),
    ("Facebook", "https://www.facebook.com/{}"),
    ("YouTube", "https://www.youtube.com/user/{}"),
    ("Reddit", "https://www.reddit.com/user/{}"),
    ("GitHub", "https://github.com/{}"),
    ("Twitch", "https://www.twitch.tv/{}"),
    ("Pinterest", "https://www.pinterest.com/{}/"),
    ("TikTok", "https://www.tiktok.com/@{}"),
    ("Flickr", "https://www.flickr.com/photos/{}")
])

REQUEST_DELAY = 2  
MAX_RETRIES = 3  
last_request_times = {}  
def check_username(website, username):

    url = website.format(username)  
    retries = 0  

    
    while retries < MAX_RETRIES:
        try:
            
            current_time = time.time()
            if website in last_request_times and current_time - last_request_times[website] < REQUEST_DELAY:
                delay = REQUEST_DELAY - (current_time - last_request_times[website])
                time.sleep(delay)  

            response = requests.get(url)  
            last_request_times[website] = time.time()  

            if response.status_code == 200:  
                return url
            else:
                return False
        except requests.exceptions.RequestException:
            retries += 1  
            delay = random.uniform(1, 3)  
            time.sleep(delay)  

    return False  

def main():
    
    parser = argparse.ArgumentParser(description="Check if a username exists on various websites.")
    parser.add_argument("username", help="The username to check.")
    parser.add_argument("-o", "--output", help="Path to save the results to a file.")
    args = parser.parse_args()

    username = args.username  
    output_file = args.output  

    print(f"{Fore.GREEN}Hugs For Bugs | Made By D3F417")
    print(f"Checking for username: {username}")

    results = OrderedDict()  

    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        
        futures = {executor.submit(check_username, website, username): website_name for website_name, website in WEBSITES.items()}
        for future in concurrent.futures.as_completed(futures):
            website_name = futures[future]  
            try:
                result = future.result()  
            except Exception as exc:
                print(f"{website_name} generated an exception: {exc}")
                result = False
            finally:
                results[website_name] = result  

    
    print("\nResults:")
    for website, result in results.items():
        if result:
            print(f"{Fore.GREEN}{website}: Found :) ({result})")
        else:
            print(f"{Fore.RED}{website}: Not Found :( ")

    
    if output_file:
        with open(output_file, "w") as f:
            for website, result in results.items():
                if result:
                    f.write(f"{website}: Found ({result})\n")
                else:
                    f.write(f"{website}: Not Found\n")
        print(f"{Fore.GREEN}\nResults saved to {output_file} Thx For Using HFB Tools :D")


main()
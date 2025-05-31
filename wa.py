import requests
import json
import argparse
import os

TOKEN_FILE = ".resources/.token.auth"
URL_FILE = ".resources/.url.auth"
VERSION = "Recluse×2.0.5"

def save_token(token):
    with open(TOKEN_FILE, "w") as f:
        f.write(token.strip())
    print("Token saved to token.auth")

def load_token():
    if not os.path.exists(TOKEN_FILE):
        raise FileNotFoundError("Token file not found. Use --token or -t to save your token first.")
    with open(TOKEN_FILE, "r") as f:
        return f.read().strip()

def save_url(url):
    with open(URL_FILE, "w") as f:
        f.write(url.strip())
    print("URL saved to url.auth")

def load_url():
    if not os.path.exists(URL_FILE):
        raise FileNotFoundError("URL file not found. Use --url or -u to save the API URL first.")
    with open(URL_FILE, "r") as f:
        return f.read().strip()

def get_args():
    parser = argparse.ArgumentParser(
        description="Send a document via UltraMsg API",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-t', '--token', type=str, help='Save API token')
    parser.add_argument('-u', '--url', type=str, help='Save base API URL (excluding /messages/document)')
    parser.add_argument('-n', '--number', type=str, help='Mobile number with country code (e.g. +911234567890)')
    parser.add_argument('-d', '--docfile', type=str, help='Document URL to send')
    parser.add_argument('-f', '--filename', type=str, help='Filename for the document (e.g. report.pdf)')
    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {VERSION}')
    return parser.parse_args()

def main():
    args = get_args()

    # Save token and/or URL, then exit immediately
    if args.token:
        save_token(args.token)

    if args.url:
        save_url(args.url)

    if args.token or args.url:
        return  # Exit after saving token or URL

    # Load saved token and base URL
    try:
        token = load_token()
        base_url = load_url()
    except FileNotFoundError as e:
        print(e)
        return

    # Prompt for missing values
    number = args.number or input("\nEnter mobile number with country code (e.g. +911234567890)\n╰┈┈➤ ").strip()
    if not number:
        print("Error: Mobile number is required.")
        return

    docfile = args.docfile or input("\nEnter Document URL to send\n╰┈┈➤ ").strip()
    if not docfile:
        print("Error: Document URL is required.")
        return

    filename = args.filename or input("\nEnter Filename for the document (e.g. report.pdf)\n╰┈┈➤ ").strip()
    if not filename:
        print("Error: Filename is required.")
        return

    # Compose and send request
    full_url = f"{base_url.rstrip('/')}/messages/document"
    payload = {
        "token": token,
        "to": number,
        "document": docfile,
        "filename": filename,
        "content_type": "application/vnd.android.package-archive",
        "priority": "10",
        "referenceId": "",
        "msgId": "",
        "mentions": ""
    }

    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(full_url, data=json.dumps(payload), headers=headers)
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

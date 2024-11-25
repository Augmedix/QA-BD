import requests
from requests.structures import CaseInsensitiveDict


def check_conversation_api_response_data(token):
    url = "https://stage-api2.augmedix.com/feedback/v1/conversation/nrt_messaging_provider@augmedix.com22030"

    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json, text/plain, */*"
    headers["accept-language"] = "en-US,en;q=0.9"
    headers[
        f"authorization"] = f"Bearer {token}"
    headers["sec-fetch-dest"] = "empty"
    headers["sec-fetch-mode"] = "cors"
    headers["sec-fetch-site"] = "same-site"
    headers[
        "user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"

    resp = requests.get(url, headers=headers)
    latest_message = resp.json()[0]['content']
    print(latest_message)
    return latest_message

if __name__ == "__main__":
    check_conversation_api_response_data(
        'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjb20uYXVnbWVkaXgiLCJleHAiOjE2NTcxNTAzMTIsInVpZCI6MjAwMTgsInJscyI6WyJTQ1JJQkUiXX0.VoF8hEpRQrr6Y-lT_-ECYWuq8d6e3s40PXA6ZJwbLXs')
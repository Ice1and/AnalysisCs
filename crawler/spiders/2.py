import requests
print(requests.get(
    "https://steamcommunity.com/market/",
    proxies={
        "http": "http://tyufqaww:k9gcmi7lgnx1@38.154.227.167:5868/",
        "https": "http://tyufqaww:k9gcmi7lgnx1@38.154.227.167:5868/"
    },
    headers={
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
        "Referer": "https://steamcommunity.com/profiles/76561199405541900/inventory/",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": "timezoneOffset=28800,0; browserid=83994221101422839; strInventoryLastContext=730_2; sessionid=234dfadcb2938cf5881da205; steamLoginSecure=76561199548892760%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MDAwRF8yNjg0Qzk0Q184OEY2MSIsICJzdWIiOiAiNzY1NjExOTk1NDg4OTI3NjAiLCAiYXVkIjogWyAid2ViOmNvbW11bml0eSIgXSwgImV4cCI6IDE3NTE4Njk0OTIsICJuYmYiOiAxNzQzMTQyMjQ4LCAiaWF0IjogMTc1MTc4MjI0OCwgImp0aSI6ICIwMDA4XzI2OTFFQzVFXzE5NEVFIiwgIm9hdCI6IDE3NTExOTY2OTIsICJydF9leHAiOiAxNzY5MTEwMzA0LCAicGVyIjogMCwgImlwX3N1YmplY3QiOiAiMTExLjI0My42NS4xNjgiLCAiaXBfY29uZmlybWVyIjogIjExMS4yNDMuNjUuMTY4IiB9.xEgQECW2V7Uz33_8M9mdmA1HFZCv405l5V-6tJcDRG-LXXgxM02RQu4sWHE5wcMbS9uIMuWvfE3UhGthBhllCA; steamCountry=HK%7Cea2372d8061403eefc34b1bad8f99fdf; recentlyVisitedAppHubs=730; rgTopicView_General_3381077=%7B%223780245614654210047%22%3A1751784513%7D; app_impressions=730@2_9_100006_100202; rgTopicView_General_4009259_7=%7B%223468361193658091414%22%3A1751784570%7D; webTradeEligibility=%7B%22allowed%22%3A0%2C%22reason%22%3A16424%2C%22allowed_at_time%22%3A1752389558%2C%22steamguard_required_days%22%3A15%2C%22new_device_cooldown_days%22%3A0%2C%22expiration%22%3A1751785059%2C%22time_checked%22%3A1751784759%7D"
    }
).text)
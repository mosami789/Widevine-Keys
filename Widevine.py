import requests

class Widevine:
    
    def __init__(self , pssh):
        self.__pssh = pssh
        self.__license_url = ""
        
        
    def GetCK(self):
        api_url = "https://cdrm-project.com/api"
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (Ktesttemp, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
        return requests.post(api_url,headers=headers ,json={"license":self.__license_url,"pssh":self.__pssh}).text

    def convert_headers(input_string):
        output_string = ""
        if input_string:
            lines = input_string.split("\n")
            formatted_lines = []
            for line in lines:
                key, value = line.split(": ", 1)
                formatted_line = f"{key}: \"{value}\""
                formatted_lines.append(formatted_line)
            output_string = "\n".join(formatted_lines)
        return output_string

    def RequestCK(license , Headers , pssh , buildInfo , proxy , cache):
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'DNT': '1',
            'Origin': 'https://cdrm-project.com',
            'Pragma': 'no-cache',
            'Referer': 'https://cdrm-project.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'X-KL-Ajax-Request': 'Ajax_Request',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        json_data = {
            'license': license,
            'headers': Headers,
            'pssh': pssh,
            'buildInfo': buildInfo,
            'proxy': proxy,
            'cache': cache,
        }
        response = requests.post('https://cdrm-project.com/wv', headers=headers, json=json_data)
        return response.text

    def CountKeys():
        headers = {'Referer': 'https://cdrm-project.com/','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',}
        response = requests.get('https://cdrm-project.com/count', headers=headers)
        return response.text
    
    def GetPSSH(url):
        headers = {'Referer': 'https://cdrm-project.com/','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',}
        response = requests.get(url, headers=headers)
        return response.text
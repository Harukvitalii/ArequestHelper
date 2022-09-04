import aiohttp
import requests
import json



class AREQUEST_MANAGER:
    def __init__(self,BOT_API,ADMIN_ID):
        self.bot_api = BOT_API
        self.admin_id = ADMIN_ID
        pass


    async def get_json_post(self,client: aiohttp.ClientSession, url: str,data, proxy) -> dict:
        if proxy == None: 
            async with client.request('post', url, data = json.dumps(data), ssl=False) as response:
                try: 
                    response.raise_for_status()
                except aiohttp.client_exceptions.ClientResponseError:
                    print(response)
                    return 'ClientResponseError'
                return await response.json(content_type=None)
        else: 
            async with client.request('post', url, data = json.dumps(data),proxy=proxy[0], proxy_auth=proxy[1], ssl=False) as response:
                try: 
                    response.raise_for_status()
                except aiohttp.client_exceptions.ClientResponseError:
                    print(response)
                    return 'ClientResponseError'
                return await response.json(content_type=None)


    async def get_json_get(self,client: aiohttp.ClientSession, url: str,proxy) -> dict:
        if proxy == None: 
            async with client.request('GET', url,ssl=False,timeout=self.timeout_seconds) as response:
                response.raise_for_status()
                return await response.json(content_type=None)
        else: 
            async with client.request('GET', url,proxy=proxy[0], proxy_auth=proxy[1],ssl=False,timeout=30) as response:
                response.raise_for_status()
                return await response.json(content_type=None)
        


    async def bot_notify(self,text):
        URL = 'https://api.telegram.org/bot' + self.bot_api +'/sendMessage'
        PARAMS = {'chat_id':self.admin_id,
                    "text":text}
        r = requests.get(url = URL, params = PARAMS,verify=False)
        return r

    def bot_notify_normal(self,text):
        URL = 'https://api.telegram.org/bot' + self.bot_api +'/sendMessage'
        PARAMS = {'chat_id':self.admin_id,
                    "text":text}
        r = requests.get(url = URL, params = PARAMS,verify=False)
        return r
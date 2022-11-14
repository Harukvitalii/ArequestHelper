import aiohttp
import requests
import json
import asyncio
import time
import ignore



class AREQUEST_MANAGER:
    def __init__(self,BOT_API,ADMIN_ID):
        self.bot_api = BOT_API
        self.admin_id = ADMIN_ID
        pass


    async def get_json_post(self,client: aiohttp.ClientSession, url: str,data, proxy) -> dict:
        data = json.dumps(data) if data != None else None
        if proxy == None: 
            async with client.request('post', url, data = data, ssl=False) as response:
                try: 
                    response.raise_for_status()
                except aiohttp.client_exceptions.ClientResponseError:
                    print(response)
                    return 'ClientResponseError'
                return await response.json(content_type=None)
        else: 
            async with client.request('post', url, data = data,proxy=proxy[0], proxy_auth=proxy[1], ssl=False) as response:
                try: 
                    response.raise_for_status()
                except aiohttp.client_exceptions.ClientResponseError:
                    print(response)
                    return 'ClientResponseError'
                return await response.json(content_type=None)


    async def get_json_get(self,client: aiohttp.ClientSession, url: str,proxy) -> dict:
        if proxy == None: 
            async with client.request('GET', url,ssl=False,timeout=30) as response:
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
    
    
    def bot_report(self,text, BOT_TOKEN):
        URL = 'https://api.telegram.org/bot' + BOT_TOKEN +'/sendMessage'
        PARAMS = {'chat_id':self.admin_id,
                    "text":text}
        r = requests.get(url = URL, params = PARAMS,verify=False)
        return r
    
    
    def run_function_with_exception(self, func, start_abr_for_notification: str, func_args = (),  tries: int = 10,attempt = 1, otladka: bool = False):
        if otladka:
            asyncio.run(func(func_args))
            print('done Success')
            exit()
            
            
        while attempt != tries:
            try: 
                asyncio.run(func(func_args))

            except KeyError:
                print('Login Please') 
                self.bot_notify_normal(f'{start_abr_for_notification} ERROR Login Please')

            except aiohttp.client_exceptions.ClientOSError:
                print('-------------------------------------------EROR Winodws closed connection-------------------------------------------')
                time.sleep(10)
                self.run_function_with_exception(func,start_abr_for_notification,attempt=attempt+1)
                self.bot_notify_normal(f'{start_abr_for_notification} ERROR Winodws closed connection\nAttempt {attempt+1}')
            except Exception as err:
                print(err)
                print('-------------------------------------------EROR-------------------------------------------')
                time.sleep(10)
                self.bot_notify_normal(f'{start_abr_for_notification} ERROR {err}\nAttempt {attempt+1}')
                self.run_function_with_exception(func,start_abr_for_notification,attempt=attempt+1)
        
        self.bot_notify_normal(f'{start_abr_for_notification} RESTART')


import aiohttp , asyncio
from arequestsHelper import AREQUEST_MANAGER


REPORT_TOKEN = '5739820723:AAG5PxkMVnogJ1_RIz9riTlWGPA6zeWLK6U'
BOT_API      = '5511110722:AAFQnuBa7YzQwnz9BErqR0Bx613bcFidfTs'
ADMIN        =  682382931
 
async def main(AH: AREQUEST_MANAGER): 
    proxies = ["45.89.19.117:9836:puaO6Y:l8EKZ4ar96",]
    proxies = [proxy.split(':') for proxy in proxies]
    proxies = [[f'http://{proxy[0]}:{proxy[1]}',aiohttp.BasicAuth(proxy[2],proxy[3])] for proxy in proxies]
    
    
    url = 'https://api64.ipify.org?format=json'
    async with aiohttp.ClientSession() as s: 
        r = await AH.get_json_get(s, url, proxies[0])
        print(r)
 
 
if __name__ == "__main__":
    AH = AREQUEST_MANAGER('234','234')
    
    AH.run_function_with_exception(main,'TEST AREQV', AH,otladka=True)      

# proxy_com
# "176.9.29.18:10097:dropharuk:P8ukS9jDVH",
# "176.9.29.18:10098:dropharuk:P8ukS9jDVH",
# "176.9.29.18:10099:dropharuk:P8ukS9jDVH",
# "176.9.29.18:10100:dropharuk:P8ukS9jDVH",
# "176.9.29.18:10101:dropharuk:P8ukS9jDVH",
# "176.9.29.18:10276:dropharuk:P8ukS9jDVH",
# "176.9.29.18:10277:dropharuk:P8ukS9jDVH",
# "176.9.29.18:10278:dropharuk:P8ukS9jDVH",
# "176.9.29.18:10279:dropharuk:P8ukS9jDVH",
# "176.9.29.18:10280:dropharuk:P8ukS9jDVH",

#proxy-seller
# "176.9.29.18:10281:dropharuk0z5IS:TJuckYfZfp",
# "176.9.29.18:10282:dropharuk0z5IS:TJuckYfZfp",
# "176.9.29.18:10283:dropharuk0z5IS:TJuckYfZfp",
# "176.9.29.18:10284:dropharuk0z5IS:TJuckYfZfp",
# "176.9.29.18:10285:dropharuk0z5IS:TJuckYfZfp",


#ru ip olimp shop end 01.01.2023
# "45.89.19.62:11210:nI6w6O:yrJQDrO6fV",  #

  
"45.89.19.117:9836:puaO6Y:l8EKZ4ar96",     #   истекает 2022-12-31 17:32:19
"45.89.18.241:17572:puaO6Y:l8EKZ4ar96",     #   истекает 2022-12-31 17:32:19
"45.89.19.94:4356:puaO6Y:l8EKZ4ar96",     #   истекает 2022-12-31 17:32:19
"45.89.19.72:11728:puaO6Y:l8EKZ4ar96",     #   истекает 2022-12-31 17:32:19
"45.89.19.108:4346:puaO6Y:l8EKZ4ar96",     #   истекает 2022-12-31 17:32:19
"45.89.18.235:17668:puaO6Y:l8EKZ4ar96",     #   истекает 2022-12-31 17:32:19
"45.89.19.26:12738:puaO6Y:l8EKZ4ar96",     #   истекает 2022-12-31 17:32:19
"45.89.19.105:16290:puaO6Y:l8EKZ4ar96",     #   истекает 2022-12-31 17:32:19
"45.89.19.32:17996:puaO6Y:l8EKZ4ar96",     #   истекает 2022-12-31 17:32:19
"45.89.19.74:13818:puaO6Y:l8EKZ4ar96",     #   истекает 2022-12-31 17:32:19


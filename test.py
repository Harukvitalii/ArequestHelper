import aiohttp , asyncio
from arequestsHelper import AREQUEST_MANAGER


REPORT_TOKEN = '5739820723:AAG5PxkMVnogJ1_RIz9riTlWGPA6zeWLK6U'
BOT_API      = '5511110722:AAFQnuBa7YzQwnz9BErqR0Bx613bcFidfTs'
ADMIN        =  682382931
 
async def main(AH: AREQUEST_MANAGER): 
    url = 'https://api.stepn.com/run/orderlist?order=2001&chain=103&refresh=true&page=0&type=603&gType=&quality=1&level=1031&bread=1008&sessionID=nP6O7WD25WC1JUBL:1669738410903:3397926'
    async with aiohttp.ClientSession() as s: 
        r = await AH.get_json_get(s, url, None)
     
 
 
if __name__ == "__main__":
    AH = AREQUEST_MANAGER('234','234')
    
    AH.run_function_with_exception(main,'TEST AREQV', AH,otladka=True)      
    
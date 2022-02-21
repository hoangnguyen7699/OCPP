# import asyncio
# import logging
# from urllib import request
# import websockets

# from ocpp.v201 import call
# from ocpp.v201 import ChargePoint as cp
# from datetime import datetime
# from ocpp.routing import on
# logging.basicConfig(level=logging.INFO)


# class ChargePoint(cp):

#     async def send_boot_notification(self):
#         request = call.BootNotificationPayload(
#                 charging_station={
#                    'model': 'Wallbox XYZ',
#                    'vendor_name': 'anewone'
#                },
#                reason="PowerUp"
#         )
#         response = await self.call(request)

#         if response.status == 'Accepted':
#             print("Connected to central system.")
#         print(response)

    
#     # async def authentication(self):
#     #     request = call.AuthorizePayload(
#     #         id_token={'idToken':'AA12345',
#     #                 'type': 'ISO14443'})
#     #     response = await self.call(request)
#     #     print(response)


#     async def authentication(self):
#         request = call.AuthorizePayload()
#         response = await self.call(request)
#         print(response)


# async def main():
#    async with websockets.connect(
#        'ws://localhost:9000/CP_1',
#         subprotocols=['ocpp2.0.1']
#    ) as ws:

#        cp = ChargePoint('CP_1', ws)

#        await asyncio.gather(cp.start(), cp.send_boot_notification())


# if __name__ == '__main__':
#    asyncio.run(main())

import asyncio
import logging
import websockets

from ocpp.v201 import call
from ocpp.v201 import ChargePoint as cp

logging.basicConfig(level=logging.INFO)


class ChargePoint(cp):

    async def send_boot_notification(self):
       request = call.BootNotificationPayload(
               charging_station={
                   'model': 'Wallbox XYZ',
                   'vendor_name': 'anewone'
               },
               reason="PowerUp"
       )
       response = await self.call(request)

       if response.status == 'Accepted':
           print("Connected to central system.")
    
    async def authentication(self):
        #Set type=ISO14443 for the authentication via RFID
        request = call.AuthorizePayload(
            id_token={'id_token':'AA12345',
                    'type': 'ISO14443'})
        response = await self.call(request)
        print("Status of the authetication: {}".format(response.id_token_info['status']))
        



async def main():
   async with websockets.connect(
       'ws://localhost:9000/CP_1',
        subprotocols=['ocpp2.0.1']
   ) as ws:

       cp = ChargePoint('CP_1', ws)

       await asyncio.gather(cp.start(), cp.authentication())


if __name__ == '__main__':
   asyncio.run(main())
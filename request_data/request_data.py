import asyncio, aiohttp
import os
from dotenv import load_dotenv
load_dotenv()
"""
    *Request Data Template*

    In this template you can see how to make a request to the API.
    You can change the request parameters, headers, etc.
    You can also add more configuration if it's needed.
    You can also add more functions to make the request.
    We usually use GET, since we are getting the data

    Author:
     Github: @ElStevenn
     Email: paumat17@gmail.com
     Webpage: paumateu.com

"""

URL_BASE = "" # Type here url base

# Uncoment this if it's needed
class ApiError(Exception):
    """Errors exceptions handle"""
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(f"API Error {status_code}: {message}")


class API_connection(ApiError):
    """
     Main API Connection class
    """

    def __init__(self, apiKey=None):
        self.api_response = None
        self._basePath = None
        self._baseURL = URL_BASE
        self._apiKey = apiKey

        """Add here more configuration if it's needed"""
        # self._acceptLanguage = 'es-ES'
        # self._publicKey = publicKey
        # self._privateKey = privateKey

    async def curl_exec(self, data, headers, method="get"):
        """Make the request"""
        url = str(self._baseURL) + str(self._basePath)
        async with aiohttp.ClientSession() as session:
            if method == "get":
                async with session.get(url, params=data, headers=headers) as response:
                    if response.status == 200:
                        print("Request was successful.")
                        return await response.json()
                    else:
                        raise ApiError(response.status, await response.text())
            elif method == "post":
                async with session.post(url, data=data, headers=headers) as response:
                    if response.status == 200:
                        print("Request was successful.")
                        return await response.json()
                    else:
                        raise ApiError(response.status, await response.text())
            elif method == "put":
                async with session.put(url, data=data, headers=headers) as response:
                    if response.status == 200:
                        print("Request was successful.")
                        return await response.json()
                    else:
                        raise ApiError(response.status, await response.text())
            elif method == "delete":
                async with session.delete(url, data=data, headers=headers) as response:
                    if response.status == 200:
                        print("Request was successful.")
                        return await response.json()
                    else:
                        raise ApiError(response.status, await response.text())
            elif method == "patch":
                async with session.patch(url, data=data, headers=headers) as response:
                    if response.status == 200:
                        print("Request was successful.")
                        return await response.json()
                    else:
                        raise ApiError(response.status, await response.text())
                    

    async def make_request(self, data, method="get") -> dict:
        if self._apiKey is None:
            raise ValueError(400, "API Key is required.")
        
        """Uncoment this if is needed"""
        # if self._publicKey is None:
        #     raise ValueError(400, "API Key is required.")

        """Change the headers if is needed, read the API docs, here is where the API-Key / OAUTH goes"""
        headers = {
            'api-key': self._apiKey,  # Change 'api-key' depending on the API you use
            'Accept': 'application/json'
            # 'Accept-Language': self._acceptLanguage,
        }

        return await self.curl_exec(data, headers, method)


    ## EXAMPLE REQUESTS ## 
    async def request_get_example1(self, **kwargs):
        """Basic request"""
        self._basePath = "example" # Type here the endpint you want to use
        data = kwargs
        return await self.make_request(data)
    

    async def request_get_example2(self, basePath, **kwargs):
        """Example definining the Path in the parametters"""
        self._basePath = basePath
        data = kwargs
        return await self.make_request(data)
    
    async def post_request_example(self, **kwards):
        """Simple path example"""
        self._basePath = "example"
        data = kwards
        return await self.make_request(data, "post") # Chgane the HTTP method if it's needed

    async def byID_request_example(self, id, **kwargs):
        """Request sorting an ID and sending needed data"""
        self._basePath = f"example/{id}"
        data = kwargs
        return await self.make_request(data)




async def main_proofs():
        # Make proofs here
    API_X_Connextion = API_connection(apiKey=os.getenv('API_KEY_REQUEST'))

    """Example resppmses"""
    # Get example 
    example1 = await API_X_Connextion.request_get_example1()
    example1_parametters = await API_X_Connextion.request_get_example1(limit=10, offset=0)
    example2 = await API_X_Connextion.request_get_example2("example/123", limt=10, offset=0)

    # Post and other method examples
    example3 = await API_X_Connextion.post_request_example(id="123", name="Jeb Jeins")
    example4 = await API_X_Connextion.byID_request_example(id="123", name="Jeb", surname="Jeins")

    # print(example1)

if __name__ == "__main__":
    asyncio.run(main_proofs())

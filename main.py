import aiohttp


class DadataRequest:

    def __init__(self, token, secretkey, baseurl, url_coordinates, lang):
        self.token = token
        self.baseurl = baseurl
        self.secretkey = secretkey
        self.coordinates_url = url_coordinates
        self.lang = lang

    async def get_suggestions(self, suggest):
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Token " + self.token,
        }
        list_suggestions = []
        body = {"query": suggest,
                "language": self.lang}
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(self.baseurl, json=body) as response:
                response_json = await response.json()
                for result in response_json['suggestions']:
                    list_suggestions.append(result['value'])
                return list_suggestions

    async def get_coordinates(self, address):
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Token " + self.token,
            "X-Secret": self.secretkey,
        }
        body = [address]
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(self.coordinates_url, json=body) as response:
                response_json = await response.json()
                return {response_json[0]['geo_lat']}, {response_json[0]['geo_lon']}

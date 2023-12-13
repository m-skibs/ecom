import asyncio
import aiohttp

async def fetch_data(url, id_value, retries=5):
    full_url = f"{url}/{id_value}"
    for attempt in range(retries):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(full_url) as response:
                    if 200 <= response.status < 300:
                        return await response.json()
                    else:
                        print(f"Request failed with status code {response.status}")
        except aiohttp.ClientError as e:
            print(f"Error during request: {e}")
        
        await asyncio.sleep(3 ** attempt)

    print(f"Failed after {retries} retries")
    return "fetch data failed"
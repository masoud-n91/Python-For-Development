import requests
import os
import json
import asyncio
import aiohttp


os.environ["API_KEY"] = "6e61766964692e6d2e393140676d61696c2e636f6d"


async def rhyme_finder(word: str):    
    API_KEY = os.getenv("API_KEY")
    url = f"https://rhyming.ir/api/rhyme-finder?api={API_KEY}&w={word}&sb=1&mfe=2&eq=1"
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                data = await response.text()
                return json.loads(data)
        except aiohttp.ClientError as e:
            print(f"An error occurred: {e}")
            return None


def get_states():
    url = "https://iran-locations-api.vercel.app/api/v1/fa/states"
    response = requests.request("GET", url)
    return json.loads(response.text)


def get_cities(state_id: int):
    url = f"https://iran-locations-api.vercel.app/api/v1/fa/cities?state_id={state_id}"
    response = requests.request("GET", url)
    return json.loads(response.text)


async def get_coordinates(state_name: str, city_name: str):
    states_list = get_states()
    
    for state in states_list:
        if state["name"] == state_name:
            state_id = state["id"]
            break
    
    cities_dict = get_cities(state_id)

    for city in cities_dict["cities"]:
        if city["name"] == city_name:
            city_latitude = city["latitude"]
            city_longitude = city["longitude"]
            break

    return {"latitude": city_latitude, "longitude": city_longitude}


async def main():
    state_name = input("Enter state name: ")
    city_name = input("Enter city name: ")
    rhym = input("Enter word: ")
    results = await asyncio.gather(get_coordinates(state_name, city_name), rhyme_finder(rhym))
    print(results)



if __name__ == "__main__":
    asyncio.run(main())
    
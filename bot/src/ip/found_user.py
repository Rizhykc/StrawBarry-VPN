import time

import aiohttp
import requests


async def get_ip_users() -> dict:
    url = 'http://ipinfo.io/json'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            ip_data = await response.json()
            return ip_data


def found_info_by_ip(ip='127.0.0.1'):
    try:
        unique_param = int(time.time())
        response = requests.get(url=f'http://ip-api.com/json/{ip}'
                                f'?unique={unique_param}').json()
        data = {
            '[IP]': response.get('query'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[Int prov]': response.get('isp'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }
        result = []
        for k, v in data.items():
            result.append(f'{k}: {v}')
        return '\n'.join(result)
    except Exception as e:
        return f"Произошла ошибка: {e}"

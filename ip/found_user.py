import requests


def found_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
            '[IP]': response.get('query'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[Int prov]': response.get('isp'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }
        for k, v in data.items():
            print(f'{k} : {v}')
    except requests.exceptions.ConnectionError:
        return '[!] Please check your connection!'


def main():
    ip = input('Plase enter a target IP:')
    found_info_by_ip(ip=ip)


if __name__ == '__main__':
    main()

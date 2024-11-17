# location.py
import requests
def get_location():
    response = requests.get('https://ipinfo.io')
    if response.status_code == 200:
        data = response.json()
        return {
            
            'ip': data.get('ip'),
            'city': data.get('city'),
            'region': data.get('region'),
            'country': data.get('country'),
            'loc': data.get('loc')
        }
        
    else:
        return {'error': 'Unable to get location'}

if __name__ == "__main__":
    location = get_location()
    print(location)

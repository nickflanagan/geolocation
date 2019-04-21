import platform
import subprocess
import requests

api_url = "https://www.googleapis.com/geolocation/v1/geolocate?key="
api_url2 = "https://maps.googleapis.com/maps/api/geocode/json?latlng="


def get_address(lat, lng):
    key = get_key()
    address = "Not Found"
    url_request = f"{api_url2}{lat},{lng}&key={key}"
    try:
        response = requests.get(url_request)
        data = response.json()
        if 'error' in data.keys():
            raise requests.RequestException('Error {0}: {1}'.format(data['error']['code'], data['error']['message']))
    except Exception as e:
        print(e)
    else:
        address = data['results'][1]['formatted_address']
    return address


def return_coordinates():
    # returns [latitude, longitude, accuracy]
    wifi_info = get_wifi_info()
    json_file = build_json(wifi_info)
    key = get_key()
    try:
        response = requests.post(api_url + key, json=json_file)
        data = response.json()
        if 'error' in data.keys():
            raise requests.RequestException('Error {0}: {1}'.format(data['error']['code'], data['error']['message']))
    except Exception as e:
        print(e)
    else:
        lat = data['location']['lat']
        lng = data['location']['lng']
        accuracy = data['accuracy']

        return [lat, lng, accuracy]


def build_json(wifi_list):
    json_dict = {"condsider Ip": "True"}
    json_dict["wifiAccessPoints"] = wifi_list
    return json_dict


def get_wifi_info():
    wifi_list = []
    sys_type = system_info()
    if 'windows' in sys_type:
        # TODO Implement windows subprocess
        # out = subprocess.check_output('netsh wlan show networks mode=bssid').decode(encoding='utf_8')
        pass
    elif 'Darwin' in sys_type:
        out = subprocess.check_output(['/usr/local/bin/airport', '--scan']).decode(encoding='utf_8')
        wifi_list = []
        results_array = out.split('\n')
        header = results_array.pop(0)
        bssid_index = header.find('BSSID')
        rssi_index = header.find('RSSI')
        channel_index = header.find('CHANNEL')
        for line in results_array:
            if len(line) < bssid_index:
                continue
            wifi_list.append({'macAddress': line[bssid_index:bssid_index + 17],
                              'signalStrength': line[rssi_index:rssi_index + 3],
                              'channel': line[channel_index:channel_index + 2].strip()})
        for item in wifi_list:
            print(item)

    else:
        # TODO: Implement linux subprocess
        pass
    return wifi_list


def get_key():
    fp = open('googleMapsAPI_Key.txt') # create your version of this file with your key
    key = fp.readline().strip()
    fp.close()

    return key


def system_info():
    return platform.system()

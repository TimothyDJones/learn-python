import json
import pprint
import requests

pp = pprint.PrettyPrinter(indent=4)

def get_ipaddr():
    url = "https://lumtest.com/myip.json"
    res = requests.get(url)
    print(res)
    pp.pprint(res.json())
    res_json = res.json()
    print("IP Address: {}".format(res_json['ip']))
    print("City: {}\tPostal Code: {}".format(res_json['geo']['city'], res_json['geo']['postal_code']))

if __name__ == "__main__":
    get_ipaddr()

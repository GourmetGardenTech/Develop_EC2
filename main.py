import requests
import json
import requests
import psycopg2



conn = psycopg2.connect(
host="34.93.233.174",
database="postgres",
user="postgres",
password="Crmpostgres123")
# create a cursor

cur = conn.cursor()
cur.execute("select count(*) from inventory WHERE sku LIKE 'BLR%'")
data = cur.fetchall()
banglore = data[0][0]

cur1 = conn.cursor()
cur1.execute("select count(*) from inventory WHERE sku LIKE 'MUM%'")
data1 = cur1.fetchall()
mumbai = data1[0][0]


cur2 = conn.cursor()
cur2.execute("select count(*) from inventory WHERE sku LIKE 'HYD%'")
data2 = cur2.fetchall()
hyderabad = data2[0][0]

cur3 = conn.cursor()
cur3.execute("select count(*) from inventory WHERE sku LIKE 'CHN%'")
data3 = cur3.fetchall()
chennai = data3[0][0]

url = "https://app.yellowmessenger.com/api/engagements/notifications/v2/push?bot=x1635730302198"

payload = json.dumps({
  "userDetails": {
    "number": "917888734634"
  },
  "notification": {
    "type": "whatsapp",
    "sender": "919108114321",
    "templateId": "customer_update7",
    "language": "en",
    "params": {
      "1": "Gourmet Garden Inventory",
      "2": "There are "+ str(hyderabad) +" products in Hyderabad on store which are out of stock right now",
      "3": "Please dowload the latest product list from below link",
      "4": "https://skfb5vyli4.execute-api.ap-southeast-1.amazonaws.com/",
      "media": {
        "mediaLink": "https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_170,w_170,f_auto,b_white,q_auto:eco,dpr_1/nxuixfnicug9coi02enx"
      }
    }
  }
})
headers = {
  'x-auth-token': '609fee68f1354c6e9149c42ac08024d18dc966f1ae4a14f60553e0b5be08cddd',
  'Content-Type': 'application/json',
  'Cookie': 'ym_xid=609fee68f1354c6e9149c42ac08024d18dc966f1ae4a14f60553e0b5be08cddd'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

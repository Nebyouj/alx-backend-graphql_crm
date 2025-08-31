#!/usr/bin/env python3
import requests, datetime

query = """
query RecentOrders {
  orders(orderDate_Gte: "%s") {
    id
    customer {
      email
    }
  }
}
""" % ( (datetime.datetime.now() - datetime.timedelta(days=7)).date() )

resp = requests.post(
    "http://localhost:8000/graphql",
    json={"query": query}
)

orders = resp.json().get("data", {}).get("orders", [])

with open("/tmp/order_reminders_log.txt", "a") as f:
    for o in orders:
        f.write(f"{datetime.datetime.now()} - Order {o['id']} for {o['customer']['email']}\n")

print("Order reminders processed!")
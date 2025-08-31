import datetime, requests

def log_crm_heartbeat():
    now = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(f"{now} CRM is alive\n")



def update_low_stock():
    mutation = """
    mutation {
      updateLowStockProducts {
        success
        updatedProducts {
          name
          stock
        }
      }
    }
    """
    resp = requests.post("http://localhost:8000/graphql", json={"query": mutation})
    data = resp.json()["data"]["updateLowStockProducts"]

    with open("/tmp/low_stock_updates_log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {data['success']}\n")
        for p in data["updatedProducts"]:
            f.write(f"Product {p['name']} new stock: {p['stock']}\n")

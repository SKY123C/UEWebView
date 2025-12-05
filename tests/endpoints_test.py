import requests
import  threading
import asyncio


async def test_get_selected_assets():

    response = requests.get("http://127.0.0.1:8050/api/v1/scripts/get_selected_assets")

    print(response.content)

# thread = threading.Thread(target=test_get_selected_assets)
# thread.daemon = True
# thread.start()

asyncio.run(test_get_selected_assets())
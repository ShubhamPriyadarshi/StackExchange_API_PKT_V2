import httpx
import aiometer
import csv
from app.core.config import key
import datetime
import functools

class StackExchangeService:
    @staticmethod
    async def scrape(page_no):
        url = f"https://api.stackexchange.com/2.3/tags?page={page_no}&order=desc&sort=popular&site=stackoverflow"
        try:
            with open('token.txt', 'r', encoding='utf-8') as file:
                access_token = file.read()
        except FileNotFoundError:
            print("Error: access token not found.")
            return

        headers = {"Authorization": f"Bearer {access_token}"}
        url += f"&access_token={access_token}&key={key}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
        try:
            data = response.json()
        except Exception as e:
            print(f"JSON data error {e} page no {page_no}")
            print(response)
            return {}

        if "items" not in data:
            print(f"Error: Response data does not contain 'items' key.{response.text}")

            return {}

        csv_file = 'data.csv'

        with open(csv_file, 'a', newline='') as file:
            tags = data["items"]

            for tag in tags:
                fieldnames = ['name', 'count', 'ingestion_timestamp']
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                writer.writerow({
                    'name': tag['name'],
                    'count': tag['count'],
                    'ingestion_timestamp': datetime.datetime.now()
                })

        return data

    @staticmethod
    async def scrape_all():
        has_more = True
        page_numbers = list(range(0, 3))

        while has_more:
            async_fns = [functools.partial(StackExchangeService.scrape, page_number) for page_number in page_numbers]
            responses = await aiometer.run_all(async_fns,max_per_second=3)
            print(responses)
            for response in responses:
                print(response)
                if response and response.get('has_more')== False:
                    has_more = False
                    print('no more pages found, terminating')
                    break

            page_numbers = [i for i in range(page_numbers[-1] + 1, page_numbers[-1] + 3)]



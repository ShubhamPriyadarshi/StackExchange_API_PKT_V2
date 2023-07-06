import asyncio
import os
from app.services.stackexchange_service import StackExchangeService
from app.services.snowflake_service import SnowflakeService

class DataLoader:
    @staticmethod
    async def load_data():

        await StackExchangeService.scrape_all()

        SnowflakeService.insert_data_from_csv('data.csv')

        if os.path.exists('data.csv'):
            os.remove('data.csv')
            print("The file 'data.csv' has been deleted.")
        else:
            print("The file 'data.csv' does not exist.")

if __name__ == "__main__":
    asyncio.run(DataLoader.load_data())

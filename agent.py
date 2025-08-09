import asyncio
from app import BrowserController

async def main():
    browser_controller = BrowserController()
    await browser_controller.start_browser()
    await browser_controller.navigate("https://www.google.com")
    # Add agent logic here
    while True:
        await asyncio.sleep(1)

if __name__ == '__main__':
    asyncio.run(main())

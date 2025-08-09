import asyncio
import logging
from playwright.async_api import async_playwright

class BrowserController:
    def __init__(self):
        self.page = None
        self.context = None
        self.browser = None
        self.p = None

    async def start_browser(self):
        self.p = await async_playwright().start()
        self.browser = await self.p.chromium.launch(
            headless=True,
            args=[
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-dev-shm-usage'
            ]
        )
        self.context = await self.browser.new_context()
        self.page = await self.context.new_page()

    async def close_browser(self):
        await self.browser.close()
        await self.p.stop()

    async def navigate(self, url):
        try:
            await self.page.goto(url, wait_until='networkidle')
            return True
        except Exception as e:
            logging.error(f"Navigation error: {str(e)}")
            return False

    async def get_content(self):
        return await self.page.content()
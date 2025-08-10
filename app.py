import asyncio
import logging
import yaml
from playwright.async_api import async_playwright

class BrowserController:
    def __init__(self, config_path='config.yml'):
        self.page = None
        self.context = None
        self.browser = None
        self.p = None
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)

    async def start_browser(self):
        browser_cfg = self.config.get('browser', {})
        remote_debugging = browser_cfg.get('remote_debugging', {})

        args = [
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-dev-shm-usage'
        ]

        if remote_debugging.get('enabled'):
            args.append(f"--remote-debugging-port={remote_debugging.get('port', 9222)}")
            args.append(f"--remote-debugging-address={remote_debugging.get('address', '0.0.0.0')}")

        self.p = await async_playwright().start()
        self.browser = await self.p.chromium.launch(
            headless=True,
            args=args
        )

        context_args = {
            'viewport': browser_cfg.get('viewport'),
            'user_agent': browser_cfg.get('user_agent'),
            'locale': browser_cfg.get('locale'),
            'timezone_id': browser_cfg.get('timezone'),
        }
        # Filter out None values
        context_args = {k: v for k, v in context_args.items() if v is not None}

        self.context = await self.browser.new_context(**context_args)
        self.page = await self.context.new_page()

    async def close_browser(self):
        try:
            if self.page:
                await self.page.close()
            if self.context:
                await self.context.close()
            if self.browser:
                await self.browser.close()
        finally:
            if self.p:
                await self.p.stop()

    async def navigate(self, url):
        try:
            if not self.page:
                raise RuntimeError("Browser not initialized. Call start_browser() first.")
            await self.page.goto(url, wait_until='networkidle')
            return True
        except Exception as e:
            logging.error(f"Navigation error: {str(e)}")
            return False

    async def get_content(self):
        if not self.page:
            raise RuntimeError("Browser not initialized. Call start_browser() first.")
        return await self.page.content()

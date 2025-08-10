import asyncio
import logging
import signal
from app import BrowserController

async def main():
    logging.basicConfig(level=logging.INFO)
    browser_controller = BrowserController()
    stop = asyncio.Event()
    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, stop.set)
    try:
        await browser_controller.start_browser()
        ok = await browser_controller.navigate("https://www.google.com")
        if not ok:
            logging.error("Initial navigation failed")
        # Add agent logic here
        await stop.wait()
    except Exception:
        logging.exception("Agent crashed")
    finally:
        try:
            await browser_controller.close_browser()
        except Exception:
            logging.exception("Error while closing browser")

if __name__ == '__main__':
    asyncio.run(main())

import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def repel_followers(api):
    for unblocked in tweepy.Cursor(api.followers).items():
        logger.info(f"Blocked {unblocked.name}")
        api.create_block(unblocked.screen_name)

def main():
    api = create_api()
    while True:
        repel_followers(api)
        for blocked in tweepy.Cursor(api.blocks).items():
            logger.info(f"Released {blocked.name}")
            api.destroy_block(blocked.screen_name)
        time.sleep(60)

if __name__ == "__main__":
    main()

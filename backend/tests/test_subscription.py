import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.subscription_service import SubscriptionService

def test_unlock_premium():
    assert SubscriptionService.unlock_premium("123456") == True
    assert SubscriptionService.unlock_premium("wrong") == False

if __name__ == "__main__":
    test_unlock_premium()
    print("Subscription logic tests passed!")

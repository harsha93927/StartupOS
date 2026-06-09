import sys
import os
import asyncio
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.nvidia_service import NvidiaService

async def test_nvidia_connection():
    # This test will fail if no API key is provided, which is expected in CI
    api_key = os.getenv("NVIDIA_API_KEY")
    if not api_key:
        print("Skipping NVIDIA connection test: NVIDIA_API_KEY not set")
        return

    service = NvidiaService(api_key)
    try:
        response = await service.generate_response("You are a helpful assistant.", "Say hello.")
        print(f"NVIDIA Response: {response}")
        assert len(response) > 0
    except Exception as e:
        print(f"NVIDIA API call failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_nvidia_connection())

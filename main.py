import asyncio

"""Case senario 1"""

async def fetch_any_tasks():
    """Get the data from the API"""
    pass

async def push_data_task(task):
    """Push the data to the API"""
    pass

async def sync_tasks():
    tasks = await fetch_any_tasks()
    results = []
    for task in tasks:
        if 'trigger' in task['content']:  # Define your trigger condition
            result = await push_data_task(task)
            results.append(result)
    return results


def main():
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(sync_tasks())
    print(results)

if __name__ == "__main__":
    print("Async ta")
    # main()

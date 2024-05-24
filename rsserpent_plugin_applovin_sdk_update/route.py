from typing import Any, Dict

import arrow
from rsserpent_rev.utils import HTTPClient, cached


path = "/applovin/sdk-update/{platform}"


@cached
async def provider(platform: str) -> Dict[str, Any]:
    """Return the latest changelog of AppLovin Max SDK for the specified platform.

    Args:
        platform (str): The platform of the SDK. \
        Supported values are: ios, android, unity, react-native, flutter, godot.

    Raises:
        ValueError: If the platform is not supported.

    Returns:
        Dict[str, Any]: The latest changelog of AppLovin Max SDK for \
         the specified platform.
    """
    map_dict = {
        "ios": "iOS",
        "android": "Android",
        "unity": "Unity",
        "react-native": "React Native",
        "flutter": "Flutter",
        "godot": "Godot",
    }
    if platform.lower() not in map_dict:
        raise ValueError(f"Unsupported platform: {platform}")

    platform = platform.lower()

    async with HTTPClient() as client:
        platform_in_url = platform.replace("-", "_")
        url = f"https://docs.applovin.com/max/api/1.0/changelog/{platform_in_url}"
        user_info = (await client.get(url)).json()

    items = [
        {
            "title": f"AppLovin Max {map_dict[platform]} SDK {item['version']} 更新",
            "description": item["content"],
            "link": url,
            "pub_date": arrow.get(item["published_at"], "MMMM D, YYYY"),
        }
        for item in user_info
    ]
    latest_date = arrow.get(user_info[0]["published_at"], "MMMM D, YYYY").format(
        "YYYY-MM-DD"
    )
    return {
        "title": f"AppLovin Max {map_dict[platform.lower()]} SDK 更新日志",
        "link": url,
        "description": f"最新更新日期：{latest_date}",
        "pub_date": items[0]["pub_date"],
        "items": items,
    }

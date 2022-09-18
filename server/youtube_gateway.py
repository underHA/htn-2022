from pyyoutube import Api

api = Api(api_key="AIzaSyBWqyeG-xeM6i2g3JVgsMerpcQzs24-ezc")


async def find_video(word: str):
    r = api.search(
        q=word + " music instrumental",
        parts=["snippet"],
        count=1,
        safe_search="moderate",
        search_type="video",
        video_category_id="10"
    )
    return "https://youtu.be/" + r.items[0].id.videoId

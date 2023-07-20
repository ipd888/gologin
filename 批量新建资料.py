from gologin import GoLogin
import concurrent.futures

gl = GoLogin({
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NGI1MjkzNDBjNGE0OWQ4NmRkNWZjYTciLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NGI1MmM4Mzc0ZjUyNDc3YTJkZGY5ZjgifQ.AqUkAwhhEuSTryypsG_i7PChKaBghWyL2oOnilQCwoU",
})

def create_profile(index):
    profile_id = gl.create({
        "name": f"配置_{index+1}",
        "os": 'mac',
        "navigator": {
            "language": 'en-US',
            "userAgent": 'random',
            "resolution": '1024x768',
            "platform": 'mac',
        },
        'proxy': {
            'mode': 'none',
        },
        "webRTC": {
            "mode": "alerted",
            "enabled": True,
        },
    })

    profile = gl.getProfile(profile_id)
    return profile_id, profile.get("name")

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(create_profile, i) for i in range(10)]
    for future in concurrent.futures.as_completed(futures):
        profile_id, profile_name = future.result()
        print(f'Profile ID: {profile_id} - 新配置文件名称:', profile_name)

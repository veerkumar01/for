import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN","" )
    API_ID = int(os.environ.get("API_ID", "31685568"))
    API_HASH = os.environ.get("API_HASH", "436f53caee1dcae5eefcdf373716fccb")
    AUTH_USER = os.environ.get('AUTH_USERS', '2083529027, 2083529027').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "〖ᴷⁱⁿᴳ Ⱥʂʂìցղҽɾ 🔰❌️🔰♡▪︎•Å𝑁𝐈𐌑À𝐿•▪︎♡ ⱽᵉʳⁱᶠⁱᵉᵈ"#Here You Can Change with Your Name  or any custom name or title you prefer

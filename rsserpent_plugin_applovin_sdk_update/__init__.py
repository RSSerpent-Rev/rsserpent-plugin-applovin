from rsserpent_rev.models import Persona, Plugin

from . import route

plugin = Plugin(
    name="rsserpent-plugin-applovin-sdk-update",
    author=Persona(
        name="EkkoG",
        link="https://github.com/EkkoG",
        email="beijiu572@gmail.com",
    ),
    prefix="/applovin/sdk-update",
    repository="https://github.com/RSSerpent-Rev/rsserpent-plugin-applovin",
    routers={route.path: route.provider},
)

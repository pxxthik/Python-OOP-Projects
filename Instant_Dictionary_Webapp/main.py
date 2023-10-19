import justpy as jp

from webapp import home, about

jp.Route(home.Home.path, home.Home.serve)
jp.Route(about.About.path, about.About.serve)
jp.justpy(port=8001)

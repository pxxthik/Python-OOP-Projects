import justpy as jp

from webapp.home import Home
from webapp.about import About
from webapp.dictionary import Dictionary

jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)
jp.Route(Dictionary.path, Dictionary.serve)

jp.justpy(port=8001)

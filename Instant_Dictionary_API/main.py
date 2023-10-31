import api
import documentation

import justpy as jp

jp.Route("/api", api.Api.serve)
jp.Route("/", documentation.Doc.serve)
jp.justpy()

import justpy as jp


class Api:
    """Handle requests at /api?w=word
    """

    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')
        jp.Div(a=wp, text=word.title())
        return wp


jp.Route("/api", Api.serve)
jp.justpy()

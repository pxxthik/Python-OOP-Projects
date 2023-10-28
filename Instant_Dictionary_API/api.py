import justpy as jp
import definition


class Api:
    """Handle requests at /api?w=word
    """

    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')

        defined = definition.Definition(word).get()

        wp.html = defined
        return wp


jp.Route("/api", Api.serve)
jp.justpy()

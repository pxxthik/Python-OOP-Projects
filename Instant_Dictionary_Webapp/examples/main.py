import justpy as jp


@jp.SetRoute("/")
def home():
    wp = jp.WebPage()
    jp.Div(a=wp, text="Hello world!")
    jp.Div(a=wp, text="Hello again")
    return wp


@jp.SetRoute("/about")
def about():
    wp = jp.WebPage()
    jp.Div(a=wp, text="Hi world!")
    jp.Div(a=wp, text="Hi again")
    return wp


# jp.Route("/", home)

jp.justpy()

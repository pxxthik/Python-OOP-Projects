import justpy as jp


class Dictionary:
    path = "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Instant English Dictionary!", classes="text-4xl m-2")
        jp.Div(a=div, text="Get the definition of any English word instantly as you type.",
               classes="text-lg")

        input_div = jp.Div(a=div, classes="grid grid-cols-2")
        jp.Input(a=input_div, placeholder="Type in a word here...",
                 classes="m-2 bg-gray-100 border-2 border-gray-200 rounded w-64 "
                         "focus:bg-white focus:outline-none focus:border-purple-500 py-2 px-4")

        output_div = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40")

        jp.Button(a=input_div, text="Get Definition",
                  classes="border-2 text-gray-500", click=cls.get_definition,
                  output_div=output_div)


        return wp

    @staticmethod
    def get_definition(widget, msg):
        widget.output_div.text = "Something was displayed"


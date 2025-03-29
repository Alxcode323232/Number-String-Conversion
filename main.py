from nicegui import html, ui
import StringNumberConversion

# Centering the title using a row with justify='center'
with ui.row().style('width: 100%; justify-content: center; font-size: 220%'):
    html.label('Number-Word Converter')

class Demo:
    def __init__(self):
        self.number = 1

demo = Demo()
v = ui.radio({'Numbers to Words': 'Numbers to Words', 'Words to Numbers': 'Words to Numbers'}) \
    .bind_value(demo, 'mode')


ui.run()

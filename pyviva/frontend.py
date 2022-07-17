from rich import print
from rich.layout import Layout
from rich.panel import Panel


def layout(): # creating base layout 

    layout=Layout()

    layout.split_column(  # splitting the base widget into two halves
        Layout(Panel('Question Panel', style='blue')),
        Layout(name="lower")
    )

    layout["lower"].split_row( # further splitting
        Layout(Panel('PyViva', style='green'), size=40),
        Layout(name="right"),
    )

    layout['right'].split_column(  # space for winnings 
        Layout(name='top'),
        Layout(name='bottom'),
        Layout(Panel('Winnings', style='red'), size=11)
    )

    layout['top'].split_row( # space for options 
        Panel('Option 1', style='blue', height=4),
        Panel('Option 2', style='yellow', height=4)
    )

    layout['bottom'].split_row(
        Panel('Option 3', style='yellow', height=4),
        Panel('Option 4', style='blue', height=4)
    )
    print(layout)
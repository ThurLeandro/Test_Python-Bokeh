from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, TextInput, Button, DataTable, TableColumn, NumericInput , Div

source = ColumnDataSource(data=dict(firstName=[], secondName=[], age=[]))

title = Div(text="<h1>Painel de Cadastro de Funcionarios</h1>", width=400)

firstName_input = TextInput(value="", title="Nome:")
secondName_input = TextInput(value="", title="Sobrenome:")
age_input = NumericInput(value=0, title="Idade:", low=0, high=120)

def add_data():
    new_data = dict(
        firstName=[firstName_input.value],
        secondName =[secondName_input.value],
        age=[age_input.value]
    )
    source.stream(new_data)
    firstName_input.value = ""
    secondName_input.value = ""
    age_input.value = 0

add_button = Button(label="Adicionar", button_type="success")
add_button.on_click(add_data)

columns = [
    TableColumn(field="firstName", title="Nome"),
    TableColumn(field="secondName", title="Sobrenome"),
    TableColumn(field="age", title="Idade"),
]

data_table = DataTable(source=source, columns=columns, width=400, height=280)

layout = column(title, firstName_input, secondName_input, age_input, add_button, data_table)

curdoc().add_root(layout)

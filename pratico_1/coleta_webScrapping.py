import pandas as pd

url = "https://pt.wikipedia.org/wiki/Estat%C3%ADsticas_da_pandemia_de_COVID-19_no_Brasil"
df = pd.read_html(url, match="Caso")[0]
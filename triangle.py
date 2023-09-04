import chainladder as cl
import pandas as pd

df = pd.read_excel('Sinistros.ods')


triangle = cl.Triangle(df, origin='Sinistro', development='Aviso', columns='Valor', cumulative=False)


triangle = triangle.incr_to_cum()

triangle.grain('OSDS')

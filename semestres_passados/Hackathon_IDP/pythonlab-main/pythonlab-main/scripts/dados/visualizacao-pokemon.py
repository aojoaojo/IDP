#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 11:36:08 2022

@author: cafe
"""

import pandas as pd

arquivo = "pokemon_data.csv"

# Abrir CSV como DataFrame
dados_poke = pd.read_csv(arquivo)

# Tipos de gráficos
# Relacionamentos
# dados_poke.plot.scatter(x="HP", y="Attack", alpha=0.5)
# dados_poke.plot.scatter(x="Defense", y="Attack", alpha=0.5)
# dados_poke.plot.scatter(x="Defense", y="Attack",s="HP", alpha=0.5)
dados_poke.plot.scatter(x="Sp. Atk", y="Sp. Def",s="Defense", alpha=0.5)
# Comparação
# dados_poke['HP'].plot()
# dados_poke['HP'].plot.bar()
# Distribuição
# dados_poke['HP'].plot.hist()
# dados_poke['HP'].plot.box()
# dados_poke['Attack'].plot.box()
# Composição

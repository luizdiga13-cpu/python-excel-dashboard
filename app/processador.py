import pandas as pd
import os
from database import salvar_banco


def processar_arquivo(df):

    df.columns = df.columns.str.strip()

    if "Vendas" not in df.columns:
        raise ValueError(
            "A planilha precisa ter a coluna 'Vendas'"
        )

    ranking = df.sort_values(
        by="Vendas",
        ascending=False
    )

    salvar_banco(ranking)

    # 🔥 ADICIONE AQUI (ANTES DE SALVAR O EXCEL)
    os.makedirs("relatorios", exist_ok=True)

    with pd.ExcelWriter(
        "relatorios/relatorio.xlsx",
        engine="xlsxwriter"
    ) as writer:

        ranking.to_excel(
            writer,
            sheet_name="Ranking",
            index=False
        )
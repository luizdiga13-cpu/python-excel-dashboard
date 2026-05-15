from sqlalchemy import create_engine
import os


# Caminho absoluto do banco
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

db_path = os.path.join(
    BASE_DIR,
    "database",
    "vendas.db"
)

# Criar engine SQLite
engine = create_engine(
    f"sqlite:///{db_path}"
)


def salvar_banco(df):

    df.to_sql(
        "vendas",
        engine,
        if_exists="replace",
        index=False
    )
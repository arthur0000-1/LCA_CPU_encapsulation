import polars as pl
import datetime

df = pl.read_excel("../../../../../../../Documents/Resilio/new/resilio-db/python/database/data/metaboli_gpu_2025-01-23_as_resilio.xlsx", read_csv_options=dict(dtypes={"Memory (Mb)": float}))

df = df.sort("Release Year", descending=False).unique(["Model name"], keep="first", maintain_order=True)

df = df.with_columns(pl.lit(datetime.datetime.now().strftime('%Y-%m-%d')).alias('Last updated'))

df.write_excel("data/GPU_database2025.xlsx")

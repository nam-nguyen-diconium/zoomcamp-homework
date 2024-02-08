from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
import os
import pyarrow as pa
import pyarrow.parquet as pq

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/src/fabled-archive-412122-ea6c741d3f5c.json"

    bucket = 'mage_demo'

    file_path = "green_taxi_2020"

    gcfs = pa.fs.GcsFileSystem()
    
    table = pa.Table.from_pandas(df)

    pq.write_to_dataset(table=table, root_path=f"{bucket}/{file_path}", filesystem=gcfs, partition_cols=["lpep_pickup_date"])

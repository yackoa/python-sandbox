import boto3
s3 = boto3.resource('s3', endpoint_url='http://localhost:4567',
                    aws_access_key_id='123', aws_secret_access_key='abc')
#s3.create_bucket(Bucket='my_bucket')
#for bucket in s3.buckets.all():
#    print(bucket.name)

import s3fs
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

dummyfile= "/home/stormfield/scratch/pyarrow_test/dummy.csv"
output = "/home/stormfield/scratch/pyarrow_test/"
in_df = pd.read_csv(dummyfile)
print(in_df)
print("-----------------")
#in_df.to_parquet(output)

#df = pd.read_parquet(output, engine='pyarrow')

#print(df)

df = pd.DataFrame(in_df)
table = pa.Table.from_pandas(df)
output_path = "/home/stormfield/scratch/pyarrow_test/root/"
"""pq.write_to_dataset(
    table,
    root_path=output_path,
    partition_cols=['A']
)"""

#
s3 = boto3.resource('s3', endpoint_url='http://localhost:4567',
                    aws_access_key_id='123', aws_secret_access_key='abc')
my_bucket = s3.Bucket('my_bucket')

print("contents")
for object in my_bucket.objects.all():
    print(object.all())



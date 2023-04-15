import boto3, os, glob
# upload multiple file to a s3 bucket

cwd = os.getcwd()
cwd = cwd + "/s3files/"
files = glob.glob(cwd + "*Python.txt")
for file in files:
    s3_resource = boto3.client("s3")
    s3_resource.upload_file(
        Filename=file, # files are not string.
        Bucket="mybucket04142023-v1", 
        Key=(file.split("/")[-1]).split("_")[0] + "_uploaded.txt")

'''
$ python3.7 s3upload_manyobjs.py 
$ 

The S3 bucket already had file4_uploaded.txt
Please note that file4_uploaded.txt was overwritten by executing this script.
See the section, Last Modified in the Objects section in the S3 bucket
'''
def s3(client, infile, bucket, name):
    client.upload_fileobj(infile, bucket, name)
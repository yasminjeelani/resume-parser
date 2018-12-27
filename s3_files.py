import boto3
import os
import sys
import uuid

def get_resumes_s3():
    sample_resumes_bucket_name='sample-resumes'
    s3 = boto3.resource('s3')
    s3_client = boto3.client('s3')
    resumes = []
    sample_resumes_bucket = s3.Bucket(sample_resumes_bucket_name)
    for resume_object in sample_resumes_bucket.objects.all():
        tmp_resume_path = '/tmp/{}{}'.format(uuid.uuid4(), resume_object.key)
        s3_client.download_file(sample_resumes_bucket_name, resume_object.key, tmp_resume_path)
        resumes.append(tmp_resume_path)
    return resumes

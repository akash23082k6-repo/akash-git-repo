import boto3

exception_bucket = []

def get_s3_buckets():
    """
    Function to get all S3 buckets present in the AWS account.
    """
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    buckets =  []
    for bucket in response['Buckets']:
        if bucket['Name'] not in exception_bucket:
            buckets.append(bucket['Name'])
    return buckets

def check_tag_presence(bucket_name, tag_key):
    """
    Function to check if a specific tag key is present for an S3 bucket.
    """
    s3 = boto3.client('s3')
    try:
        response = s3.get_bucket_tagging(Bucket=bucket_name)
        tags = response['TagSet']
        for tag in tags:
            if tag['Key'] == tag_key:
                print(f"Tag {tag_key} is present on the bucket {bucket_name}")
                return True
        return False
    except s3.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchTagSet':
            return False

def add_tag(bucket_name, tag_key, tag_value):
    """
    Function to add a tag to an S3 bucket without removing existing tags.
    """
    s3 = boto3.client('s3')
    try:
        response = s3.get_bucket_tagging(Bucket=bucket_name)
        existing_tags = response['TagSet']
        existing_tags.append({'Key': tag_key, 'Value': tag_value})
        s3.put_bucket_tagging(
            Bucket=bucket_name,
            Tagging={
                'TagSet': existing_tags
            }
        )
    except s3.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchTagSet':
            s3.put_bucket_tagging(
                Bucket=bucket_name,
                Tagging={
                    'TagSet': [
                        {
                            'Key': tag_key,
                            'Value': tag_value
                        }
                    ]
                }
            )
        else:
            raise

def main():
    buckets = get_s3_buckets()
    tag_key = 'Name'
    for bucket in buckets:
        if not check_tag_presence(bucket, tag_key):
            print(f"Tag {tag_key} is not present on the bucket {bucket}")
            add_tag(bucket, 'Name', bucket) 
            print(f"Added tag 'Name' with value '{bucket}' to bucket '{bucket}'.")
        else:
            print(f"Tag {tag_key} is already present on the bucket {bucket}")

if __name__ == "__main__":
    main()

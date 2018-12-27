import json
from s3_files import get_resumes_s3
from main import main
def lambda_handler(event, context):
    resumes = get_resumes_s3()
    main()
    return {
        'statusCode': 200,
        'body': json.dumps(resumes)
    }

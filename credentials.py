def get_mongodb_credentials():
    ssm_client = boto3.client('ssm')
    parameter_name = 'mongodb_access'
    response = ssm_client.get_parameter(Name=parameter_name, WithDecryption=True)
    credentials = response['Parameter']['Value']
    return credentials
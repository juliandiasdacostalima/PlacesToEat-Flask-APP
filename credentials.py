import boto3

def get_mongodb_credentials(parameter_name):
    """
    Retrieve MongoDB credentials from AWS Systems Manager Parameter Store.
    
    Args:
        parameter_name (str): The name of the parameter containing the credentials.
        
    Returns:
        str: MongoDB credentials.
    """
    try:
        # Initialize AWS Systems Manager client
        ssm_client = boto3.client('ssm', region_name='us-east-1')
        
        # Retrieve parameter value with decryption
        response = ssm_client.get_parameter(Name=parameter_name, WithDecryption=True)
        
        # Extract credentials from response
        credentials = response['Parameter']['Value']
        
        return credentials
    except Exception as e:
        # Error handling in case fetching credentials fails
        print("Error fetching MongoDB credentials:", e)
        return None

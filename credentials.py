import boto3
def get_mongodb_credentials(parameter_name):
    try:
        ssm_client = boto3.client('ssm')
        response = ssm_client.get_parameter(Name=parameter_name, WithDecryption=True)
        credentials = response['Parameter']['Value']
        return credentials
    except Exception as e:
        # Manejo de errores en caso de que falle la obtención de las credenciales
        print("Error al obtener las credenciales de MongoDB:", e)
        return None

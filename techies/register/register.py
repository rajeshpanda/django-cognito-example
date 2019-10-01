import boto3
from techiesv1.settings import COGNITO_USER_POOL as UserPoolId

client = boto3.client('cognito-idp')


def createBusinessUser(email, phone):
    response = client.admin_create_user(
        UserPoolId=UserPoolId,
        Username=email,
        UserAttributes=[
            {
                'Name': 'email',
                'Value': 'string'
            },
        ],
        ValidationData=[
            {
                'Name': 'phone_number',
                'Value': 'string'
            },
        ],
        ForceAliasCreation=True | False,
        DesiredDeliveryMediums=[
            'SMS' | 'EMAIL',
        ]
    )

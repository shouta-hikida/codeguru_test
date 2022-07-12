import json
import os
import boto3

def deactivate_access_key(access_key):
    response = access_key.deactivate()
    print(response)
    HTTPStatusCode = response['ResponseMetadata']['HTTPStatusCode']
    print("HTTPStatusCode:")
    print(HTTPStatusCode)
    accessKeyId = access_key.access_key_id
    print(accessKeyId + " is deactivated.")
    return

def main(event, context):
    # 環境変数から取得
    targetAccessKeyUserName = os.environ['TARGET_ACCESS_KEY_USER_NAME']
    # IAMのclientとresource作成
    iamClient = boto3.client('iam')
    iamResource = boto3.resource('iam')
    # IAMユーザーのアクセスキーを取得し無効化
    keys=iamClient.list_access_keys(UserName=targetAccessKeyUserName)
    for key in keys['AccessKeyMetadata']:
        access_key = iamResource.AccessKey(targetAccessKeyUserName, key['AccessKeyId'])
        # アクセスキーの無効化
        deactivate_access_key(access_key)
    return
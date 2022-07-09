from . import routes
from flask import request
import logging

from config.connection import s3_connection
from config.s3Config import BUCKET_NAME

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('Hello')

UPLOAD_FOLDER = '../image'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
s3 = s3_connection()

@routes.route('/image', methods=['post'])
def get_image():

    file = request.files['file']
    print('header:', file.headers, '\n')
    file.name = '학교로고.png'
    print('name:', file.name, '\n')
    print('content-type:', file.content_type, '\n')

    s3.Bucket(BUCKET_NAME).put_object(
        Body=file,
        Key='test/'+file.name,
        ContentType=file.content_type)
    response = 's3://blossom-s3-test/test/학교로고.png'
    return response

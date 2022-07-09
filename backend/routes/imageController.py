from io import BytesIO

from . import routes
from flask import request, make_response, send_file
import logging

from config.connection import s3_connection
from config.s3Config import BUCKET_NAME
from PIL import Image

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('Hello')


def serve_pil_image(pil_img):
    img_io = BytesIO()
    print(pil_img.format)
    pil_img.save(img_io, pil_img.format, quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/'+pil_img.format)


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
s3 = s3_connection()


@routes.route('/image', methods=['post'])
def post_image():
    file = request.files['file']
    print('header:', file.headers, '\n')
    file.name = '학교로고.png'
    print('name:', file.name, '\n')
    print('content-type:', file.content_type, '\n')

    s3.Bucket(BUCKET_NAME).put_object(
        Body=file,
        Key='test/' + file.name,
        ContentType=file.content_type)
    response = 'ok'
    return response


@routes.route('/image', methods=['get'])
def get_image():
    bucket = s3.Bucket(BUCKET_NAME)
    object = bucket.Object('test/newFile.png')
    response = object.get()
    file_stream = response['Body']
    img = Image.open(file_stream)

    return serve_pil_image(img)

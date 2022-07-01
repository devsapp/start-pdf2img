# coding=utf-8

from pdf2image import convert_from_path
import json
import subprocess
import zipfile
import os
import oss2


'''
convert_from_path(pdf_path, dpi=200, output_folder=None, first_page=None, last_page=None, fmt='ppm', jpegopt=None, thread_count=1, userpw=None, use_cropbox=False, strict=False,
                  transparent=False, single_file=False, output_file=str(uuid.uuid4()), poppler_path=None, grayscale=False, size=None, paths_only=False, use_pdftocairo=False, timeout=600)
'''


def make_zip(zipFileName, dirpath):
    with zipfile.ZipFile(zipFileName, 'w', zipfile.ZIP_DEFLATED) as f:
        for path, dirnames, filenames in os.walk(dirpath):
            fpath = path.replace(dirpath, '')
            for filename in filenames:
                f.write(os.path.join(path, filename),
                        os.path.join(fpath, filename))


def handler(event, context):
    evt = json.loads(event)
    creds = context.credentials
    auth = oss2.StsAuth(creds.access_key_id,
                        creds.access_key_secret, creds.security_token)
    bucketName = evt['bucket']
    region = evt.get('region', context.region)
    endpoint = "oss-{}.aliyuncs.com".format(region)
    if region == context.region:  # use internal endpoint
        endpoint = "oss-{}-internal.aliyuncs.com".format(region)

    bucket = oss2.Bucket(auth, endpoint, bucketName)
    object = evt['src_object']
    bucket.get_object_to_file(object, '/tmp/test.pdf')

    subprocess.check_call("mkdir -p /tmp/images", shell=True)

    pdf_name = "/tmp/test.pdf"
    pages = convert_from_path(pdf_name)
    for i, page in enumerate(pages):
        jpg_name = "/tmp/images/test_{}.jpg".format(i)
        page.save(jpg_name, 'JPEG')
    subprocess.check_call("ls -lh /tmp", shell=True)
    subprocess.check_call("rm /tmp/test.pdf", shell=True)
    make_zip("/tmp/test.zip", "/tmp/images")

    subprocess.check_call("ls -lh /tmp/images", shell=True)
    dst_object = evt['dst_object']
    if not dst_object.endswith('.zip'):
        return "dest object name must be zip file, for example: test.zip"

    bucket.put_object_from_file(dst_object, '/tmp/test.zip')

    return 'SUCC'

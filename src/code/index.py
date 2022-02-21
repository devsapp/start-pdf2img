# coding=utf-8

from pdf2image import convert_from_path
import json
import subprocess
import zipfile
import os


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


def handler(environ, start_response):
    # get request_body
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0
    request_body = environ['wsgi.input'].read(request_body_size)

    try:
        subprocess.check_call("rm -rf /tmp/test/images", shell=True)
        subprocess.check_call("rm -rf /tmp/test.zip", shell=True)
    except:
        pass

    evt = json.loads(request_body)
    pdf_url = evt['pdf_url']
    subprocess.check_call(
        "wget -O /tmp/test.pdf {}".format(pdf_url), shell=True)

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

    data = b''
    with open('/tmp/test.zip', 'rb') as f:
        data = f.read()

    status = '200 OK'
    response_headers = [('Content-type', 'application/octet-stream')]
    start_response(status, response_headers)

    return [data]

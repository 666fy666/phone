from aip import AipOcr

config = {
    'appId': '25963617',
    'apiKey': 'FkImi13Uj6Ry0irvgcAhoxq8',
    'secretKey': 'nrowIKYG7RgKHw2N0V06fURyFtFWNvXo'
}

client = AipOcr(**config)


def get_file_content(file):
    with open(file, 'rb') as fp:
        return fp.read()


def img_to_str(image_path):
    image = get_file_content(image_path)
    result = client.basicGeneral(image)
    if 'words_result' in result:
        return '\n'.join([w['words'] for w in result['words_result']])


if __name__ == '__main__':
    imagepath = 'ocr.png'
    res = img_to_str(imagepath)
    print(res)

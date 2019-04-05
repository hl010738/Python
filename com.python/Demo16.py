#实战 抓去图片

import urllib.request
import os

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.3')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html


def get_page(url):

    html = url_open(url).encode('utf-8')
    a = html.find('current-comment-page') + 23
    b = html.find(']', a)

    print(html[a, b])


def find_img(page_url):
    html = url_open(page_url).encode('utf-8')
    img_addr = []
    a = html.find('img src')
    b = html.find('.jpg', a, a + 255)

    while a != -1:
        if b != -1:
            img_addr.append(html[a + 9 : b + 4])
        else:
            b = a + 9

    for i in img_addr:
        print(i)

    return img_addr

def save_img(img_addr):
    for i in img_addr:
        filename = i.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(i)
            f.write(img)


def download_mm(folder = 'ooxx', pages = 10):
    os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx/'
    page_num = int(get_page(url))


    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'
        img_addr = find_img(page_url)
        save_img(img_addr)


if __name__ == '__main__':
    download_mm()



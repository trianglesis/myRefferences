"""
Change Win10 wallpaper to something downloaded.
"""
import sys

import requests
import ctypes
import datetime
import os
import cv2
import glob
from time import time
import logging


place = os.path.normpath('D:/Projects/PycharmProjects/myRefferences/logs/')


def test_logger(name, mode, path=None):
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    if not path:
        path = place
    log_name = os.path.normpath(f"{path}/{name}.log")

    # Extra detailed logging to file:
    f_handler = logging.FileHandler(log_name, mode=mode, encoding='utf-8')

    f_handler.setLevel(logging.DEBUG)
    # Extra detailed logging to console:
    f_format = logging.Formatter(
        '{asctime:<24}'
        '{levelname:<8}'
        '{filename:<20}'
        '{funcName:<22}'
        'L:{lineno:<6}'
        '{message:8s}',
        style='{'
    )

    f_handler.setFormatter(f_format)
    log.addHandler(f_handler)

    return log


log = test_logger(name='himawari', mode='w')


def get_image_himawari_sat(level, offset):
    """
    Y dimention
    4d:
    https://himawari8-dl.nict.go.jp/himawari.asia/img/D531106/4d/550/2020/01/13/002000_0_0.png
    https://himawari8-dl.nict.go.jp/himawari.asia/img/D531106/4d/550/2020/01/13/002000_0_1.png
    https://himawari8-dl.nict.go.jp/himawari.asia/img/D531106/4d/550/2020/01/13/002000_0_2.png
    https://himawari8-dl.nict.go.jp/himawari.asia/img/D531106/4d/550/2020/01/13/002000_0_3.png
    X dimention
    https://himawari8-dl.nict.go.jp/himawari.asia/img/D531106/4d/550/2020/01/13/002000_0_0.png
    https://himawari8-dl.nict.go.jp/himawari.asia/img/D531106/4d/550/2020/01/13/002000_1_0.png
    https://himawari8-dl.nict.go.jp/himawari.asia/img/D531106/4d/550/2020/01/13/002000_2_0.png
    https://himawari8-dl.nict.go.jp/himawari.asia/img/D531106/4d/550/2020/01/13/002000_3_0.png

    Example URL
        https://himawari8-dl.nict.go.jp/himawari.asia/img/D531106/{zoom}/550/{YYYY}/{MM}/{DD}/HHMMSS_X_Y.png

    :return:
    """
    isinstance(level, int), "Level should be an integer: (0-4)"

    base_url = 'https://himawari8-dl.nict.go.jp/himawari8/img'
    infrared = 'INFRARED_FULL'
    rgb = 'D531106'
    width = 550
    level_matrix = (
        ('1d', 1),
        ('4d', 4),
        ('8d', 8),
        ('16d', 16),
        ('20d', 20),
    )
    X = 0
    Y = 0
    today = datetime.datetime.now(tz=datetime.timezone.utc)
    year = today.strftime('%Y')
    month = today.strftime('%m')
    day = today.strftime('%d')
    if offset:
        hour = (today - datetime.timedelta(hours=offset)).strftime('%H')
    else:
        hour = today.strftime('%H')
    minute = (today - datetime.timedelta(minutes=today.minute - 30 % 10)).strftime('%M')
    second = '00'

    # HH - each hour, MM each 10 min, SS - always 00
    img_time = f'{hour}{minute}{second}'
    LEVEL = level_matrix[level]

    # From 1st tile down columns
    img_tiles_m = dict()
    for X in range(LEVEL[1]):
        # X - column
        img_tiles_m.update({X: dict()})
        for Y in range(LEVEL[1]):
            # Y - row
            img_pane = f"_{X}_{Y}.png"
            url = f"{base_url}/{rgb}/{LEVEL[0]}/{width}/{year}/{month}/{day}/{img_time}{img_pane}"
            key = f"{X}_{Y}"
            # img_tiles_m.update({key: dict(url=url, x=X, y=Y, chunk=LEVEL[1])})
            img_tiles_m[X].update({key: dict(url=url)})
    return img_tiles_m


def download(url):
    ts = time()
    try:
        r = requests.get(url)
        if r.status_code == 200:
            log.info(f'Downloaded: {url} {time() - ts}')
            return r
        else:
            log.info(f'Request ended with status code: {r.status_code} {time() - ts}')
    # TODO: Make retry
    except requests.exceptions.ConnectionError as e:
        log.critical(f"<=Download=> ConnectionError: {e}")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        log.critical(f"Request ended with error: {e} {time() - ts}")
        sys.exit(1)


def save(tmp_dir, name, r=None):
    file_name = os.path.normpath(f"{tmp_dir}/{name}.png")
    with open(file_name, 'wb') as f:
        f.write(r.content)
        log.info(f'Saved file: {file_name}')
    return file_name


def download_image_matrix(tile_matrix, tmp_dir):
    log.info("Downloading tiles image.")
    saved_files_paths = dict()
    saved_files_obj = dict()
    ts = time()
    for key, val in tile_matrix.items():
        saved_files_paths.update({key: list()})
        saved_files_obj.update({key: list()})
        for k, v in val.items():
            resp = download(url=v['url'])
            file = save(tmp_dir, name=k, r=resp)
            # Save list of files path:
            saved_files_paths[key].append(file)
            # Save list of read files
            saved_files_obj[key].append(cv2.imread(file))
    log.info(f"Downloaded all tiles: {saved_files_paths} {time() - ts}")
    return saved_files_paths, saved_files_obj


def concat_tile(im_list_2d):
    return cv2.hconcat([cv2.vconcat(im_list_h) for im_list_h in im_list_2d])


def wipe_temp(temp):
    log.info("Wipe temp.")
    files = glob.glob(temp + "/*")
    for f in files:
        os.remove(f)


def compose_image(matrix, render_path, saved_path, temp):
    """
    https://note.nkmk.me/en/python-opencv-hconcat-vconcat-np-tile/
    :param matrix:
    :param render_path:
    :param saved_path:
    :param temp:
    :return:
    """
    log.info("Composing image.")
    now = datetime.datetime.now()
    im_list_2d = []
    for k, v in matrix.items():
        im_list_2d.append(v)
    # log.info(f"List 2lvl {im_list_2d}")
    image_tile = concat_tile(im_list_2d)
    img_name = f"{render_path}/render.png"
    saved_img = f"{saved_path}/World_{now.strftime('%Y-%m-%d_%H-%M')}.png"
    cv2.imwrite(img_name, image_tile)
    cv2.imwrite(saved_img, image_tile)
    wipe_temp(temp)
    log.info(f"Saving image: {saved_img}")
    return img_name


def set_wallpaper(path):
    # ctypes.windll.user32.SystemParametersInfoW(SPI_SET_WALLPAPER, 0, pathToBmp, 0)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)


def run():
    """
    https://www.winhelponline.com/blog/run-bat-files-invisibly-without-displaying-command-prompt/
    :return:
    """
    log.info("<=== Start wallpaper change ===>")
    tmp = os.path.normpath('E:/Pictures/himawari/tmp')
    render = os.path.normpath('E:/Pictures/himawari/render')
    saved = os.path.normpath('E:/Pictures/himawari/saved')

    img_tiles_matrix = get_image_himawari_sat(level=1, offset=5)
    files_paths, files_obj = download_image_matrix(img_tiles_matrix, tmp)
    image_name = compose_image(files_obj, render, saved, tmp)
    set_wallpaper(path=image_name)
    log.info("<=== Finish wallpaper change ===>")


if __name__ == "__main__":
    run()

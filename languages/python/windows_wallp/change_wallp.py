"""
Change Win10 wallpaper to something downloaded.
"""
import ctypes, os, datetime


pathToBmp = os.path.normpath('C:/Users/kookm_000/Desktop/wallpapers/qR6X0VG.png')


def get_image_himiwari_sat():
    """
    https://himawari.asia/himawari8-image.htm?sI=D531106&sClC=ffff00&sTA=true&sTAT=TY&sS=3&sNx=0&sNy=0&sL=-360.296875&sT=-340.015625&wW=2560&wH=1307&au=true
    :return:
    """
    url = "https://himawari.asia/himawari8-image.htm?sI=D531106&sClC=ffff00&sTA=true&sTAT=TY&sS=3&sNx=0&sNy=0&sL=-360.296875&sT=-340.015625&wW=2560&wH=1307&au=true"


def get_image_zoom_earth():
    """
    https://zoom.earth/#view=28.5,25.3,4z/date=2021-01-11,13:15,+2/layers=nolabels
    :return:
    """
    url = "https://zoom.earth/#view=28.5,25.3,4z/date=2021-01-11,13:15,+2/layers=nolabels"


def get_image_ssec():
    """
    https://www.ssec.wisc.edu/data/geo/images/met-prime/animation_images/

    Get image like:
    'met-prime_' '2021010_0300'  '_01_fd.jpg'
    name          YY_MM_DD_HHMM  postfix
    Times: 00,03,06,09,12,15,18,21,00
    :return:
    """
    url = "https://www.ssec.wisc.edu/data/geo/images/met-prime/animation_images/"
    file_postfix_gif = "_01_fd.gif"
    file_postfix_jpg = "_01_fd.jpg"
    now = datetime.datetime.now()
    file_dt = datetime.datetime.now()


def set_wallpaper(path):
    """

    :param path:
    :return:
    """
    # ctypes.windll.user32.SystemParametersInfoW(SPI_SET_WALLPAPER, 0, pathToBmp, 0)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)

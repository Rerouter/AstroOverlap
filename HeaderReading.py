import math
import os
from typing import Callable, Union, TextIO

from astropy.io import fits
from tkinter import Tk, filedialog
from shapely.geometry import Polygon

LightImages = []
SupportedFileFormats = "fits"
Directory = ''
Output = []


def open_folder():
    """
    :return foldername:
    """
    Tk().withdraw()
    foldername = filedialog.askdirectory(title="Select Folder to Scan")
    if not foldername:
        print("No File Selected")
        return 0
    return foldername


def open_file():
    """
    :return filename:
    """
    Tk().withdraw()
    filename = filedialog.askopenfile(title="Select FITS File",
                                      filetypes=(("FITS files", "*.fits"), ("all files", "*.*")))
    if not filename:
        print("No File Selected")
        return 0
    return filename


def calculate_iou(box_1, box_2):
    poly_1 = Polygon(box_1)
    poly_2 = Polygon(box_2)
    poly_1 = poly_1.buffer(0)
    poly_2 = poly_2.buffer(0)
    iou = poly_1.intersection(poly_2).area / poly_1.union(poly_2).area
    return iou


#def make_file_list():
#    if os.path.isdir(Directory):
#        for filename in os.listdir(Directory):
#            if filename.lower().endswith(SupportedFileFormats):
#                LightImages.append(str(os.path.join(Directory.replace('/', '\\') + os.sep, filename)))


def make_file_list():
    for currentpath, folders, files in os.walk(Directory):
        for file in files:
            filename = os.path.join(currentpath.replace('/', '\\'), file)
            if filename.lower().endswith(SupportedFileFormats):
                LightImages.append(filename)


def compute_overlap(rectangles, reference, output):
    for rectangle in rectangles:
        box_1 = reference[0:3]
        box_2 = rectangle[0:3]
        overlap = calculate_iou(box_1, box_2)
        if overlap:
            output.append([rectangle[4], overlap * 100])
            holder = rectangle
            rectangles.remove(rectangle)
            compute_overlap(rectangles, holder, output)


def make_overlap_list():
    Corners = []
    make_file_list()
    for file in LightImages:
        hdul = fits.open(file)
        hdr = hdul[0].header

        try:
            hdr['OBJCTROT']
            hdr['RA']
            hdr['DEC']
            hdr['FOCALLEN']
            hdr['XPIXSZ']
            hdr['YPIXSZ']
            hdr['NAXIS1']
            hdr['NAXIS2']
        except KeyError:
            LightImages.remove(file)
            continue

        ImageWidth = 206.265 * hdr['XPIXSZ'] / hdr['FOCALLEN'] * hdr['NAXIS1']
        ImageHeight = 206.265 * hdr['YPIXSZ'] / hdr['FOCALLEN'] * hdr['NAXIS2']
        ImageAngle = hdr['OBJCTROT']

        Corners_Local = [[hdr['RA'] + ImageWidth/3600/2, hdr['DEC'] + ImageHeight/3600/2],
                         [hdr['RA'] - ImageWidth/3600/2, hdr['DEC'] + ImageHeight/3600/2],
                         [hdr['RA'] + ImageHeight/3600/2, hdr['DEC'] - ImageHeight/3600/2],
                         [hdr['RA'] - ImageHeight/3600/2, hdr['DEC'] - ImageHeight/3600/2],file]

        for corner in Corners_Local[0:3]:
            centerx = hdr['RA']
            centery = hdr['DEC']
            x = corner[0] - centerx
            y = corner[1] - centery
            a = math.radians(ImageAngle)
            corner[0] = x * math.cos(a) - y * math.sin(a) + centerx
            corner[1] = x * math.sin(a) + y * math.cos(a) + centery

        Corners.append(Corners_Local)

    print(Corners)
    while Corners:
        Reference = Corners.pop()
        Grouping = []
        compute_overlap(Corners, Reference, Grouping)

        if Grouping:
            Output.append([Reference[4], Grouping])

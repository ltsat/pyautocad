#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name = "pyautocad",
    packages = ["pyautocad"],
    version = "0.1.0",
    description = "AutoCAD Automation for python",
    author = "Roman Haritonov",
    author_email = "reclosedev@gmail.com",
    url = "https://bitbucket.org/reclosedev/pyautocad",
    download_url = "https://bitbucket.org/reclosedev/pyautocad/get/582e0cf418d6.zip",
    keywords = ["autocad", "automation", "activex", "comtypes"],
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering",
        ],
    long_description = """\
pyautoacad - AutoCAD Automation for python
------------------------------------------

Example code:

    from pyautocad import Autocad
    from pyautocad import APoint

    acad = Autocad()
    acad.prompt("Hello, Autocad from Python\n")
    print acad.doc.Name

    p1 = APoint(0, 0)
    for i in range(5):
        acad.model.AddMText(p1, 10, u'Hi!')
        p1.y += 10
    p2 = APoint(0, 0)
    acad.model.AddLine(p2, p2 + APoint(0, 100))


    dp = APoint(10, 0)
    for mtext in acad.iter_objects('MText'):
        print mtext.TextString, mtext.InsertionPoint
        mtext.InsertionPoint = APoint(mtext.InsertionPoint) + dp
        #
        # or
        #
        # p = APoint(mtext.InsertionPoint)
        # p.x += 10
        # mtext.InsertionPoint = p
"""
)

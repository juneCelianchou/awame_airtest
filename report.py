# -*- encoding=utf8 -*-
__author__ = "celian"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.report.report import simple_report

simple_report(__file__)
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android:///",
    ])


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)


# Created On: 2011-11-27
# Copyright 2014 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "BSD" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/bsd_license

from qtlib.column import Column
from ..base.results_model import ResultsModel as ResultsModelBase

class ResultsModel(ResultsModelBase):
    COLUMNS = [
        Column('marked', defaultWidth=30),
        Column('name', defaultWidth=200),
        Column('folder_path', defaultWidth=180),
        Column('size', defaultWidth=60),
        Column('extension', defaultWidth=40),
        Column('mtime', defaultWidth=120),
        Column('percentage', defaultWidth=60),
        Column('words', defaultWidth=120),
        Column('dupe_count', defaultWidth=80),
    ]
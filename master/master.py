#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import main_function as fn


search_main_directory = fn.searching('master/csv')

if search_main_directory == True:
    fn.sort()

elif search_main_directory == False:
    os.mkdir('csv')
    fn.sort()

exit()
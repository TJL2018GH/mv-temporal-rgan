#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
import numpy as np
import matplotlib.image as mpimg
from RGAN import RGAN

# compile RGAN and load images
train_images = [mpimg.imread(file) for file in glob.glob("./data/faces/*")]
train_images = np.asarray(train_images,dtype="float32")
train_images /= 255
# run model and check outout
test = RGAN()
test.train(train_images,"test")
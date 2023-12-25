#!/usr/bin/python

# avenir-python: Machine Learning
# Author: Pranab Ghosh
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you
# may not use this file except in compliance with the License. You may
# obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0 
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied. See the License for the specific language governing
# permissions and limitations under the License.

# Package imports
import os
import sys
import argparse
from matumizi.util import *
from matumizi.mlutil import *
from matumizi.sampler import *
from dcmpnet import *

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--op', type=str, default = "none", help = "operation")
	parser.add_argument('--cfpath', type=str, default = "", help = "config file path")
	parser.add_argument('--prec', type=int, default = 3, help = "floating point precision")
	parser.add_argument('--nplots', type=int, default = -1, help = "num of plots")
	parser.add_argument('--findex', type=int, default = -1, help = "forecast woindow index")
	parser.add_argument('--tibeg', type=int, default = -1, help = "time begin index")
	parser.add_argument('--tiend', type=int, default = -1, help = "time end index")
	parser.add_argument('--trvafile', type=str, default = "none", help = "trend validation file")
	parser.add_argument('--revafile', type=str, default = "none", help = "remian validation file")

	args = parser.parse_args()
	op = args.op
	
	dn = DecmpNetwork(args.cfpath)
	
	if op == "decomp":
		dn.decompose()

	elif op == "train":
		dn.fit()

	elif op == "validate":
		trVaFpath = args.trvafile if args.trvafile != "none" else None
		reVaFpath = args.revafile if args.revafile != "none" else None
		dn.validate(args.findex, args.tibeg, args.tiend, trVaFpath, reVaFpath)
		
	else:
		exitWithMsg("invalid command")

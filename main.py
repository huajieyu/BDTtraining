#import pandas as pd

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import GradientBoostingClassifier
import os, sys
import ROOT

def dfstart():
	print("this is the begining of readin the input data")

	wd=os.path.dirname("/dune/app/users/jiang/dunetpc_analysis/newduneana_May/PionAbsChxAna/Main/mac/")
	if wd:
		os.chdir(wd)
		print("found the working directory")
		histFileName = "output_test.root"
		histFileName_data = "output_test_data.root"
		histFile = ROOT.TFile.Open(histFileName, "READ")
		histFile_data = ROOT.TFile.Open(histFileName_data, "READ")

		dataHisto = histFile_data.Get("h_Evttot")
		mcHisto = histFile.Get("h_Evttot")
		canvas = ROOT.TCanvas("canvas")
		canvas.cd()
		dataHisto.Draw("h")
		plotFileName="h_Evttot.pdf"
		canvas.Print(plotFileName+"[")
		canvas.Print(plotFileName+"]")

if __name__=="__main__":
	dfstart();

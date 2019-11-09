import pluginTypes as pluginTypes
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import os


class revSTEM(pluginTypes.IExtensionPlugin):

	def __init__(self):
		super(revSTEM, self).__init__()

		# self.detectorInfo = {'dwellTime': self.dwellTime, 'binning': self.binning, 'numFrames': self.numFrames,
		# 					 'detectors': ['DF2', 'BF']}

		self.defaultParameters = {'name': 'revSTEM', 'rotation': '90', 'dwellTime': '5e-6',
		                          'binning': '512x512',
		                          'numFrames': '12', 'detectors': ['HAADF']}

	def run(self, input):
		frames = int(input['numFrames'])
		print(frames)
		tia = self.interfaces['tiascript']
		stem = tia.techniques['STEMImage']

		stem.setupAcquisition(input)
		rotAngle = float(input['rotation'])

		for i in range(frames):
			print(f'acqiuring {i}')
			rot = i * rotAngle
			stem.scanRotation(rot)
			stem.acquire()

		return None
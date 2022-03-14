import json
import numpy as np
import ruptures as rpt

import os

os.environ["HOME"] = "/app/"

import matplotlib.pyplot as plt

input_directory = os.environ['IEXEC_IN']
output_directory = os.environ['IEXEC_OUT']
input_filename = os.environ['IEXEC_DATASET_FILENAME']

filepath = os.path.join(input_directory, input_filename)
print("Loading file " + filepath)

signal = np.genfromtxt(filepath, delimiter=',')
algo = rpt.Pelt(model="rbf").fit(signal)
result = algo.predict(pen=10)

rpt.display(signal, [], result)
plt.savefig(os.path.join(output_directory, "ruptures_result.pdf"))

with open(os.path.join(output_directory, "computed.json"), 'w+') as f:
    json.dump(
        {"deterministic-output-path": os.path.join(output_directory, "ruptures_result.pdf")}, f)

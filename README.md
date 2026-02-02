# pymirtoolbox

Python wrapper around a compiled [MIRtoolbox](https://www.jyu.fi/hytk/fi/laitokset/mutku/en/research/materials/mirtoolbox) (version 1.8.2) component, exposing MIR features like `mirbrightness`, `mirtempo`, `mirmfcc`, and `mirchromagram` as NumPy arrays.

The goal is to keep a one-to-one naming with MIRtoolbox (`mirbrightness`, `mirtempo`, …) while making the API convenient to use from Python and IDE-friendly.

---

## Installation
> **Important:** `pymirtoolbox` currently supports Python **3.10–3.12** only, and requires **MATLAB Runtime R2025b** (or full **MATLAB R2025b**). Compatibility outside these versions is not guaranteed.

### Linux

**Note**: If you already have MATLAB R2025b installed, you typically do not need a separate MATLAB Runtime.

1. Install MATLAB Runtime R2025b (no license needed):
> You can download it manually from [Mathworks website](https://www.mathworks.com/products/compiler/matlab-runtime.html), or use the following `wget` command to download the source and then unzip and install it:

```
wget https://ssd.mathworks.com/supportfiles/downloads/R2025b/Release/2/deployment_files/installer/complete/glnxa64/MATLAB_Runtime_R2025b_Update_2_glnxa64.zip  
unzip -qq -d matlabruntime MATLAB_Runtime_R2025b_Update_2_glnxa64.zip  
cd matlabruntime/  
sudo ./install -agreeToLicense yes
```
2. Add MATLAB Runtime libraries to your environment (bash):
```
echo 'export LD_LIBRARY_PATH="${LD_LIBRARY_PATH:+${LD_LIBRARY_PATH}:}/usr/local/MATLAB/MATLAB_Runtime/R2025b/runtime/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/R2025b/bin/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/R2025b/sys/os/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/R2025b/extern/bin/glnxa64"' >> ~/.bashrc  
source ~/.bashrc
```
3. Clone and install `pymirtoolbox`:
```
git clone https://github.com/yourname/pymirtoolbox.git  
cd pymirtoolbox  

virtualenv pymirvenv -p python3.12  
source pymirvenv/bin/activate  

pip install .
```
You can now import and use `pymirtoolbox` in your code.

---

### macOS

1. MATLAB Runtime / MATLAB:

   - If you already have MATLAB R2025b installed, you typically do not need a separate MATLAB Runtime.
   - Otherwise, download the [MATLAB Runtime R2025b (25.2) macOS installer from MathWorks](https://www.mathworks.com/products/compiler/matlab-runtime.html) and install it via the GUI.

2. Clone and install `pymirtoolbox`:
```
git clone https://github.com/yourname/pymirtoolbox.git  
cd pymirtoolbox  

virtualenv pymirvenv -p python3.12  
source pymirvenv/bin/activate  

pip install .
```
3. Running scripts with MATLAB (if needed):

   If you installed MATLAB Runtime:
```
/Applications/MATLAB/MATLAB_Runtime/R2025b/bin/mwpython YOUR_SCRIPT.py
```
   If you have the full MATLAB installation:
```
/Applications/MATLAB_R2025b.app/bin/mwpython YOUR_SCRIPT.py
```
---

## Usage

Basic example:
```
from pymirtoolbox import feature_extractor

result = feature_extractor.mirbrightness(
    audio_input="path/to/audio.wav",
    Frame=True,
    CutOff=1500,
)

brightness = result["brightness"]

result = feature_extractor.mirmfcc(
    audio_input="path/to/audio.wav",
    Frame=True,
    Rank=13,
)

mfcc = result["mfcc"]
melspec = result["melspec"]
```

For the full list of features, parameters, and output shapes, see the
[Feature reference](FEATURES.md).

For details on the compiled MATLAB dispatcher and build process, see the
[MATLAB component](matlab_component/).

---

## Contributing

Right now the focus is on completing the list of extractable features.

- To add a new feature, add a new entry to `pymirtoolbox/feature_metadata.json` following the existing structure (name, category, description, outputs, params).
- The helpers that generate docs, tests, and type stubs use this JSON and will pick it up automatically.

Future plans include:

- Folder / batch processing.
- Exposing additional MIRtoolbox operators beyond the current feature extractors.

Pull requests that extend or refine the feature metadata are very welcome.

---

## License and copyright

[MIRtoolbox](https://www.jyu.fi/hytk/fi/laitokset/mutku/en/research/materials/mirtoolbox) is free software, available under the terms of the GNU General Public License (GPL), as stated by its authors (see the MIRtoolbox website and manual).

`pymirtoolbox` is an independent Python project designed to interoperate with compiled MIRtoolbox components and is developed separately from the MIRtoolbox authors and MathWorks.

`pymirtoolbox` is distributed under the same license terms (GNU GPL v2). See the `LICENSE` file in this repository for details.

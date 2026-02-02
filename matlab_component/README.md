# MATLAB component

This folder contains the MATLAB dispatcher and build script for the compiled MIRtoolbox component used by `pymirtoolbox`.

---

## Files

- `feature_dispatcher.m`  
  MATLAB entry point used by the Python wrapper. It receives a feature name and audio input, looks up the corresponding MIR function and outputs in `feature_metadata.json`, calls the appropriate MIRtoolbox function(s), and returns a struct of named outputs.

- `builder.m`  
  MATLAB build script that calls `compiler.build.pythonPackage` to generate the Python package (including the compiled component and `.ctf` file) from `feature_dispatcher.m` and the MIRtoolbox folder.

---

## `builder.m`

The `builder.m` script ties together the dispatcher and MIRtoolbox when building the Python package. Its core content is:
```
mirToolboxFolder = 'mirtoolbox1.8.2';
outDir = fullfile(pwd, "pymirtoolbox");
appFile = which("feature_dispatcher.m");

buildResults = compiler.build.pythonPackage(appFile, ...
    PackageName="pymirtoolbox", ...
    OutputDir=outDir, ...
    AdditionalFiles={mirToolboxFolder}, ...
    Verbose="on");
```
- `mirToolboxFolder` should point to the MIRtoolbox installation you want to bundle (for example, `mirtoolbox1.8.2`).
- `appFile` is the main MATLAB file that exposes the features (`feature_dispatcher.m`).
- `compiler.build.pythonPackage` produces a Python package under `OutputDir` named after `PackageName`, which contains the compiled component and the `.ctf` archive.

---

## Overview

MATLAB provides a feature that can compile MATLAB code into components usable from other languages, such as Python. These components expose a callable interface in the destination language without requiring a full MATLAB installation or license on the target machine. Instead, they run on top of the MATLAB Runtime, which is license-free and intended specifically for executing compiled MATLAB code (not for interactive MATLAB usage or toolbox development).

The Python package compiler (`compiler.build.pythonPackage`) generates, among other files, two important pieces:

- an `__init__.py` module that provides the Python interface to the compiled component
- a `PACKAGE_NAME.ctf` file containing the compiled MATLAB code and resources

To compile this project you need, on the build machine:

- MATLAB
- MATLAB Compiler SDK
- DSP System Toolbox
- Statistics and Machine Learning Toolbox
- MIRtoolbox (for example, version 1.8.2)

Note that the generated binaries are platform-specific: if you build on Linux, the resulting package (and its compiled binaries) will work on Linux; if you build on macOS, on macOS, and so on.

For this project:

- Download and install MIRtoolbox (e.g. version 1.8.2), and set `mirToolboxFolder` in `builder.m` to the folder containing MIRtoolbox.
- Ensure `feature_dispatcher.m` is on the MATLAB path and use its location as `appFile` in `builder.m`. This file is the main entry point: it reads the feature metadata JSON, dispatches to the appropriate MIRtoolbox functions, and shapes the outputs that Python receives.
- Run `builder.m`. It will produce a Python package in the directory specified by `OutputDir`, in a subfolder named after `PackageName`.

For more information and the official documentation of the MATLAB-to-Python workflow, see:

- https://www.mathworks.com/help/compiler_sdk/gs/create-a-python-application-with-matlab-code.html

After running `builder.m`, you will see the generated Python package in the `PackageName` folder. The two key files there are the `__init__.py` and the `.ctf` file. To support multiple platforms (for example, Linux and macOS), you can repeat the build on each target OS and keep the corresponding generated packages in your project, selecting the appropriate one at runtime based on the current platform.

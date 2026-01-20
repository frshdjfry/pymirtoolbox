# pymirtoolbox.feature_extractor

## Rhythm

### `mirtempo`

Estimates the tempo of the audio in beats per minute, optionally over time.

**Outputs**

| Name | Type | Shape | Units | Description |
| ---- | ---- | ----- | ----- | ----------- |
| `tempo` | matrix | (n_candidates, n_frames, n_channels) for frame-based analysis, or (n_candidates, n_channels) for global tempo. | BPM | Estimated tempo values in beats per minute, either global or per frame and per candidate. |
| `autocor` | matrix | Feature-dependent matrix or tensor describing periodicity over lag/frequency, frames, and channels. | arbitrary | Tempo-related autocorrelation or spectrum representation used internally for tempo estimation. |

**Parameters**

| Name | Type | Default | Example | Unit | Description |
| ---- | ---- | ------- | ------- | ---- | ----------- |
| `audio_input` | string | null | tests/data/test.wav | None | Path to the audio file to analyze. |
| `Frame` | bool | False | True | None | Estimate tempo over successive frames instead of as a single global value. |
| `Min` | number | 40 | 60 | BPM | Minimum tempo to consider in the search range. |
| `Max` | number | 200 | 180 | BPM | Maximum tempo to consider in the search range. |
| `Total` | number | 1 | 3 | count | Number of best tempo candidates to return. |

## Timbre

### `mirbrightness`

Spectral brightness, defined as the proportion of energy above a cutoff frequency.

**Outputs**

| Name | Type | Shape | Units | Description |
| ---- | ---- | ----- | ----- | ----------- |
| `brightness` | matrix | (n_frames, n_channels) for frame-based analysis, or (1, n_channels) for global brightness. | ratio | Brightness values per frame or globally, in the range [0, 1]. |

**Parameters**

| Name | Type | Default | Example | Unit | Description |
| ---- | ---- | ------- | ------- | ---- | ----------- |
| `audio_input` | string | null | tests/data/test.wav | None | Path to the audio file to analyze. |
| `Frame` | bool | False | True | None | Compute brightness over successive frames instead of as a single global value. |
| `CutOff` | number | 1500 | 1500 | Hz | Cutoff frequency above which spectral energy is considered for brightness. |
| `MinRMS` | number | 0.01 | 0.01 | RMS | Minimum RMS energy threshold below which frames are treated as silence. |

### `mirmfcc`

Mel-frequency cepstral coefficients describing the spectral envelope over time.

**Outputs**

| Name | Type | Shape | Units | Description |
| ---- | ---- | ----- | ----- | ----------- |
| `mfcc` | matrix | (n_coeffs, n_frames, n_channels) | cepstral | MFCC coefficients for each frame. |
| `melspec` | matrix | (n_bands, n_frames, n_channels) | dB | Mel-band log-magnitude spectrum for each frame. |

**Parameters**

| Name | Type | Default | Example | Unit | Description |
| ---- | ---- | ------- | ------- | ---- | ----------- |
| `audio_input` | string | null | tests/data/test.wav | None | Path to the audio file to analyze. |
| `Frame` | bool | False | True | None | Compute MFCCs in successive frames instead of as a single global descriptor. |
| `Rank` | number | 13 | 13 | coeffs | Number of MFCC coefficients to compute starting from rank 1. |

## Tonal

### `mirchromagram`

Chromagram representation of pitch-class energy over time.

**Outputs**

| Name | Type | Shape | Units | Description |
| ---- | ---- | ----- | ----- | ----------- |
| `chromagram` | matrix | (n_chroma_bins, n_frames, n_channels) | normalized energy | Chroma energy values over time, optionally across channels or filterbank subbands. |

**Parameters**

| Name | Type | Default | Example | Unit | Description |
| ---- | ---- | ------- | ------- | ---- | ----------- |
| `audio_input` | string | null | tests/data/test.wav | None | Path to the audio file to analyze. |
| `Frame` | bool | False | True | None | Compute a time-varying chromagram instead of a single global chroma vector. |
| `Res` | number | 12 | 24 | bins per octave | Chromatic resolution, i.e. number of chroma bins per octave. |
| `Wrap` | string | yes | no | None | Whether to wrap chroma into a single octave (key-invariant) or keep absolute pitch information. |
| `Normal` | number | 1 | 2 | L-norm | Normalization applied to each chroma vector (0: none, 1: L1, 2: L2). |
| `Tuning` | number | 440.0 | 440.0 | Hz | Reference tuning frequency of A4. |


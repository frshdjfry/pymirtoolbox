# pymirtoolbox.feature_extractor

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

### `mirhcdf`

Harmonic change detection function (HCDF) describing the amount of harmonic change between successive frames.

**Outputs**

| Name | Type | Shape | Units | Description |
| ---- | ---- | ----- | ----- | ----------- |
| `hcdf` | matrix | (n_frames, n_channels) | arbitrary | HCDF values over time, with larger values indicating stronger harmonic change between frames. |

**Parameters**

| Name | Type | Default | Example | Unit | Description |
| ---- | ---- | ------- | ------- | ---- | ----------- |
| `audio_input` | string | null | tests/data/test.wav | None | Path to the audio file to analyze. |
| `Frame` | bool | True | True | None | Compute the HCDF over successive frames. Typically enabled since HCDF is defined over time. |

### `mirkey`

Estimates the musical key of the audio, optionally over time.

**Outputs**

| Name | Type | Shape | Units | Description |
| ---- | ---- | ----- | ----- | ----------- |
| `key` | matrix | (n_frames, n_channels) for frame-based analysis, or (1, n_channels) for global key estimation. | key index or label representation | Estimated musical key values, either globally or per frame. |

**Parameters**

| Name | Type | Default | Example | Unit | Description |
| ---- | ---- | ------- | ------- | ---- | ----------- |
| `audio_input` | string | null | tests/data/test.wav | None | Path to the audio file to analyze. |
| `Frame` | bool | False | True | None | Estimate the key on successive frames instead of as a single global value. |

### `mirkeystrength`

Computes key strength, i.e. a score between -1 and +1 associated with each possible key candidate, based on cross-correlation of the chromagram with tonal profiles.

**Outputs**

| Name | Type | Shape | Units | Description |
| ---- | ---- | ----- | ----- | ----------- |
| `keystrength` | matrix | (n_tonal_centers, n_frames, n_channels, 2) where the last dimension indexes major (layer 1) and minor (layer 2) keys. | correlation score in [-1, 1] | Key strength values for each tonal center and time position, with separate layers for major and minor keys. |
| `chromagram` | matrix | (n_chroma_bins, n_frames, n_channels) | normalized energy | Underlying wrapped and normalized chromagram used for key strength estimation. |

**Parameters**

| Name | Type | Default | Example | Unit | Description |
| ---- | ---- | ------- | ------- | ---- | ----------- |
| `audio_input` | string | null | tests/data/test.wav | None | Path to the audio file to analyze. |
| `Frame` | bool | False | True | None | Compute a time-varying key strength curve over successive frames instead of a single global profile. |
| `Weight` | number | null | 0.5 | None | Weight parameter forwarded to the underlying chromagram computation, controlling profile weighting. |
| `Triangle` | bool | null | True | None | Triangle weighting option forwarded to the underlying chromagram computation. |

### `mirmode`

Computes key strength, i.e. a score between -1 and +1 associated with each possible key candidate, based on cross-correlation of the chromagram with tonal profiles.

**Outputs**

| Name | Type | Shape | Units | Description |
| ---- | ---- | ----- | ----- | ----------- |
| `keystrength` | matrix | (n_tonal_centers, n_frames, n_channels, 2) where the last dimension indexes major (layer 1) and minor (layer 2) keys. | correlation score in [-1, 1] | Key strength values for each tonal center and time position, with separate layers for major and minor keys. |
| `chromagram` | matrix | (n_chroma_bins, n_frames, n_channels) | normalized energy | Underlying wrapped and normalized chromagram used for key strength estimation. |

**Parameters**

| Name | Type | Default | Example | Unit | Description |
| ---- | ---- | ------- | ------- | ---- | ----------- |
| `audio_input` | string | null | tests/data/test.wav | None | Path to the audio file to analyze. |
| `Frame` | bool | False | True | None | Compute a time-varying key strength curve over successive frames instead of a single global profile. |
| `Weight` | number | null | 0.5 | None | Weight parameter forwarded to the underlying chromagram computation, controlling profile weighting. |
| `Triangle` | bool | null | True | None | Triangle weighting option forwarded to the underlying chromagram computation. |


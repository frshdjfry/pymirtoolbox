# pymirtoolbox.feature_extractor

## Pitch

### `mirinharmonicity`

Estimates inharmonicity, i.e. the amount of partial energy that does not lie on the ideal harmonic series of a fundamental frequency, as values between 0 and 1.

**Outputs**

| Name | Type | Shape | Units | Description |
| ---- | ---- | ----- | ----- | ----------- |
| `inharmonicity` | matrix | (n_frames, n_channels) for frame-based analysis, or (1, n_channels) for global inharmonicity. | ratio | Inharmonicity rate, either globally or per frame, with values between 0 and 1. |
| `spectrum` | matrix | (n_freq_bins, n_frames, n_channels) | magnitude | Spectrum representation used internally for the inharmonicity estimation. |
| `f0` | matrix | (n_frames, n_channels) | Hz | Fundamental frequency used as reference for the harmonic series. |

**Parameters**

| Name | Type | Default | Example | Unit | Description |
| ---- | ---- | ------- | ------- | ---- | ----------- |
| `audio_input` | string | null | tests/data/test.wav | None | Path to the audio file to analyze. |
| `Frame` | bool | False | True | None | Compute the inharmonicity over successive frames instead of as a single global value. |

### `mirpitch`

Estimates pitch content and returns pitch frequencies in Hz, optionally with multiple candidates over time.

**Outputs**

| Name | Type | Shape | Units | Description |
| ---- | ---- | ----- | ----- | ----------- |
| `pitch` | matrix | (n_pitches, n_frames, n_channels) | Hz | Estimated pitch frequencies in Hz, possibly with multiple candidates per frame. |
| `representation` | matrix | Feature-dependent periodicity representation over lag/frequency, frames, and channels. | arbitrary | Autocorrelation or cepstral representation used for pitch estimation, with highlighted peaks for selected pitches. |

**Parameters**

| Name | Type | Default | Example | Unit | Description |
| ---- | ---- | ------- | ------- | ---- | ----------- |
| `audio_input` | string | null | tests/data/test.wav | None | Path to the audio file to analyze. |
| `Frame` | bool | False | True | None | Estimate pitch on successive frames instead of on a single global segment. |
| `Min` | number | 75 | 75 | Hz | Minimum pitch to consider, in Hz. |
| `Max` | number | 2400 | 2400 | Hz | Maximum pitch to consider, in Hz. |
| `Total` | number | 1 | 3 | count | Number of best pitch candidates to keep per frame. |
| `Mono` | bool | False | True | None | If true, select only the single best pitch per frame (equivalent to Total = 1). |

## Rhythm

### `mireventdensity`

Estimates the average frequency of events, i.e., the number of note onsets per second, either globally or over time.

**Outputs**

| Name | Type | Shape | Units | Description |
| ---- | ---- | ----- | ----- | ----------- |
| `eventdensity` | matrix | (n_frames, n_channels) for frame-based analysis, or (1, n_channels) for global density. | events per second | Event density values, either per frame or as a single global value, representing the number of note onsets per second. |

**Parameters**

| Name | Type | Default | Example | Unit | Description |
| ---- | ---- | ------- | ------- | ---- | ----------- |
| `audio_input` | string | null | tests/data/test.wav | None | Path to the audio file to analyze. |
| `Frame` | bool | False | True | None | Compute event density over successive frames instead of as a single global value. |

### `mirmetroid`

Dynamic metrical centroid and metrical strength curves derived from the metrical analysis carried out using mirmetre.

**Outputs**

| Name | Type | Shape | Units | Description |
| ---- | ---- | ----- | ----- | ----------- |
| `metrical_centroid` | matrix | (n_frames, n_channels) | BPM | Dynamic metrical centroid curve describing the temporal evolution of metrical activity in BPM. |
| `metrical_strength` | matrix | (n_frames, n_channels) | arbitrary | Dynamic metrical strength curve indicating the overall strength of the dominant metrical levels, potentially exceeding 1. |

**Parameters**

| Name | Type | Default | Example | Unit | Description |
| ---- | ---- | ------- | ------- | ---- | ----------- |
| `audio_input` | string | null | tests/data/test.wav | None | Path to the audio file to analyze. |
| `Gate` | bool | False | True | None | Use a simpler weighting method where weights equal autocorrelation scores of the dominant metrical levels, which may yield more abrupt changes in the metrical centroid curve. |
| `Combine` | bool | True | False | None | If false, do not combine multiple metrical hierarchies; instead, return separate centroid and strength curves for each detected metrical hierarchy. |

### `mirpulseclarity`

Estimates rhythmic pulse clarity, indicating the strength of the beats as derived from the mirtempo analysis.

**Outputs**

| Name | Type | Shape | Units | Description |
| ---- | ---- | ----- | ----- | ----------- |
| `pulseclarity` | matrix | (n_frames, n_channels) for frame-based analysis, or (1, n_channels) for global pulse clarity. | arbitrary (higher values indicate clearer pulse) | Pulse clarity values, either as a single global value or as a curve over time when frame-based analysis is used. |
| `autocor` | matrix | (n_lags, n_frames, n_channels) | correlation | Autocorrelation representation used internally for the pulse clarity estimation. |

**Parameters**

| Name | Type | Default | Example | Unit | Description |
| ---- | ---- | ------- | ------- | ---- | ----------- |
| `audio_input` | string | null | tests/data/test.wav | None | Path to the audio file to analyze. |
| `Frame` | bool | False | True | None | Compute pulse clarity over successive frames instead of as a single global value. |
| `Model` | number | 1 | 1 | index | Model index controlling which optimized pulse-clarity model to use (1: default model, 2: alternative model, [1 2]: combined). |

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

### `mirregularity`

Spectral irregularity, measuring the variability of successive spectral peaks.

**Outputs**

| Name | Type | Shape | Units | Description |
| ---- | ---- | ----- | ----- | ----------- |
| `irregularity` | matrix | (n_frames, n_channels) for frame-based analysis, or (1, n_channels) for global irregularity. | ratio | Irregularity values, either per frame or as a single global value, typically between 0 and 2. |

**Parameters**

| Name | Type | Default | Example | Unit | Description |
| ---- | ---- | ------- | ------- | ---- | ----------- |
| `audio_input` | string | null | tests/data/test.wav | None | Path to the audio file to analyze. |
| `Frame` | bool | False | True | None | Compute irregularity over successive frames instead of as a single global value. |
| `Jensen` | bool | False | True | None | Use the Jensen (1999) definition, where irregularity is based on squared differences between adjoining partial amplitudes. This is the default model in MIRtoolbox when no specific method is given. |
| `Krimphof` | bool | False | False | None | Use the Krimphoff et al. (1994) definition, where irregularity is based on deviations from the local mean of each partial and its neighbours. |

### `mirroughness`

Estimates sensory roughness (dissonance) of the sound over time or globally.

**Outputs**

| Name | Type | Shape | Units | Description |
| ---- | ---- | ----- | ----- | ----------- |
| `roughness` | matrix | (n_frames, n_channels) for frame-based analysis, or (1, n_channels) for global roughness. | arbitrary | Roughness values, either per frame or globally, reflecting sensory dissonance of the signal. |

**Parameters**

| Name | Type | Default | Example | Unit | Description |
| ---- | ---- | ------- | ------- | ---- | ----------- |
| `audio_input` | string | null | tests/data/test.wav | None | Path to the audio file to analyze. |
| `Frame` | bool | False | True | None | Compute roughness over successive frames instead of as a single global value. |

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

Estimates the musical mode (typically major vs. minor) of the audio, either globally or over time.

**Outputs**

| Name | Type | Shape | Units | Description |
| ---- | ---- | ----- | ----- | ----------- |
| `mode` | matrix | (n_modes, n_frames, n_channels) for frame-based analysis, or (n_modes, 1, n_channels) for global mode estimation. | mode strength | Mode strength values for the main modes (e.g., major and minor), either globally or per frame. |

**Parameters**

| Name | Type | Default | Example | Unit | Description |
| ---- | ---- | ------- | ------- | ---- | ----------- |
| `audio_input` | string | null | tests/data/test.wav | None | Path to the audio file to analyze. |
| `Frame` | bool | False | True | None | Estimate mode on successive frames instead of as a single global value. |


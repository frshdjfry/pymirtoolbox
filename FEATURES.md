# pymirtoolbox.feature_extractor

## Tonal

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


function result = feature_dispatcher(feature, filename, varargin)
    if ~ischar(feature) && ~isstring(feature)
        error('FEATURE must be a char or string.');
    end
    if ~ischar(filename) && ~isstring(filename)
        error('FILENAME must be a char or string path to an audio file.');
    end

    feature = lower(strtrim(char(feature)));
    filename = char(filename);

    if isempty(varargin)
        error('Metadata path must be provided as an additional argument.');
    end

    metaPath = varargin{1};
    varargin(1) = [];

    if ~ischar(metaPath) && ~isstring(metaPath)
        error('Metadata path must be a char or string.');
    end
    metaPath = char(metaPath);

    persistent FEATURE_META META_PATH_CACHED
    if isempty(FEATURE_META) || isempty(META_PATH_CACHED) || ~strcmp(META_PATH_CACHED, metaPath)
        if ~exist(metaPath, 'file')
            error('Feature metadata file not found: %s', metaPath);
        end
        jsonText = fileread(metaPath);
        FEATURE_META = jsondecode(jsonText);
        META_PATH_CACHED = metaPath;
    end

    if ~isfield(FEATURE_META, feature)
        supported = strjoin(fieldnames(FEATURE_META), ', ');
        error('Unknown feature "%s". Supported: %s.', feature, supported);
    end

    meta = FEATURE_META.(feature);
    if ~isfield(meta, 'outputs')
        error('No outputs defined for feature "%s" in metadata.', feature);
    end

    outputsSpec = meta.outputs;
    outNames = fieldnames(outputsSpec);
    maxIdx = 0;
    for i = 1:numel(outNames)
        on = outNames{i};
        outSpec = outputsSpec.(on);
        if ~isstruct(outSpec) || ~isfield(outSpec, 'index')
            error('Invalid output spec for feature "%s", output "%s".', feature, on);
        end
        idx = outSpec.index;
        if ~isscalar(idx) || ~isnumeric(idx)
            error('Invalid output index for feature "%s", output "%s".', feature, on);
        end
        if idx > maxIdx
            maxIdx = idx;
        end
    end

    if maxIdx < 1
        error('No valid output indices defined for feature "%s".', feature);
    end

    mirFuncName = char(meta.name);
    fh = str2func(mirFuncName);

    mirObjs = cell(1, maxIdx);
    [mirObjs{:}] = fh(filename, varargin{:});

    s = struct();
    for i = 1:numel(outNames)
        on = outNames{i};
        outSpec = outputsSpec.(on);
        idx = outSpec.index;
        if idx <= numel(mirObjs) && ~isempty(mirObjs{idx})
            s.(on) = mirgetdata(mirObjs{idx});
        else
            s.(on) = [];
        end
    end

    result = s;
end

# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import ConcatenateLTA


def test_ConcatenateLTA_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_lta1=dict(argstr='%s',
    mandatory=True,
    position=-3,
    ),
    in_lta2=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    out_file=dict(argstr='%s',
    hash_files=False,
    keep_extension=True,
    name_source=['in_lta1'],
    name_template='%s-long',
    position=-1,
    ),
    subjects_dir=dict(),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = ConcatenateLTA.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ConcatenateLTA_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = ConcatenateLTA.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""This module provides interfaces for workbench surface commands"""
from __future__ import (print_function, division, unicode_literals,
                        absolute_import)
import os

from ..base import (TraitedSpec, File, traits, CommandLineInputSpec)
from .base import WBCommand
from ... import logging

iflogger = logging.getLogger('nipype.interface')


class CiftiSeparateInputSpec(CommandLineInputSpec):
    in_file = File(
        exists=True,
        mandatory=True,
        argstr="%s",
        position=0,
        desc="the input cifti file")
    direction = traits.Enum(
        "ROW",
        "COLUMN",
        mandatory=True,
        argstr="%s",
        position=1,
        desc="which direction to separate into components, ROW or COLUMN")
    out_volume = File(
        name_source=["in_file"],
        name_template="%s.nii.gz",
        keep_extension=False,
        argstr="-volume-all %s",
        position=2,
        desc="separate all volume structures into a volume file")
    out_left = File(
        name_source=["in_file"],
        name_template="%s.L.func.gii",
        keep_extension=False,
        argstr="-metric CORTEX_LEFT %s",
        position=3,
        desc="separate a surface model into CORTEX_LEFT")
    out_right = File(
        name_source=["in_file"],
        name_template="%s.R.func.gii",
        keep_extension=False,
        argstr="-metric CORTEX_RIGHT %s",
        position=4,
        desc="separate a surface model into CORTEX_RIGHT")

class CiftiSeparateOutputSpec(TraitedSpec):
    out_volume = File(exists=True, desc="the output volume")
    out_left = File(exists=True, desc="the output left surface")
    out_right = File(exists=True, desc="the output right surface")


class CiftiSeparate(WBCommand):
    """
    Separate a CIFTI file into volume and left and right surfaces

   
    """
    input_spec = CiftiSeparateInputSpec
    output_spec = CiftiSeparateOutputSpec
    _cmd = 'wb_command -cifti-separate'

    def _format_arg(self, opt, spec, val):
        return super(CiftiSeparate, self)._format_arg(opt, spec, val)

    def _list_outputs(self):
        outputs = super(CiftiSeparate, self)._list_outputs()
        return outputs


class CiftiCreateDenseTimeseriesInputSpec(CommandLineInputSpec):
    out_file = File(
        name_source=["volume_file"],
        name_template="%s.dtseries.nii",
        keep_extension=False,
        argstr="%s",
        position=0,
        desc="the output cifti file")
    volume_file = File(
        exists=True,
        mandatory=True,
        argstr="-volume %s",
        position=1,
        desc="volume file containing all voxel data for all volume structures")
    volume_label = File(
        exists=True,
        mandatory=True,
        argstr="%s",
        position=2,
        desc="label volume file containing labels for cifti structures")
    left_metric = File(
        exists=True,
        mandatory=True,
        argstr="-left-metric %s",
        position=3,
        desc="metric for left surface")
    right_metric = File(
        exists=True,
        mandatory=True,
        argstr="-right-metric %s",
        position=4,
        desc="metric for right surface")

class CiftiCreateDenseTimeseriesOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc="the output cifti file")


class CiftiCreateDenseTimeseries(WBCommand):
    """
    Combine volume and left and right surfaces into a dense timeseries CIFTI

   
    """
    input_spec = CiftiCreateDenseTimeseriesInputSpec
    output_spec = CiftiCreateDenseTimeseriesOutputSpec
    _cmd = 'wb_command -cifti-create-dense-timeseries'

    def _format_arg(self, opt, spec, val):
        return super(CiftiSeparate, self)._format_arg(opt, spec, val)

    def _list_outputs(self):
        outputs = super(CiftiSeparate, self)._list_outputs()
        return outputs


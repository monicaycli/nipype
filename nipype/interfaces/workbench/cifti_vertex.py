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


class CiftiSmoothInputSpec(CommandLineInputSpec):
    in_file = File(
        exists=True,
        mandatory=True,
        argstr="%s",
        position=0,
        desc="the input cifti file")
    surface_sigma = traits.Float(
        argstr="%.8f",
        mandatory=True,
        position=1,
        desc="the sigma for the gaussian surface smoothing kernel,in mm")
    volume_sigma = traits.Float(
        argstr="%.8f",
        mandatory=True,
        position=2,
        desc="the sigma for the gaussian volume smoothing kernel,in mm")
    direction = traits.Enum(
        "ROW",
        "COLUMN",
        mandatory=True,
        argstr="%s",
        position=3,
        desc="which direction to ssmooth, ROW or COLUMN")
    out_file = File(
        name_source=["in_file"],
        name_template="%s_smooth",
        keep_extension=True,
        argstr="%s",
        position=4,
        desc="the output cifti file")
    left_surface = File(
        exists=True,
        mandatory=True,
        argstr="-left-surface %s",
        position=5,
        desc="specify the left surface to use")
    right_surface = File(
        exists=True,
        mandatory=True,
        argstr="-right-surface %s",
        position=6,
        desc="specify the right surface to use")


class CiftiSmoothOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc="the output cifti file")


class CiftiSmooth(WBCommand):
    """
   Smooth a CIFTI file

   
    """
    input_spec = CiftiSmoothInputSpec
    output_spec = CiftiSmoothOutputSpec
    _cmd = 'wb_command -cifti-smoothing'

    def _format_arg(self, opt, spec, val):
        return super(CiftiSmooth, self)._format_arg(opt, spec, val)

    def _list_outputs(self):
        outputs = super(CiftiSmooth, self)._list_outputs()
        return outputs

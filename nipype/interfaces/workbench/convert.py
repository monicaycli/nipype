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


class CiftiToNiftiInputSpec(CommandLineInputSpec):
    in_file = File(
        exists=True,
        mandatory=True,
        argstr="%s",
        position=0,
        desc="the input cifti file")
    out_file = File(
        name_source=["in_file"],
        name_template="%s.nii.gz",
        keep_extension=False,
        argstr="%s",
        position=1,
        desc="the output nifti file")

class CiftiToNiftiOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc="the output nifti file")


class CiftiToNifti(WBCommand):
    """
    Convert a CIFTI file to NIFTI

   
    """
    input_spec = CiftiToNiftiInputSpec
    output_spec = CiftiToNiftiOutputSpec
    _cmd = 'wb_command -cifti-convert -to-nifti'

    def _format_arg(self, opt, spec, val):
        return super(CiftiToNifti, self)._format_arg(opt, spec, val)

    def _list_outputs(self):
        outputs = super(CiftiToNifti, self)._list_outputs()
        return outputs

class NiftiToCiftiInputSpec(CommandLineInputSpec):
    in_file = File(
        exists=True,
        mandatory=True,
        argstr="%s",
        position=0,
        desc="the input nifti file")
    cifti_template = File(
        exists=True,
        mandatory=True,
        argstr="%s",
        position=1,
        desc="a cifti file with the dimension(s) and mapping(s) that should be used")
    out_file = File(
        name_source=["in_file"],
        name_template="%s.nii",
        keep_extension=False,
        argstr="%s",
        position=2,
        desc="the output cifti file")

class NiftiToCiftiOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc="the output nifti file")


class NiftiToCifti(WBCommand):
    """
    Convert a NIFTI file to CIFTI

   
    """
    input_spec = NiftiToCiftiInputSpec
    output_spec = NiftiToCiftiOutputSpec
    _cmd = 'wb_command -cifti-convert -from-nifti'

    def _format_arg(self, opt, spec, val):
        return super(NiftiToCifti, self)._format_arg(opt, spec, val)

    def _list_outputs(self):
        outputs = super(NiftiToCifti, self)._list_outputs()
        return outputs


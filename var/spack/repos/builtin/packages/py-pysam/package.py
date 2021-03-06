# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPysam(PythonPackage):
    """A python module for reading, manipulating and writing genomic data
       sets."""

    homepage = "https://pypi.python.org/pypi/pysam"
    url      = "https://github.com/pysam-developers/pysam/archive/v0.14.1.tar.gz"

    version('0.14.1', 'ad88fa5bbcc0fdf4a936734691d9c9d1')
    version('0.13', 'a9b502dd1a7e6403e35e6972211688a2')
    version('0.11.2.2', '56230cd5f55b503845915b76c22d620a')
    version('0.7.7', 'eaf9f37cbccc5e2708754d045909c1a0')

    depends_on('py-setuptools', type='build')
    depends_on('py-cython@0.21:', type='build')
    depends_on('curl')
    depends_on('bcftools')
    depends_on('htslib')
    depends_on('samtools')

    depends_on('htslib@:1.6', when='@:0.13')

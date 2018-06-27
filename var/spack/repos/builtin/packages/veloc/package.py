##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Veloc(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/ECP-VeloC/VELOC"
    url      = "https://github.com/ECP-VeloC/VELOC/archive/veloc-1.0rc1.zip"
    tags     = ['ecp']

    version('1.0rc1', 'c6db0de56b5b865183b1fa719ac74c1d')
    version('master', git='https://github.com/ecp-veloc/veloc.git',
            branch='master')

    depends_on('boost~atomic~chrono~clanglibcpp~date_time~debug~exception'
               '~filesystem~graph~icu~iostreams~locale~log~math~mpi'
               '~multithreaded~numpy~program_options~python~random~regex'
               '~serialization~shared~signals~singlethreaded~system'
               '~taggedlayout~test~thread~timer~versionedlayout~wave')
    depends_on('libpthread-stubs')
    depends_on('mpi')
    depends_on('er')
    depends_on('axl')
    depends_on('cmake@3.9:', type='build')

    def cmake_args(self):
        args = []
        args.append("-DWITH_AXL_PREFIX=%s" % self.spec['axl'].prefix)
        args.append("-DWITH_ER_PREFIX=%s" % self.spec['er'].prefix)
        args.append("-DBOOST_ROOT=%s" % self.spec['boost'].prefix)

        # requires C++11
        if 'CXXFLAGS' in env and env['CXXFLAGS']:
            env['CXXFLAGS'] += ' ' + self.compiler.cxx11_flag
        else:
            env['CXXFLAGS'] = self.compiler.cxx11_flag

        return args

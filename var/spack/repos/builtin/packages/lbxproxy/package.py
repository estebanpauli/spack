# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Lbxproxy(AutotoolsPackage):
    """lbxproxy accepts client connections, multiplexes them over a single
    connection to the X server, and performs various optimizations on the
    X protocol to make it faster over low bandwidth and/or high latency
    connections.

    Note that the X server source from X.Org no longer supports the LBX
    extension, so this program is only useful in connecting to older
    X servers."""

    homepage = "http://cgit.freedesktop.org/xorg/app/lbxproxy"
    url      = "https://www.x.org/archive/individual/app/lbxproxy-1.0.3.tar.gz"

    version('1.0.3', '50a2a1ae15e8edf7582f76bcdf6b8197')

    depends_on('libxext')
    depends_on('liblbxutil')
    depends_on('libx11')
    depends_on('libice')

    depends_on('xtrans', type='build')
    depends_on('xproxymanagementprotocol', type='build')
    depends_on('bigreqsproto', type='build')
    depends_on('pkgconfig', type='build')
    depends_on('util-macros', type='build')

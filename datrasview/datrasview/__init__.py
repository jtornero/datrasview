# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DATRASView
                                 A QGIS plugin
 Download LFD data from ICES DATRAS 
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-05-30
        copyright            : (C) 2018 by Jorge Tornero, Fran Velasco, Instituto Español de Oceanografía
        email                : jorge.tornero@ieo.es
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load DATRASView class from file DATRASView.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .datrasview import DATRASView
    return DATRASView(iface)

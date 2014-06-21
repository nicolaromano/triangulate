#!/usr/bin/env python
'''
Copyright (C) 2014 Nicola Romano', romano.nicola@gmail.com

version 0.2
	0.2: Added code for rect and paths. Lines now point to path code.
	0.1: first version. Functions for drawing lines and text

------------------------------------------------------------------------
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
------------------------------------------------------------------------

'''

import inkex, simpletransform, simplestyle

def draw_SVG_line(x1, y1, x2, y2, style, parent):
	line = draw_SVG_path([(x1, y1), (x2, y2)], 0, style, parent)
	return line

def draw_SVG_path(points, closed, style, parent):
	pathdesc = "M "
	for p in points:
		pathdesc = pathdesc + str(p[0]) + "," + str(p[1]) + " "
	if closed == 1:
		pathdesc = pathdesc + "Z"

	attribs = {
		'style' : simplestyle.formatStyle(style),
		'd' : pathdesc
		}
	
	path = inkex.etree.SubElement(parent, inkex.addNS('path','svg'), attribs)
	return path

def draw_SVG_text(x, y, text, parent, style, angle=0):
	attribs = {
		'style' : simplestyle.formatStyle(style),
		'x' : str(x),
		'y' : str(y)
		}

	# Generate text
	txt = inkex.etree.SubElement(parent, inkex.addNS('text'), attribs)
	txt.text = text
	# Rotate (if needed)
	# We need to rotate around the text center.
	# To achieve this we move it to the origin, rotate it and then translate it back
	rotmatrix = simpletransform.parseTransform('translate('+str(x)+','+str(y)+')'+
										' rotate('+str(angle)+')'+
										' translate('+str(-x)+','+str(-y)+')')
	simpletransform.applyTransformToNode(rotmatrix, txt)
	return txt

def draw_SVG_rect(x0, y0, x1, y1, style, parent):
	attribs = {
		'style' : simplestyle.formatStyle(style),
		'x' : str(min(x0, x1)),
		'y' : str(min(y0, y1)),
		'width' : str(abs(x1-x0)),
		'height' : str(abs(y1-y0))
		}
	
	rect = inkex.etree.SubElement(parent, inkex.addNS('rect','svg'), attribs)
	return rect

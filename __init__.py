# ##### BEGIN GPL LICENSE BLOCK #####
#
#  Floor Generator, a Blender addon
#  (c) 2013,2015,2016 Michel J. Anders (varkenvarken)
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Floor Generator",
    "author": "Michel Anders (varkenvarken) with contributions from Alain, Floric ,Lell and Marek Moravec. The idea to add patterns is based on Cedric Brandin's (clarkx) parquet addon",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh",
    "description": "Adds a mesh representing floor boards (planks)",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Add Mesh"
    }

from . import auto_load

auto_load.init()

def register():
    auto_load.register()

def unregister():
    auto_load.unregister()

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse

from qgis.core import (
    QgsApplication,
    QgsProject,
    QgsMapLayer,
    QgsOfflineEditing,
)

parser = argparse.ArgumentParser()

parser.add_argument("db", help="DB Name")
parser.add_argument("schema", help="DB Schema")
parser.add_argument("project", help="Project name")

args = parser.parse_args()

PROJECT_NAME            = args.project
SOURCE_DB_NAME          = args.db
SOURCE_DB_SCHEMA        = args.schema
SOURCE_PROJECT_PATH     = f'postgresql://docker:docker@192.168.1.5:5432?sslmode=disable&dbname={SOURCE_DB_NAME}&schema={SOURCE_DB_SCHEMA}&project={PROJECT_NAME}'
OFFLINE_PROJECT_PATH    = f'./{PROJECT_NAME}.qgs'
OFFLINE_DATA_PATH       = './'
OFFLINE_DB_FILE         = f'{PROJECT_NAME}-offline_db.gpkg'

def isVector(layer):
    return layer.type() == QgsMapLayer.VectorLayer


def isNotTemp(layer):
    return not layer.isTemporary()

# QgsApplication.setPrefixPath("/path/to/qgis/installation", True)

qgs = QgsApplication([], False)
qgs.initQgis()

project = QgsProject.instance()

project.read(SOURCE_PROJECT_PATH)

project.write(OFFLINE_PROJECT_PATH)

layers = [l for l in project.mapLayers().values()]

vectorLayers = filter(isVector, layers)

notTempLayers = filter(isNotTemp, vectorLayers)

ids = [l.id() for l in notTempLayers]

# print(ids)

offlineEditing = QgsOfflineEditing()

offlineEditing.convertToOfflineProject(OFFLINE_DATA_PATH, OFFLINE_DB_FILE, ids, False, QgsOfflineEditing.GPKG)

qgs.exitQgis()
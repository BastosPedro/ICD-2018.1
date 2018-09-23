#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 20:20:22 2018

@author: pedro
"""
import folium as fo

m = fo.Map(
        location = [-9.66625,  -35.7351],
        #tiles = 'Bacias Hidrograficas AL',
        zoom_start = 2
        )

fo.GeoJson(
            'http://dados.al.gov.br/dataset/104be3f2-e942-43ea-bdde-afb660a32a6f/resource/650dddab-74af-454b-bb34-495c66798dd7/download/regioeshidrograficas.geojson',
            name='bacias hidrograficas al',
        ).add_to(m)

m.save('mapinha.html')
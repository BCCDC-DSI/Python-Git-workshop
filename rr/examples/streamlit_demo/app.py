#    Copyright 2024 lisatwyw Lisa Y.W. Tang
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import folium, geopy
import streamlit as st
from branca.element import Figure

def map_loc( address ):
  '''
  Creates a map
  '''

  geolocator = geopy.geocoders.Nominatim(user_agent="3")
  location = geolocator.geocode( address )         
  lx,ly=location.longitude, location.latitude

  fig = Figure( width=400,height=200)
  a_map = folium.Map(location = [lx,ly], zoom_start = 16)
  
  p  = geopy.point.Point(lx, ly)
  
  gl = geopy.geocoders.Nominatim(user_agent="my_test") # Without the user_agent it raises a ConfigurationError.
  site = gl.reverse(p)
  site_name = site[0]
  folium.Marker( location=[lx, ly], popup='Default popup Marker3',tooltip=site_name).add_to(m)
  fig.add_child(a_map)
  
  return fig, a_map, site_name

try:
  address = 'Cactus Club, Downtown'
  fig, a_map, site_name = map_loc(address)
except Exception as e:
  print( e ) 

st.title( 'My first web app' )
st.header( 'My favourite restaurant' )
st.markdown("# Top heading")
st.markdown("## Subheading")
st.read_markdown_file( 'readme.md' )
st.st_folium( a_map )

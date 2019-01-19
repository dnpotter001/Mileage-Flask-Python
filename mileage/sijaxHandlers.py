import os
from flask import Flask, g
import flask_sijax
from mileage import pyrow

class ErgHandler(object):

  @staticmethod
  def checkForErgs(obj_response):
    ergs = list(pyrow.find())

    if len(ergs) == 0:
      obj_response.html_append('#ergSideBar', '<h1>No ergs found</h1>')
    else:
      obj_response.html_append('#ergSideBar', f'<h1> {len(ergs)} erg found')
      for erg in ergs:
        erg = pyrow.pyrow(erg)
        ergData = erg.get_erg()
        obj_response.html_append('#ergSideBar', str(ergData))
        obj_response.html_append('#ergSideBar', f"""
        <ul>
          <li><b>Serial: </b> { ergData['serial'] } </li>
          <li><b>Model</b>: PM{ ergData['model'] } </li>
          <li><b>Status</b>: { ergData['status'] } </li>
          <li><b>Software Version</b>: { ergData['swversion'] }<li>
        </ul>""")



# if len(ergs) == 0:
#   isConnected = False
#   ergData = []
# else:
#   isConnected = True
#   for erg in ergs:
#     erg = pyrow.pyrow(erg)
#     ergData = [{'serial': 123},{'serial': 3857345}]
#     ergData.append(erg.get_erg())

# ergConnection = {
#   "connected": isConnected,
#   "count": len(ergData),
#   "ergData": ergData,
# }
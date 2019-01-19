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

        obj_response.html_append('#ergSideBar', f"""
        <ul>
          <li><b>Serial: </b> { ergData['serial'] } </li>
          <li><b>Model</b>: PM{ ergData['model'] } </li>
          <li><b>Status</b>: { ergData['status'] } </li>
          <li><b>Software Version</b>: { ergData['swversion'] }</li>
        </ul>""")


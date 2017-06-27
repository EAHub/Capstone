from flask import Flask, render_template, request, redirect, url_for
from pandas import DataFrame, to_datetime
import pandas as pd
import numpy as np
import json
import requests
import time
import datetime
from bokeh.plotting import figure, output_file, show
from bokeh import embed
from bokeh.charts import TimeSeries, show, output_file
from bokeh.layouts import column
from bokeh.resources import CDN
from bokeh.embed import components
import os
import cgi



app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/Page1')

@app.route('/Page1', methods=['GET','POST'])
def Page1():
  return render_template('Page1.html')


@app.route('/Page2', methods=['GET', 'POST'])
def Page2():
	return render_template('Page2.html')

if __name__ == '__main__':
  app.run(port=33507)

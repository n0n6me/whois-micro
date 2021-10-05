from flask import Flask, jsonify, make_response
from datetime import date, datetime
import os
import whois
import json

app = Flask(__name__)

@app.route("/")
def index():
    return "whois simple json api"

@app.route('/<domain>')
def get_whois(domain):
  try:
    domain = whois.whois(domain)
    if isinstance(domain.creation_date, (datetime, date)):
      domain_creation_date = domain.creation_date.isoformat()
    else:
      domain_creation_date = domain.creation_date
    if isinstance(domain.expiration_date, list):
      domain.expiration_date = domain.expiration_date[0]
    if isinstance(domain.expiration_date, (datetime, date)):
      domain_expiration_date = domain.expiration_date.isoformat()
    else:
      domain_expiration_date = domain.expiration_date
    if domain.org is None:
      domain.org = domain.registrant_organization
    if isinstance(domain.status, list):
      domain.status = domain.status[0]
    return jsonify(
      query = 'ok',
      domain_name = domain.domain_name,
      creation_date = domain_creation_date,
      expiration_date = domain_expiration_date,
      status = domain.status,
      org = domain.org,
      registrar = domain.registrar,
      )
  except Exception:
      return make_response('', 500)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

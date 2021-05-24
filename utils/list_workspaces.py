#!/usr/bin/env python3
import requests
import os
import json
import sys
import hcl
import subprocess
from jinja2 import Template


from tfe.core.organization import Organization
from tfe.core import session


def tfe_token(tfe_api, config):
    with open(sanitize_path(config), 'r') as fp:
        obj = hcl.load(fp)
    return obj.get('credentials').get(tfe_api).get('token')

def sanitize_path(config):
    path = os.path.expanduser(config)
    path = os.path.expandvars(path)
    path = os.path.abspath(path)
    return path
 
def main(tfe_api, tfe_org):
    tkn = tfe_token(tfe_api, 
        os.path.join(
            os.environ.get("HOME"), 
            ".terraformrc"
        )
    )
    session.TFESession("https://{0}".format(tfe_api), tkn)
    org = Organization(tfe_org)

    with open(os.path.join(os.path.dirname(__file__), "templates/workspace.tpl"), "r") as ws_template:
        t = Template(ws_template.read())

    ws = org.workspaces()
    tf_dir = os.path.expandvars(os.path.join(os.path.dirname(__file__), os.pardir))
    try:
        os.unlink(os.path.join(tf_dir, "./tfmod/workspace_list.tf"))
    except FileNotFoundError:
        pass # no worries if that file isn't there

    for x in sorted(ws, key=lambda ws: ws.name):
        with open(os.path.join(tf_dir, "./tfmod/workspace_list.tf"), "a") as tf:
            tf.write(
                t.render(
                    workspace=x
                )
            )
            tf.write("\n")

if __name__ == "__main__":
    from optparse import OptionParser
    p = OptionParser()
    p.add_option("-a", dest="tfe_api")
    p.add_option("-o", dest="tfe_org")
    opt, arg = p.parse_args()
    main(opt.tfe_api, opt.tfe_org)
from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
from models import Question

bp = Blueprint('intro', __name__, url_prefix='/')

@bp.route('/')
def main():
    return render_template('intro.html')

@bp.route('/linux')
def linux():
    return render_template('notion/linux.html')

@bp.route('/aws')
def aws():
    return render_template('notion/aws.html')

@bp.route('/docker')
def docker():
    return render_template('notion/docker.html')

@bp.route('/kubernetes')
def kubernetes():
    return render_template('notion/kubernetes.html')

@bp.route('/cicd')
def cicd():
    return render_template('notion/cicd.html')
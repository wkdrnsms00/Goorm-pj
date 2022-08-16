from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
from models import Question

bp = Blueprint('main', __name__, url_prefix='/main')

@bp.route('/kk')
def index():
    return redirect(url_for('question._list'))

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)
from flask import render_template, redirect, url_for, flash, url_for, request
from app.auth import bp
from app.auth.forms import SearchForm
import json
import requests

@bp.route('/',methods=['GET','POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        queries = form.search_input.data.split(',')
        query_responses = {}
        for query in queries:
            processed_query = query.strip()
            response = requests.get(f'https://elasticsearch.frendy.in/pulldata/query_es?user_text={processed_query}')
            product_ids = json.loads(response.content)['data']['product_ids'].split(',')
            query_responses[processed_query] = product_ids
        return render_template('new_result.html',query_responses=query_responses)
    return render_template('index.html',title='Search Page Prototype',form=form)
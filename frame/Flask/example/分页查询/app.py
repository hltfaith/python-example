#!usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, render_template, request
from page_utils import Pagination
app = Flask(__name__)
 
@app.route('/test')
def test():
    li = []
    for i in range(1, 100):
        li.append(i)
    pager_obj = Pagination(request.args.get("page", 1), len(li), request.path, request.args, per_page_count=10)
    print(request.path)
    print(request.args)
    index_list = li[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    return render_template("obj/test.html", index_list=index_list, html=html)
 
if __name__ == '__main__':
    app.run(debug=True)

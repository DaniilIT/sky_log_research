from pathlib import Path
from flask import Flask, request, abort
from utils import build_query


DATA_DIR = 'data'


app = Flask(__name__)


@app.route('/perform_query', methods=['POST'])
def perform_query():
    file_name = request.form.get('file_name')
    cmd_1 = request.form.get('cmd_1')
    val_1 = request.form.get('val_1')
    cmd_2 = request.form.get('cmd_2')
    val_2 = request.form.get('val_2')
    if not (cmd_1 and val_1 and file_name):
        abort(400)

    file_path = Path.cwd().joinpath(DATA_DIR, file_name)
    if not file_path.exists():
        return abort(400, 'Wrong file_path')

    with open(file_path) as file:
        result = build_query(cmd_1, val_1, file)
        if cmd_2 and val_2:
            result = build_query(cmd_2, val_2, result)
        result = '\n'.join(result)

    return app.response_class(result, content_type='text/plain')


if __name__ == '__main__':
    app.run(debug=True)

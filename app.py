import os
# тест

from flask import Flask, request, jsonify

from functions import function_to_filter

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['POST'])
def perform_query():
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат
    # return app.response_class('', content_type="text/plain")
    data = request.json
    with open(data["file_name"]) as file:
        result = function_to_filter(
            value=data["value1"],
            data=file.readlines()
        )
        return jsonify(result)

    # Проверить валидность данных [map, limit....] и значение
    # Отдельно проверить имя файла

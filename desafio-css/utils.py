import json

def extract_route(request):
    return request.split(' ')[1][1:]

def read_file(path):
    return open(path, 'r+b').read()

def load_data(file):
    return json.loads(read_file(f"data/{file}"))

def load_template(file):
    return open(f"desafio-css/docs/{file}", 'r', encoding='utf-8').read()

def add_note(note):
    lista = load_data('notes.json')
    lista.append(note)
    with open('data/notes.json', 'w', encoding='utf-8') as doc:
        lista = json.dumps(lista, ensure_ascii=False, indent=4)
        doc.write(lista)

def build_response(body='', code=200, reason='OK', headers=''):
    if headers == '':
        response = 'HTTP/1.1 ' + str(code) + ' ' + reason + headers + '\n\n' + body
    else:
        response = 'HTTP/1.1 ' + str(code) + ' ' + reason + '\n' + headers + '\n\n' + body
    return response.encode()
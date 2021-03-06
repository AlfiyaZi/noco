from collections import OrderedDict


class HTML2VECConverter:
    HTML2VEC_DIRECTION = 0
    VEC2HTML_DIRECTION = 1

    html_int_map = {
        '/>': 1,
        '>': 2,
        '<body': 3,
        '</body>': 4,
        '<input': 5,
        '</input>': 6,
        '<table': 7,
        '</table>': 8,
        '<div': 9,
        '</div>': 10,
        '<p': 11,
        '</p>': 12,
        '<button': 13,
        '</button>': 14,
        'class=': 15,
        '<head': 16,
        '</head>': 17,
        '<html': 18,
        '</html>': 19,
        '<li': 20,
        '</li>': 21,
        '<ul': 22,
        '</ul>': 23,
        '<ol': 24,
        '</ol>': 25,
        '<tr': 26,
        '</tr>': 27,
        '<td': 28,
        '</td>': 29,
        '<link': 30,
        '</link>': 31,
        '<textarea': 32,
        '</textarea>': 33
    }

    def __init__(self):
        self.html_int_map = OrderedDict(sorted(self.html_int_map.items(), key=lambda x: x[1]))

    def _clear_data(self, data):
        return data.replace('\n', '')

    def _get_next_item(self, data):
        origin_data = data[::]
        while data:
            for k, v in self.html_int_map.items():
                if data.startswith(k):
                    return k, data[len(k):]
            data = data[1:]
        return None, origin_data

    def split_html(self, data):
        result = []
        html = self._clear_data(data[::])
        while html:
            node, new_html = self._get_next_item(html)
            if node:
                result.append(node)
                html = new_html
        return result

    def convert(self, data, direction=HTML2VEC_DIRECTION):
        if direction == self.HTML2VEC_DIRECTION:
            result = [self.html_int_map[node] for node in self.split_html(data)]
        elif direction == self.VEC2HTML_DIRECTION:
            reversed_map = {v:k for k,v in self.html_int_map.items()}
            result = ''.join([reversed_map[num] for num in data])
        return result

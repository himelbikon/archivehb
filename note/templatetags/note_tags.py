from django import template

register = template.Library()

@register.filter
def table_tag_adder(topic):
    contents = list(map(striper, topic.content.split('*')))
    table = '<table> <tr> <th> ''' + topic.caption + ' </th> </tr> '
    for content in contents[1:]:
        table += '<tr><td>* ' + content + '</td></tr>'
    table+= '</table>'
    return table

def striper(x):
    return x.strip()

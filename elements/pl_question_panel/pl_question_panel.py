import prairielearn as pl
import lxml.html


def prepare(element_html, element_index, data):
    element = lxml.html.fragment_fromstring(element_html)
    pl.check_attribs(element, required_attribs=[], optional_attribs=[])
    

def render(element_html, element_index, data):
    if data['panel'] == 'question':
        element = lxml.html.fragment_fromstring(element_html)
        return pl.inner_html(element)
    else:
        return ''

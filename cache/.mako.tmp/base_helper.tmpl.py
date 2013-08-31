# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1377941778.860656
_enable_loop = True
_template_filename = u'/usr/local/lib/python2.7/dist-packages/nikola/data/themes/base/templates/base_helper.tmpl'
_template_uri = u'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_head', 'html_translations', 'html_navigation_links', 'html_social', 'late_load_js', 'html_sidebar_links']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 41
        __M_writer(u'\n\n')
        # SOURCE LINE 44
        __M_writer(u'\n\n')
        # SOURCE LINE 48
        __M_writer(u'\n\n<!--FIXME: remove in v7 -->\n')
        # SOURCE LINE 53
        __M_writer(u'\n\n')
        # SOURCE LINE 76
        __M_writer(u'\n\n\n')
        # SOURCE LINE 85
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_head(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        favicons = context.get('favicons', UNDEFINED)
        description = context.get('description', UNDEFINED)
        title = context.get('title', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        blog_author = context.get('blog_author', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        len = context.get('len', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n    <meta charset="utf-8">\n    <meta name="description" content="')
        # SOURCE LINE 4
        __M_writer(unicode(description))
        __M_writer(u'" >\n    <meta name="author" content="')
        # SOURCE LINE 5
        __M_writer(unicode(blog_author))
        __M_writer(u'">\n    <title>')
        # SOURCE LINE 6
        __M_writer(filters.html_escape(unicode(title)))
        __M_writer(u' | ')
        __M_writer(filters.html_escape(unicode(blog_title)))
        __M_writer(u'</title>\n    ')
        # SOURCE LINE 7
        __M_writer(unicode(mathjax_config))
        __M_writer(u'\n')
        # SOURCE LINE 8
        if use_bundles:
            # SOURCE LINE 9
            if use_cdn:
                # SOURCE LINE 10
                __M_writer(u'            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
                # SOURCE LINE 11
            else:
                # SOURCE LINE 12
                __M_writer(u'            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
                pass
            # SOURCE LINE 14
        else:
            # SOURCE LINE 15
            __M_writer(u'        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css"/>\n')
            # SOURCE LINE 18
            if has_custom_css:
                # SOURCE LINE 19
                __M_writer(u'            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
                pass
            pass
        # SOURCE LINE 22
        __M_writer(u'    <!--[if lt IE 9]>\n      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js" type="text/javascript"></script>\n    <![endif]-->\n')
        # SOURCE LINE 25
        if rss_link:
            # SOURCE LINE 26
            __M_writer(u'        ')
            __M_writer(unicode(rss_link))
            __M_writer(u'\n')
            # SOURCE LINE 27
        else:
            # SOURCE LINE 28
            if len(translations) > 1:
                # SOURCE LINE 29
                for language in translations:
                    # SOURCE LINE 30
                    __M_writer(u'                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(unicode(language))
                    __M_writer(u')" href="')
                    __M_writer(unicode(_link('rss', None, language)))
                    __M_writer(u'">\n')
                    pass
                # SOURCE LINE 32
            else:
                # SOURCE LINE 33
                __M_writer(u'            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(unicode(_link('rss', None)))
                __M_writer(u'">\n')
                pass
            pass
        # SOURCE LINE 36
        if favicons:
            # SOURCE LINE 37
            for name, file, size in favicons:
                # SOURCE LINE 38
                __M_writer(u'            <link rel="')
                __M_writer(unicode(name))
                __M_writer(u'" href="')
                __M_writer(unicode(file))
                __M_writer(u'" sizes="')
                __M_writer(unicode(size))
                __M_writer(u'"/>\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 79
        __M_writer(u'\n')
        # SOURCE LINE 80
        for langname in translations.keys():
            # SOURCE LINE 81
            if langname != lang:
                # SOURCE LINE 82
                __M_writer(u'            <a href="')
                __M_writer(unicode(_link("index", None, langname)))
                __M_writer(u'">')
                __M_writer(unicode(messages("LANGUAGE", langname)))
                __M_writer(u'</a>\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        tuple = context.get('tuple', UNDEFINED)
        navigation_links = context.get('navigation_links', UNDEFINED)
        rel_link = context.get('rel_link', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 55
        __M_writer(u'\n')
        # SOURCE LINE 56
        for url, text in navigation_links[lang]:
            # SOURCE LINE 57
            if isinstance(url, tuple):
                # SOURCE LINE 58
                __M_writer(u'            <li> ')
                __M_writer(unicode(text))
                __M_writer(u'\n            <ul>\n')
                # SOURCE LINE 60
                for suburl, text in url:
                    # SOURCE LINE 61
                    if rel_link(permalink, suburl) == "#":
                        # SOURCE LINE 62
                        __M_writer(u'                    <li class="active"><a href="')
                        __M_writer(unicode(suburl))
                        __M_writer(u'">')
                        __M_writer(unicode(text))
                        __M_writer(u'</a>\n')
                        # SOURCE LINE 63
                    else:
                        # SOURCE LINE 64
                        __M_writer(u'                    <li><a href="')
                        __M_writer(unicode(suburl))
                        __M_writer(u'">')
                        __M_writer(unicode(text))
                        __M_writer(u'</a>\n')
                        pass
                    pass
                # SOURCE LINE 67
                __M_writer(u'            </ul>\n')
                # SOURCE LINE 68
            else:
                # SOURCE LINE 69
                if rel_link(permalink, url) == "#":
                    # SOURCE LINE 70
                    __M_writer(u'                <li class="active"><a href="')
                    __M_writer(unicode(url))
                    __M_writer(u'">')
                    __M_writer(unicode(text))
                    __M_writer(u'</a>\n')
                    # SOURCE LINE 71
                else:
                    # SOURCE LINE 72
                    __M_writer(u'                <li><a href="')
                    __M_writer(unicode(url))
                    __M_writer(u'">')
                    __M_writer(unicode(text))
                    __M_writer(u'</a>\n')
                    pass
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_social(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 46
        __M_writer(u'\n\t')
        # SOURCE LINE 47
        __M_writer(unicode(social_buttons_code))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 43
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_sidebar_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def html_navigation_links():
            return render_html_navigation_links(context)
        __M_writer = context.writer()
        # SOURCE LINE 51
        __M_writer(u'\n    ')
        # SOURCE LINE 52
        __M_writer(unicode(html_navigation_links()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



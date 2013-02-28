FILEID = 0
POSITION = 1
CODESTR = 2
DEPS = 3
CONTEXT = 4
OPTIONS = 5
SELECTORS = 6
PROPERTIES = 7
PATH = 8
INDEX = 9
LINENO = 10
MEDIA = 11
EXTENDS = 12
RULE_VARS = {
    'FILEID': FILEID,
    'POSITION': POSITION,
    'CODESTR': CODESTR,
    'DEPS': DEPS,
    'CONTEXT': CONTEXT,
    'OPTIONS': OPTIONS,
    'SELECTORS': SELECTORS,
    'PROPERTIES': PROPERTIES,
    'PATH': PATH,
    'INDEX': INDEX,
    'LINENO': LINENO,
    'MEDIA': MEDIA,
    'EXTENDS': EXTENDS,
}


def spawn_rule(from_rule=None, **kwargs):
    if from_rule is None:
        rule = SassRule()
    else:
        rule = from_rule.copy()

    for k, v in kwargs.items():
        rule[RULE_VARS[k.upper()]] = v

    return rule


class SassRule(object):
    """At its heart, a CSS rule: combination of a selector and zero or more
    properties.  But this is Sass, so it also tracks some Sass-flavored
    metadata, like `@extend` rules and `@media` nesting.
    """

    def __init__(self, file_id=None, position=None, unparsed_contents=None, dependent_rules=None,
            context=None, options=None, selectors=frozenset(), properties=None,
            path='./', index=None, lineno=0, media=None, extends_selectors=frozenset()):

        self.file_id = file_id
        self.position = position
        self.unparsed_contents = unparsed_contents
        self.context = context
        self.options = options
        self.selectors = selectors
        self.path = path
        self.lineno = lineno
        self.media = media
        self.extends_selectors = extends_selectors

        if dependent_rules is None:
            self.dependent_rules = set()
        else:
            self.dependent_rules = dependent_rules

        if properties is None:
            self.properties = []
        else:
            self.properties = properties

        if index is None:
            self.index = {0: '<unknown>'}
        else:
            self.index = index

    def copy(self):
        return type(self)(
            file_id=self.file_id,
            position=self.position,
            unparsed_contents=self.unparsed_contents,
            #deps=set(self.deps),
            dependent_rules=self.dependent_rules,
            context=self.context,
            options=self.options,
            selectors=self.selectors,
            #properties=list(self.properties),
            properties=self.properties,
            path=self.path,
            #index=dict(self.index),
            index=self.index,
            lineno=self.lineno,
            media=self.media,
            extends_selectors=self.extends_selectors,
        )



    def __iter__(self):
        raise TypeError


    def __setitem__(self, key, value):
        """Backwards compatibility for the list approach."""
        if key == FILEID:
            self.file_id = value
        elif key == POSITION:
            self.position = value
        elif key == CODESTR:
            self.unparsed_contents = value
        elif key == DEPS:
            self.dependent_rules = value
        elif key == CONTEXT:
            self.context = value
        elif key == OPTIONS:
            self.options = value
        elif key == SELECTORS:
            self.selectors = value
        elif key == PROPERTIES:
            self.properties = value
        elif key == PATH:
            self.path = value
        elif key == INDEX:
            self.index = value
        elif key == LINENO:
            self.lineno = value
        elif key == MEDIA:
            self.media = value
        elif key == EXTENDS:
            self.extends_selectors = value
        else:
            raise KeyError(key)

    def __getitem__(self, key):
        """Backwards compatibility for the list approach."""
        if key == FILEID:
            return self.file_id
        elif key == POSITION:
            return self.position
        elif key == CODESTR:
            return self.unparsed_contents
        elif key == DEPS:
            return self.dependent_rules
        elif key == CONTEXT:
            return self.context
        elif key == OPTIONS:
            return self.options
        elif key == SELECTORS:
            return self.selectors
        elif key == PROPERTIES:
            return self.properties
        elif key == PATH:
            return self.path
        elif key == INDEX:
            return self.index
        elif key == LINENO:
            return self.lineno
        elif key == MEDIA:
            return self.media
        elif key == EXTENDS:
            return self.extends_selectors
        else:
            raise KeyError(key)
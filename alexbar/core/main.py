import re    

# -----------------------------------------------

INPUT = "./convertor/tmp.txt"
OUTPUT = "./templates/core/posts/tmp.html"

PATTERNS = [
(r'h:(.*?);', lambda content: f"""
<div class="header" style="height: fit-content; ">
    <img src="{{% static 'core/img/posts/{content}' %}}" style="width: 100%; border-radius: 6px;">
</div>"""),

(r'in:', lambda content: f"""
<div class="in-post">"""),
(r':in;', lambda content: f"""</div>"""),

(r'vert:', lambda content: f"""
    <div class="vert10">"""),
(r':vert;', lambda content: f"""    </div>"""),

(r't:(.*?);', lambda content: f"""        <div class="h1">
            <h1 class="h1">{content}</h1>
        </div>"""),

(r'd:(.*?);', lambda content: f"""        <div class="r3">
            <h3>{content}</h3>
        </div>"""),

(r'sep;', lambda content: f"""
    <div class="separator long-separator"></div>
"""),

(r's:(.*?);', lambda content: f"""    <div class="span"><span>{content}</span></div>"""),

(r'p:(.*?);', lambda content: f"""    <div class="p">
        <p>
            {content}
        </p>
    </div>"""),

(r'hor:', lambda content: f"""    <div class="hor">"""),
(r':hor;', lambda content: f"""    </div>"""),

(r'cen-title:', lambda content: f"""    <div class="cen">"""),
(r':cen-title;', lambda content: f"""    </div>"""),

(r'img-set:', lambda content: f"""<div class="cen">
    <div class="img6">"""),
(r'img:(.*?);', lambda content: f"""        <img src="{{% static 'core/img/posts/{content}' %}}" style="width: 50dvw; border-radius: 6px;">"""),
(r':img-set;', lambda content: f"""    </div>
</div>"""),

(r'n:(.*?);', lambda content: f"""        <h2>{content}</h2>"""),

(r'a:(.*?);', lambda content: f"""        <audio controls>
            <source src="{{% static 'core/audio/{content}' %}}">
        </audio>"""),

(r'sp;', lambda content: f"""
        <div class="space"></div>
"""),

(r'gif:(.*?);', lambda content: f"""
<div class="in-post">
    <div class="vert">   
        <div class="cen">
            <div class="space"></div>
            <img style="width: 50%; border-radius: 6px;" src="{{% static 'core/img/posts/{content}' %}}">
            <div class="space"></div>
        </div>
    </div>
</div>
"""),
]


# -----------------------------------------------


def read_input():
    with open(INPUT, 'r') as f:
        return f.read()
    
def pattern_to_matches(pattern, input_text):
    new_pattern = rf'{pattern}'
    matches = re.findall(new_pattern, input_text)
    return matches




def convert_to_html(input_text):
    html_output = [
        "{% extends 'core/base.html' %}",
        "{% load static %}",
        "",
        "{% block content %}",
        "<!-- CONTENT -->"
    ]

    matches = []
    for pattern, formatter in PATTERNS:
        for match in re.finditer(pattern, input_text):
            context = match.group(1) if len(match.groups()) > 0 else ''
            matches.append((match.start(), formatter(context)))

    matches.sort(key=lambda x: x[0])

    for _, html_fragment in matches:
        html_output.append(html_fragment)

    html_output.append("{% endblock %}")
    return "\n".join(html_output)


# ------------------------------------------------

# Example usage
# input_text = read_input()
# html_output = convert_to_html(input_text)
# with open(OUTPUT, 'w') as f:
#     f.write(html_output)
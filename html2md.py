import os
import re
from bs4 import BeautifulSoup

# Get the meta data
MD_HEAD = """---
title: {title}
date: {date}
updated: {date}
tags:
{tags}
categories:
- {categories}
---\n
"""

def table_handler(table):
    text = ''
    head = table.find('thead')
    if head:
        text += '| ' + ' | '.join([th.text.strip() for th in head.find_all('th')]) + ' |\n'
        text += '| ' + ' | '.join(['---'] * len(head.find_all('th'))) + ' |\n'
    body = table.find('tbody')
    if body:
        for tr in body.find_all('tr'):
            text += '| ' + ' | '.join([td.text.strip() for td in tr.find_all('td')]) + ' |\n'
    return '\n' + text + '\n'
    # can use prettify() to get the original html and it can be rendered by the markdown
    # return '\n' + table.prettify()

def code_handler(code):
    code_type = re.match(r'<figure class="highlight ([a-z]+)">', str(code))
    if code_type:
        code_type = code_type.group(1)
    else:
        code_type = ''
    lines = code.find_all('span', class_="line")
    code_text = ''
    for line in lines:
        code_text += line.text + '\n'
    text = code_text
    return f'```{code_type}\n{text}```\n'

# Get the content
def paragraph_handler(p):
    if p.name == None:
        return p.string.strip()
    if p.name == 'figure':
        return code_handler(p)
    if p.name in [f'h{i}' for i in range(1, 7)]:
        text = p.text.strip()
        return '#' * int(p.name[1]) + ' ' + text + '\n'
    if p.name == 'table':
        return table_handler(p)
    
    text = ''
    for child in p.children:
        if child.name == None:
            text += child.string.strip()
        elif child.name == 'img':
            if child.get('data-src') and child.get('alt'):
                text += f'![{child["alt"]}]({child["data-src"]})'
        elif child.name == 'strong':
            text += f'**{child.text}**'
        elif child.name == 'em':
            text += f'*{child.text}*'
        elif child.name == 'a':
            if child.get('href'):
                text += f'[{child.text}]({child["href"]})'
        elif child.name == 'br':
            text += '\n'
        elif child.name == 'code':
            text += f'`{child.text}`'
        elif child.name == 'p':
            text += paragraph_handler(child)
        elif child.name == 'span':
            text += child.text
        elif child.name == 'ul' or child.name == 'ol':
            for li in child.find_all('li'):
                text += '- ' + paragraph_handler(li)
        elif child.name == 'li':
            text += paragraph_handler(child)
        elif child.name == 'table':
            text += table_handler(child)
        elif child.name == 'figure':
            text += code_handler(child)
        elif child.name == 'blockquote':
            text += '> ' + child.text.strip() + '\n'
        elif child.name == 'hr':
            text += '---\n'
        elif child.name == 'sub':
            text += f'<sub>{child.text}</sub>'
        elif child.name == 'sup':
            text += f'<sup>{child.text}</sup>'
        elif child.name == 'f1':
            text += f'<font size="1">{child.text}</font>'
        elif child.name == 'thead' or child.name == 'tbody':
            text += child.text
        else:
            print(child.name)
    return text + '\n'

    

def html2md(html_file, md_path):
    soup = BeautifulSoup(open(html_file, encoding='utf-8'), "html.parser")

    # Get the meta data
    post_title = soup.find('div', class_="posttitle").text
    categories = soup.find('a', class_="post-meta__categories").text
    tags = [f'- {tag.text.strip()}' for tag in soup.find_all('a', class_="post-meta__tags")]
    date_pattern = r'(\d{4})-(\d{2})-(\d{2})'
    post_date = soup.find('time', class_="post-meta__date").text
    published_date, updated_date = re.findall(date_pattern, post_date)
    published_date, updated_date = '-'.join(published_date), '-'.join(updated_date)

    # Get the content
    content = soup.find('div', id="post-content")

    # Remove the line number of code block
    lines = content.find_all('span', class_="line")
    for line in lines:
        if re.match(r'\d+', line.text.strip()):
            line.extract()

    # Write the markdown file
    if not os.path.exists(f'{md_path}/{categories}'):
        os.makedirs(f'{md_path}/{categories}')
    
    # Replace the '/' in the title, or it will be recognized as a directory
    if '/' in post_title:
        post_title = post_title.replace('/', '或')
    with open(f'{md_path}/{categories}/{post_title}.md', 'w', encoding='utf-8') as f:
        f.write(MD_HEAD.format(title=post_title, date=published_date, tags='\n'.join(tags), categories=categories))
        for child in content.children:
            f.write(paragraph_handler(child))


if __name__ == '__main__':
    for dirpath, dirnames, filenames in os.walk('./posts'):
        for filename in filenames:
            if filename.endswith('.html'):
                html2md(os.path.join(dirpath, filename), './markdown')

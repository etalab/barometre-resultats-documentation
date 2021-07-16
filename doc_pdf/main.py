import os
import re
from datetime import date
from pathlib import Path

import click
import frontmatter
from emoji import get_emoji_regexp

root_folder = '/'.join(os.path.abspath(__file__).split('/')[:-2])
md_folder = os.path.join(root_folder, 'mesures')
doc_pdf_folder = os.path.join(root_folder, 'doc_pdf')

themes_str_dict = {
    '1-education-jeunesse' : 'Éducation - Jeunesse',
    '2-economie-emploi' : 'Économie - Emploi',
    '3-transition-ecologique' : 'Transition écologique',
    '4-agriculture' : 'Agriculture',
    '5-securite' : 'Sécurité',
    '6-justice' : 'Justice',
    '7-sante-famille-handicap' : 'Santé - Famille - Handicap',
    '8-logement' : 'Logement',
    '9-services-publics-territoires' : 'Services publics - Territoires',
    '10-culture' : 'Culture - Sports'
}

def emojify(string):
    """
    Find emojis in a string and replace them with an
    inline Markdown image to Twemoji.

    Handles multi-character emojis like flags (🇫🇷 = Ⓕ + Ⓡ)
    """
    def replace(match):
        def codepoint(codes):
            # See https://github.com/twitter/twemoji/issues/419#issuecomment-637360325
            if '200d' not in codes:
                return '-'.join([c for c in codes if c != 'fe0f'])
            return '-'.join(codes)
        cdn_fmt = "https://twemoji.maxcdn.com/v/latest/72x72/{codepoint}.png"
        # {:x} gives hex
        url = cdn_fmt.format(
            codepoint=codepoint([f'{ord(c):x}' for c in match.group(0)])
        )
        return f'!["Emoji"]({url}){{width=16 height=16}}'

    return get_emoji_regexp().sub(replace, string)


def clean_lines(lines):
    res = list(lines)

    pattern = re.compile(r'^::: (tip|warning|danger|lexique)(.*)')

    for i, line in enumerate(lines):
        res[i] = emojify(line)

        # Replace VuePress custom containers
        # https://vuepress.vuejs.org/guide/markdown.html#custom-containers
        m = pattern.match(line.strip())
        if m:
            type, title = [e.strip() for e in m.groups()]
            if type == 'lexique':
                title = f"Lexique : {title}"
            res[i] = f"<div class='banner {type}'>\n**{title}**\n\n"

        if line.strip() == ':::':
            res[i] = '</div>\n'

        # Remove VuePress table of contents
        if line.strip() == '[[toc]]':
            res[i] = ''

    return res


def build_metadata():
    date_str = date.today().strftime("%d/%m/%Y")

    return {
        # https://github.com/chdemko/pandoc-latex-environment
        'pandoc-latex-environment': {
            'tip': ['banner', 'tip'],
            'warning': ['banner', 'warning'],
            'danger': ['banner', 'danger'],
            'lexique': ['banner', 'lexique'],
        },
        # https://github.com/Wandmalfarbe/pandoc-latex-template
        'titlepage': "true",
        'toc-own-page': "true",
        'toc-depth' : 2,
        'titlepage-color': "FFFFFF",
        'titlepage-text-color': "0053b3",
        'lang': "fr",
        'title': "Documentation - Baromètre des résultats de l’action publique",
        #'author': "Etalab",
        'date': date_str,
        'footer-center': '\\footnotesize Consultez les données sur \href{https://www.data.gouv.fr/fr/datasets/barometre-des-resultats-de-laction-publique/}{www.data.gouv.fr/fr/datasets/barometre-des-resultats-de-laction-publique/}',
        #'logo': 'logo.png',
        'colorlinks': "true",
        'linkcolor': "etalab-blue",
        'urlcolor': "etalab-blue",
        'numbersections': 'true',
    }


def file_content(f):
    md_content = frontmatter.load(f).content
    lines = f"\n{md_content}\n".split('\n')
    return [f"{l}\n" for l in lines]


@click.command()
@click.argument('output_path')
def main(output_path):
    p = Path(md_folder)

    if Path('./images').exists():
        raise ValueError("images folder already exists. Should not exist for symlinks")
    
    #Creating a dict with appropriate keys to give the correct order for the themes
    themes_dict = {int(theme_md_filename.split('-')[0]) : theme_md_filename for theme_md_filename in os.listdir(md_folder)}
    themes_list = [themes_dict[theme_key] for theme_key in sorted(themes_dict.keys())]

    lines = []

    #Adding first section of README.md as document introduction
    readme_path = os.path.join(root_folder, 'README.md')
    with open(readme_path) as f:
        readme_text = f.read()
        intro_text = '# Introduction : ' + readme_text.split('# ')[1]
        intro_lines = intro_text.splitlines(True)
        lines.extend(intro_lines)

    #Adding mesures texts
    for theme in themes_list :
        
        lines += ['\pagebreak \n']
        for i in range(12) :  #Trick to center title in page
            lines += ['&nbsp;  \n']
            lines += ["\n"]
        lines += ['# ' + themes_str_dict[theme] + '\n']
        lines += ['\pagebreak \n']
        
        files = [p / theme / filename for filename in os.listdir(p / theme)]
        
        for file in files:
            with file.open() as f:
                file_lines = file_content(f)
                corrected_file_lines = []
                for line in file_lines :
                    if line.startswith('#') :
                        corrected_line = '#' + line
                    else :
                        corrected_line = line
                    corrected_file_lines += [corrected_line]
                        
                lines.extend(corrected_file_lines)

    # Create a single file with all content
    metadata = build_metadata()
    content = frontmatter.Post(''.join(clean_lines(lines)), **metadata)
    with open('tmp.md', 'w') as f:
        f.writelines(frontmatter.dumps(content))

    # Build PDF with Pandoc
    os.makedirs(Path(output_path).parent, exist_ok=True)

    os.symlink(p / 'images/', Path('./images'))
    # See https://pandoc.org/MANUAL.html
    # especially "Markdown variants"
    os.system(f'''
    pandoc --toc -s tmp.md -o {output_path} \
      --template "{doc_pdf_folder}/eisvogel.latex" \
      --from markdown+lists_without_preceding_blankline \
      --filter pandoc-latex-environment
    ''')

    # Clean up
    os.unlink(Path('./images'))
    os.remove('tmp.md')

    click.echo(f"PDF file has been generated at {output_path}")

if __name__ == '__main__':
    main()

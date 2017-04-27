def build_md():
    import subprocess

    command = ('pandoc --bibliography scripts/process_publications/ref.bib --csl scripts/process_publications/blog_style.csl '
               '-t markdown_github -s scripts/process_publications/ref_list.md -o scripts/process_publications/tmp.md')
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)


def remove_escapes():

    with open('scripts/process_publications/tmp.md', 'r') as f:
        data = f.read()

    data = data.replace('\\', '')
    data = data.replace('<', '')
    data = data.replace('>', '')

    with open('scripts/process_publications/md_refs.md', 'w') as f:
        f.write(data)


build_md()
remove_escapes()

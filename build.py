# Scan to build pages.json
import pathlib
import json

from markdown import Markdown


index_text = pathlib.Path('index.html').read_text(encoding='utf8')
mdengine = Markdown(extensions = ['meta'])

for dir in pathlib.Path('.').glob('**'):
    (dir/'index.html').write_text(index_text,encoding='utf8')
    result = []
    for file in dir.glob('*.md'):
        mdengine.reset()
        with open(file.parent / (file.name[:-3]+'.html'),'w') as fp:
            fp.write(mdengine.convert(file.read_text(encoding='utf8')))
        meta = mdengine.Meta
        meta['id'] = [file.name[:-3]]
        for key in meta.keys():
            meta[key] = meta[key][0]
        result.append(meta)
    with open(dir/'pages.json','w') as fp:
        json.dump(result, fp)
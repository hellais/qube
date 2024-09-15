import os
import json
import pathlib

from string import Template

import yaml

ROOT = pathlib.Path(os.path.dirname(os.path.realpath(__file__)))

def generate_page(link_id: int, links: str):
    dst_dir = ROOT / "l" / str(link_id)
    dst_dir.mkdir(parents=True, exist_ok=True)
    
    with (ROOT / "redirector_template.html").open("r") as in_file:
        template = in_file.read()

    index = dst_dir / "index.html"
    with index.open("w") as out_file:
        d = {"url_list": ""}
        d["url_list"] = ",\n".join([json.dumps(l) for l in links])
        t = Template(template).substitute(d)
        out_file.write(t)
    print(f"written {index}")

def main():
    with open("links.yml") as in_file:
        link_descriptor = yaml.safe_load(in_file)
        for link_id, links in link_descriptor.items():
            generate_page(link_id, links)

if __name__ == "__main__":
    main()

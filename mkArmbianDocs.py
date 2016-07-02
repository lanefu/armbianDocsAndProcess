#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    Created by Lane Jennison on 2016-02-05.
"""

import sys,os
import fnmatch
import re
import logging as log
import jinja2
from jinja2 import Template, BaseLoader, Environment



def parse_arguments():
    """ Arguments parsing function. """
    import argparse
    parser = argparse.ArgumentParser(description='mkKnowledge script.')
    parser.add_argument('-v', '--verbose', action='store_true', help='increase output verbosity')
    parser.add_argument('-i', '--indir', metavar='INPUT_DIRECTORY', default='./', help='directory containing knowledgebase files')
    parser.add_argument('-o', '--outdir', metavar='OUTPUT_DIRECTORY', default='./', help='directory to store site.xml')

    return parser.parse_args()

#locate markdown files in path and return list
def findFiles(indir):

    assert os.path.isdir(indir), "Provided directory path is not a directory"

    validFileList = list()

    log.info("looking for files in %s", indir)
    #find markdown files
    for file in os.listdir(indir):
        if os.path.isdir(os.path.join(indir,file)):
            log.info("%s is a directory, skipping", file)
        elif fnmatch.fnmatch(file,'*.md'):
            log.info("adding %s as markdown file", file)
            validFileList.append(file)

    return validFileList

#verify file is markdown and extract first heading to use as title
def parseFiles(validFileList, indir):

    assert validFileList, "No valid markdown files to parse"
    assert os.path.isdir(indir), "Provided directory path is not a directory"

    parsedFileList = dict()
    tocregex = re.compile("(?P<parent>(?<=\[)[\w-]+?(?=\]))\]-{1}(?P<child>[\w-].*(?=\.md))")
    mdregex = re.compile("^#{1,2}\s+(?P<title>(\w+( \w+))+)(\s+)?(#{1,2})?$")
##FIXME add Try catch or finaly
    for file in sorted(validFileList):
        filepath = os.path.join(indir,file)
        fp = open(filepath)
        for line in fp:
            log.info("checking file %s and line %s", file, line)
            result = mdregex.match(line)
            if result:
                title = result.group('title')
                log.info("Using title string %s", title)
                parsedFileList[file] = title
                break
        fp.close()
    return parsedFileList

#generte  mkdocs.yml using jinja template and dict of markdown files
def generateSite(parsedFileList):

    mkdocsTemplate = """

site_name: Armbian Documentation

repo_url: https://github.com/lanefu/armbianDocsAndProcess
repo_name: Github

site_author: "Armbian team"

theme: readthedocs

markdown_extensions:
  - smarty
  - footnotes
  - toc:
      permalink: True

pages:
  - Introduction: index.md
  - Knowledge Base:
{% for file, title in kbdict.iteritems() %}    - '{{ title }}' : '{{ file }}'
{% endfor %}

"""
    template = Template(mkdocsTemplate)
    return template.render(kbdict=parsedFileList)

def writeSiteFile(content,outdir):
    assert os.path.isdir(outdir), "Provided output directory path is not a directory"

    file = "mkdocs.yml"
    filepath = os.path.join(outdir,file)
    fp = open(filepath,'w')

    fp.write(content)
    fp.close()
    log.info("%s generated", file)

def main():
    """ Main function. """
    args = parse_arguments()

    if args.verbose:
	log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
	log.info("Verbose output.")
    else:
	log.basicConfig(format="%(levelname)s: %(message)s")


    log.info("mkArmbianDocs version 0.100002, created by Lane Jennison.")

    indir = args.indir
    outdir = args.outdir

    writeSiteFile(generateSite(parseFiles(findFiles(indir),indir)),outdir)


if __name__ == "__main__":
    main()

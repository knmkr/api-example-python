#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests  # pip install requests


def _main():
    token = 'GENOMELINKTEST'
    headers = {'Authorization': 'Bearer {}'.format(token)}

    phenotype = 'eye-color'
    population = 'european'
    report_url = 'https://genomicexplorer.io/v1/reports/{}?population={}'.format(phenotype, population)
    response = requests.get(report_url, headers=headers)
    data = response.json()
    print json.dumps(data)

    chrom = 'chr1'
    start = '100000'
    end = '100500'
    sequence_url = 'https://genomicexplorer.io/v1/genomes/sequence/?region={}:{}-{}'.format(chrom, start, end)
    response = requests.get(sequence_url, headers=headers)
    data = response.json()
    print json.dumps(data)

if __name__ == '__main__':
    _main()

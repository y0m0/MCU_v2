#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# clean_catalog.py
#

from lxml import etree


def clean(catalog_file):
    """
    take a catalog file and remove all
    the unwanted products from it
    """

    stores = { 'Ingen': '0', 'Hovedlager' : '1', 'Caffe Vespa': '4', 'Interlogistik': '8', 'Vectura' : '10' }
    stores_not_allowed = [ stores['Caffe Vespa'], stores['Interlogistik'], stores['Vectura'] ]

    tree = etree.parse(catalog_file)
    root = tree.getroot()

    for g_otemp in root.findall('g_otemp'):
        storeid = g_otemp.find('storeid').text
        prodtype = g_otemp.find('prodtype').text
        prodname = g_otemp.find('desc').text.lower()

    # search for products to be removed from the catalog
        if storeid in stores_not_allowed or prodtype == '(Ingen)' or prodtype == 'Div. bestillingsvarer' or 'oluf' in prodname:
            root.remove(g_otemp)
    # remove product group entry for the alcohol % from the catalog
        if prodtype == 'Alkoholholdige Drikkevarer':
            g_otemp.find('prodgroupex').text = ""

    tree.write(catalog_file, pretty_print=True, encoding = 'Windows-1252')

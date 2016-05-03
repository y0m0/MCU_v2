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

    tree = etree.parse(catalog_file)
    root = tree.getroot()

    for g_otemp in root.findall('g_otemp'):
        storeid = g_otemp.find('storeid').text
        prodtype = g_otemp.find('prodtype').text
        prodname = g_otemp.find('desc').text.lower()

    # search for products to be removed from the catalog
        if storeid != '1' or prodtype == '(Ingen)' or prodtype == 'Div. bestillingsvarer' or 'oluf' in prodname:
            root.remove(g_otemp)


    tree.write(catalog_file, pretty_print=True, encoding = 'Windows-1252')

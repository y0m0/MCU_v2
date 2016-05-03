#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# apply_discounts.py
#

from itertools import imap
from lxml import etree


class Item(object):
    def __init__(self, el):
        self.elem = el
        self.d = {x.tag: x for x in el}

    def __getattr__(self, key):
        return getattr(self.d, key)


def custom(catalog_file, discount_file, output_file):
    """
    returns a new catalog file (output_file)
    by modifying product prices inside the catalog file
    based on the values taken from the discount file
    """

    roots = (etree.fromstring(catalog_file),)
    ret = etree.Element(roots[0].tag)

    disroot = etree.fromstring(discount_file)
    items = imap(Item, disroot)
    disdict = {x.get('prodid').text: x for x in items
               if x.get('prodid') is not None and x.get('newprice') is not None}

    prodid_seen = set()

    for root in roots:
        for el in imap(Item, root):
            prod_id = el.get('prodid').text.strip()
            if prod_id and prod_id not in prodid_seen:
                if prod_id in disdict:
                    if disdict[prod_id].get('price').text != '0.0000':
                        el.get('prod_priceout').text = disdict[prod_id].get('price').text
                    else:
                        el.get('prod_priceout').text = disdict[prod_id].get('newprice').text
                else:
                    if el.get('prodtype').text != 'Alkoholholdige Drikkevarer':
                        el.get('prod_priceout').text = '%0.4f' % (
                            float(el.get('prod_priceout').text) * 0.88)
                prodid_seen.add(prod_id)
                ret.append(el.elem)

    output_file.write(etree.tostring(ret, pretty_print = True,
        #encoding = 'ASCII'  # This outputs html entities for ascii chars > 127 (for instance &#248;)
        encoding = 'Windows-1252'  # This outputs the original char even for ascii > 127
        ))


def twelve_percent(catalog_file, output_file):
    """
    returns a new catalog file by applying
    a flat 12% discount on all the products,
    but leaving unmodified the ones falling under
    the category "alkoholholdige drikkevarer"
    """

    roots = (etree.fromstring(catalog_file),)
    ret = etree.Element(roots[0].tag)

    prodid_seen = set()

    for root in roots:
        for el in imap(Item, root):
            prod_id = el.get('prodid').text.strip()
            if prod_id and prod_id not in prodid_seen:
                if el.get('prodtype').text != 'Alkoholholdige Drikkevarer':
                    el.get('prod_priceout').text = '%0.4f' % (
                        float(el.get('prod_priceout').text) * 0.88)
                prodid_seen.add(prod_id)
                ret.append(el.elem)

    output_file.write(etree.tostring(ret, pretty_print=True,
        #encoding = 'ASCII'  # This outputs html entities for ascii chars > 127 (for instance &#248;)
        encoding='Windows-1252'  # This outputs the original char even for ascii > 127
        ))





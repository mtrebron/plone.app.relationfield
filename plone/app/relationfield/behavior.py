# -*- coding: utf-8 -*-
from plone.app.dexterity import _
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives as form
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope.interface import provider
from zope import schema

@provider(IFormFieldProvider)
class IRelatedItems(model.Schema):
    """Behavior interface to make a Dexterity type support related items.
    """

    relatedItems = RelationList(
        title=_(u'label_related_items', default=u'Related Items'),
        default=[],
        value_type=RelationChoice(
            title=u'Related', vocabulary='plone.app.vocabularies.Catalog'
        ),
        required=False,
    )
    relation_caption = schema.TextLine(
        title=_(u'label_relation_caption', default=u'Provide an optional caption for the Related Items'),
        required=False,
        default=u''
    )
    form.widget(
        'relatedItems',
        RelatedItemsFieldWidget,
        vocabulary='plone.app.vocabularies.Catalog',
        pattern_options={
            'recentlyUsed': True  # Just turn on. Config in plone.app.widgets.
        },
    )

    fieldset(
        'categorization', label=_(u'Categorization'), fields=['relatedItems', 'relation_caption']
    )

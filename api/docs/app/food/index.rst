Приложение ``food``
===================

Примеры запросов:
"""""""""""""""""

.. code-block:: python

    Все категории продуктов:

    query{
      foodCategories{
        id,
        nameRu,
        nameEn,
        nameCh
        foods{
          id,
          nameRu,
          internalCode,
          code,
          cost,
          additional{
            id
          }
          descriptionRu,
          descriptionEn,
          descriptionCh
          isVegan,
          isSpecial,
          isPublish,

        }
      }
    }


Описание структуры graphql запросов приложения:
"""""""""""""""""""""""""""""""""""""""""""""""
.. toctree::
   :maxdepth: 2

   schema/queries.rst

Описание контроллеров приложения:
"""""""""""""""""""""""""""""""""
.. toctree::
   :maxdepth: 2

   views.rst

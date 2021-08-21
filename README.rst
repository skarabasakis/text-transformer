================
Text Transformer
================

Text transformer is a toy application that transforms text in various fun ways:

- **silence:** Remove all the vowels
- **leetify:** Convert to `leetspeak <https://en.wikipedia.org/wiki/Leet>`_
- **ransomize:** Randomly mix uppercase and lowercase letters for a `ransom note <https://en.wikipedia.org/wiki/Ransom_note_effect>`_ effect
- **jumble:** Shuffle the middle letters of all words, like in the popular `typoglycemia <https://en.wikipedia.org/wiki/Typoglycemia>`_ internet meme

Text transformer implements three distinct frontends:

- a command line interface
    .. image:: https://user-images.githubusercontent.com/142385/130324879-f5ae8164-23fb-4466-94ae-4f4c1743946a.png
       :width: 480px
- a tkinter GUI (``--tkui``)
    .. image:: https://user-images.githubusercontent.com/142385/130325439-32cec00f-9032-4072-9fd8-fc6ba14d762b.png
       :width: 480px
- a browser-based GUI (``--webui``)
    .. image:: https://user-images.githubusercontent.com/142385/130325599-71c758fc-5d93-4d24-ae0b-e406f8c3c52a.png
       :width: 480px

Local development setup
-----------------------
Requirements
^^^^^^^^^^^^
- Python 3.9 with tkinter
- Poetry 1.x

Setup instructions
^^^^^^^^^^^^^^^^^^
#. Clone the project
#. Install dependencies: ``poetry install``
#. Activate virtualenv: ``poetry shell``

# Project_Graph_citation


PubMed est connu pour être le principal moteur de recherche de données bibliographiques dans le domaine de la biologie et de la médecine. Il a été développé par le Centre américain pour les informations biotechnologiques (NCBI), et est hébergé par la Bibliothèque américaine de médecine.
Cet entrepôt bibliographique est un moteur de recherche gratuit donnant accès à la base de données bibliographique MEDLINE, rassemblant des citations et des résumés d'articles de recherche biomédicale.
Ainsi, l’objectif principal de ce projet sera de générer des graphes de citations pour un ensemble d'articles et par la suite d'analyser ces graphes.
Pour cela, la génération d’un script va devoir être générer afin de pouvoir extraire les données et de part, utiliser Gephi pour visualiser l’ensemble des citations et les relations existantes entre- elles.

# executable
Afin de faciliter l’utilisation du code par des utilisateurs quelconques, un package informatique a été développé. Différentes méthodes dans ce package permettrons une analyse appronfondie des besoins.

### Create object Usage :
>>> from PythonProject import ExtractCitation >>> objctExtract = ExtractCitation ()
### retrievePubmedNotice usage:
>>> objctExtract.retrievePubmedNotice()
### getPmidMedelieCitation usage :
>>> objctExtract.getPmidMedelieCitation(xmlFile)
### getPmidCommentCorrectionList usage :
>>> objctExtract.getPmidCommentCorrectionList(xmlFile)
### getPmidCommentCorrectionListCiter usage :
>>> objctExtract.getPmidCommentCorrectionListCiter(xmlFile)
### getArticlesCitedBy usage :
>>> objctExtract.getArticlesCitedBy(pmid)
### listArticlesCorpusPmid usage :
>>> objctExtract.listArticlesCorpusPmid()
### articlesInGraph usage :
>>> objctExtract.articlesInGraph()
### articleIsFromOriginalCorpus usage :
>>> objctExtract.articleIsFromOriginalCorpus()
### arcticle_max_citation usage :
>>> objctExtract.arcticle_max_citation()
### article_cite_by
>>> objctExtract. article_cite_by()
### max_ArticlesCitedBy_citate
>>> objctExtract. max_ArticlesCitedBy_citate()
### trieArticleCitationMax
>>> objctExtract.trieArticleCitationMax()
### generateGraph
>>> objctExtract.trieArticleCitationMax()

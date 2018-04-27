#! /usr/bin/env python
# coding:UTF8
#----Library-----#
import pickle
import time
import sys
import os
import networkx as nx
import xml.dom.minidom
pythonVersion = sys.version_info[0] # Verification de la version de python
if pythonVersion < 3 :
    import urllib # on utilise cette librairie si version python 2
else :
    import urllib.request # on utilise cette librairie si version python 3


class ExtractCitation (object) :

    #-----------------------------CONSTANTE-------------------------------
    DATA_DIR = "data"
    TOPIC = "-metabolicNetworkReconstruction"
    PYTHON_VERSION = sys.version_info[0]
    PUBMED_URL = "http://www.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?rettype=xml&retmode=xml&db=pubmed&id="
    PATH = "DirPubMedFile"

    def __init__(self) :
        self.dataDir = self.__class__.DATA_DIR + self.__class__.TOPIC + "/"
        self.pmidList = []
        self.delaySeconds = 1

    def retrievePubmedNotice (self) :
        with open("corpus" + self.__class__.TOPIC + ".txt") as pmidListFile :
            try :
                os.makedirs(self.__class__.PATH)
            except OSError :
                if not os.path.isdir (self.__class__.PATH):
                    raise
            os.chdir(self.__class__.PATH)
            for currentLine in pmidListFile :
                pmid = currentLine.replace("\n", "") # On retire le saut de ligne
                self.pmidList.append(pmid)
                if self.__class__.PYTHON_VERSION < 3 :
                    pubmedFile = urllib.urlopen (self.__class__.PUBMED_URL + pmid)
                    destFile = open (self.__class__.DATA_DIR + pmid + ".xml", "w")
                else :
                    pubmedFile = urllib.request.urlopen(self.__class__.PUBMED_URL + pmid)
                    destFile = open(self.__class__.DATA_DIR + pmid + ".xml", "wb")
                destFile.write(pubmedFile.read())
                destFile.close()
                if self.delaySeconds > 0 :
                    time.sleep(self.delaySeconds)
        with open('../pmidList' + self.__class__.TOPIC + '.pkl', 'wb') as output:
            pickle.dump(self.pmidList, output)

    def getPmidMedelieCitation(self, xmlFile) :
        """
        Méthode permettant d'afficher le PMIDs de l'aticle à partir de
        l'onglet xml MedlineCitation

        Args:
            xml_filepath: a str object for the xml filepath.

        PARAMS output:
            -void
        """
        try :
            os.chdir(self.__class__.PATH)
        except OSError :
            if not os.path.isdir (self.__class__.PATH):
                os.chdir("../" + self.__class__.PATH)
        domArticle = xml.dom.minidom.parse(xmlFile)
        domArticle = xml.dom.minidom.parse(xmlFile)
        MedlineElt = domArticle.getElementsByTagName("MedlineCitation")
        for currentElt in MedlineElt :
            medlineValue = ""
            medllineValueList = currentElt.getElementsByTagName("PMID")
            medlineValueElt = medllineValueList[0]
            medlineValue = medlineValueElt.childNodes[0].data
        return(medlineValue)

    def getPmidCommentCorrectionList (self, xmlFile) :
        """
        Méthode permettant d'afficher le PMIDs dans l'onglet xml
        CommentsCorrectionsList

        Args:
            xml_filepath: a str object for the xml filepath.

        PARAMS output:
                - void
        """
        try :
            os.chdir(self.__class__.PATH)
        except OSError :
            if not os.path.isdir (self.__class__.PATH):
                os.chdir("../" + self.__class__.PATH)
        domArticle = xml.dom.minidom.parse(xmlFile)
        domArticle = xml.dom.minidom.parse(xmlFile)
        MedlineElt = domArticle.getElementsByTagName("CommentsCorrectionsList")
        for currentElt in MedlineElt :
            medlineValue = ""
            medllineValueList = currentElt.getElementsByTagName("PMID")
            medlineValueElt = medllineValueList[0]
            medlineValue = medlineValueElt.childNodes[0].data
            print(medlineValue)

    def getPmidCommentCorrectionListCiter (self, xmlFile) :
        """
        Méthode permettant d'afficher les PMIDs dans les elements
        CommentsCorrections de CommentsCorrectionsList.

        Args:
            xml_filepath: a str object for the xml filepath.

        PARAMS output:
            - void
        """
        try :
            os.chdir(self.__class__.PATH)
        except OSError :
            if not os.path.isdir (self.__class__.PATH):
                os.chdir("../" + self.__class__.PATH)
        commentsCorrectionsList = domArticle.getElementsByTagName("CommentsCorrectionsList")

        domArticle = xml.dom.minidom.parse(xmlFile)
        if (commentsCorrectionsList == 1) :
            for element in commentsCorrectionsList :
                element = element.getElementsByTagName ("CommentsCorrections")
                for pmid in element :
                    PMID = pmid.getElementsByTagName("PMID")
                    print (PMID[0].firstChild.nodeValue)

    def getArticlesCitedBy(self, pmid) :
        """
        Méthode pemettant de renvoyer une liste des PMID des articles cité
        par PMID.
        Recherche de la notice XML dans le bon répertoire, le lit et renvoie la
        liste eventuellement vide des articles cités.

        Args:
            xml_filepath: a str object for the xml filepath.

        PARAMS output:
            listPmidCite : list[]
        """
        try :
            os.chdir(self.__class__.PATH)
        except OSError :
            if not os.path.isdir (self.__class__.PATH):
                os.chdir("../" + self.__class__.PATH)

        dataFile = (self.__class__.DATA_DIR + pmid + ".xml")
        #print (dataFile)
        #print (os.getcwd())

        try:
            domArticle = xml.dom.minidom.parse(dataFile)
        except:
            return

        listPmidCite = []
        PMID_Elts = domArticle.getElementsByTagName("PMID")
        if ((PMID_Elts.length)>=1):
        #print (domArticle)
            commentsCorrectionsList = domArticle.getElementsByTagName("CommentsCorrectionsList")
            if ((commentsCorrectionsList.length)==1) :
                for element in commentsCorrectionsList :
                    element = element.getElementsByTagName ("CommentsCorrections")
                    for pmid in element :
                        PMID = pmid.getElementsByTagName("PMID")
                        #print (PMID[0].firstChild.nodeValue)
                        try :
                            listPmidCite.append(PMID[0].firstChild.nodeValue)
                        except:
                            pass
        return (listPmidCite)

    def listArticlesCorpusPmid (self) :
        """
        Méthode pemettant de renvoyer une liste des PMID des articles du corpus
        Args:
            None

        PARAMS output:
            articlesCorpus : list()
        """

        try :
            os.path.isfile("corpus-metabolicNetworkReconstruction.txt")
        except OSError :
            if not os.path.isfile("corpus-metabolicNetworkReconstruction.txt"):
                os.chdir("..")

        corpus_file = open(r"corpus-metabolicNetworkReconstruction.txt", "r")
        contenu = corpus_file.readlines()
        corpus_file.close()

        articlesCorpus = []
        for ligne in contenu:
            #print ligne
            articlesCorpus.append(str(ligne.rstrip('\n')))
        return (articlesCorpus)

    def dictArticleCites (self) :
        """
        Méthode pemettant de renvoyer un dictionnaire dont les clefs sont des
        PMID du corpus et la valeur correspondant a la liste des PMID des articles
        cité par la clef

        Args:
            None

        PARAMS output:
            articlesCorpus : list()
        """

        dict_article_cite = dict()
        articleCorpus = self.listArticlesCorpusPmid()
        #print (articleCorpus)

        for element in articleCorpus:
            #print (element)
            #print (self.getArticlesCitedBy(element))
            dict_article_cite[element] = self.getArticlesCitedBy(element)
        return (dict_article_cite)

    def articlesInGraph (self) :
        """
        Méthode permettant de renvoyer une liste contenant les PMIDs des articles
        intervenant dans le graphe de citation c'est à dire celles présente dans
        le corpus ansi que celle cité.
        On fera également attention aux doublons.

        Args:
            None

        PARAMS output:
            articlesCorpus : list()
        """
        articleIngraph = []
        articleCorpus = self.listArticlesCorpusPmid()
        articleCitee = self.dictArticleCites()

        if (len (articleCorpus) > 0):
            for element in articleCorpus :
                if element not in articleIngraph :
                    try :
                        articleIngraph.append(element)
                    except :
                        pass

        elif (len (articleCitee) > 0) :
            for eltInDict in articleCitee :
                for eltsValue in articleCitee[eltInDict]:
                    if eltsValue not in articleIngraph :
                        try :
                            articleIngraph.append(eltsValue)
                        except TypeError :
                            pass
        return (articleIngraph)

    def articleIsFromOriginalCorpus (self) :
        """
        Méthode permettant de renvoyer un dictionnaire dont les clefs sont les
        PMID des articles du graphe et la valeur est un boléen associé à chaque
        clef. On associe True s'il s’agit d’un artice du corpus d’origine sinon
        False.

        Args:
            None

        PARAMS output:
            articlesCorpus : dict()
        """

        dictPmidOriginal = {}
        articleIngraph = self.articlesInGraph()
        try :
            articleCorpus = self.listArticlesCorpusPmid()
        except :
            os.chdir("..")
            articleCorpus = self.listArticlesCorpusPmid()

        for elts in articleIngraph :
            if elts in articleCorpus :
                dictPmidOriginal[elts] = True
            else :
                dictPmidOriginal[elts] = False
        return (dictPmidOriginal)

    def arcticle_max_citation (self) :
        dictArtCite = self.dictArticleCites()

        maxCitation = 0
        AticleMaxCitation = None

        for key, value in dictArtCite.items() :
            if (len(value) > maxCitation) :
                maxCitation = len (value)
                AticleMaxCitation = key
            else :
                pass
        return (AticleMaxCitation)

    def article_cite_by (self) :
        """
        Méthode permettant de creer un dictionnaire dont les clefs sont les PMID
        des articles du corpus graphe, et la valeur associé à chaque clef est la
        liste (éventuellement vide) des articles qui citent la clef.
        Args:
            None

        PARAMS output:
            dictArticlesCitedBy : dict()
        """
        try :
            articleInsideGraph = self.articlesInGraph()
        except IOError :
            os.chdir("..")
            articleInsideGraph = self.articlesInGraph()
        dictArticlesCitedBy = dict()
        for element in articleInsideGraph:
            dictArticlesCitedBy[element] = self.getArticlesCitedBy(element)
        return(dictArticlesCitedBy)

    def max_ArticlesCitedBy_citate (self) :
        """
        méthode permettant de trouver l'article contenant le plus de citation

        Args:
            None

        PARAMS output:
            pmid_du_max_citation : variable

        """
        max_ArticlesCitedBy_citation=0
        pmid_du_max_citation=None

        try :
            dictArticle = self.article_cite_by()
        except IOError :
            os.chdir("..")
            dictArticle = self.article_cite_by()

        for cle,valeur in dictArticle.items():

            if len(valeur) > max_ArticlesCitedBy_citation:
                max_ArticlesCitedBy_citation= len(valeur)
                pmid_du_max_citation =cle
            else :
                pass
        return (pmid_du_max_citation)

    def trieArticleCitationMax (self) :
        """
        Méthode permettant de trier les articles par nombre décroissant de citations.

        Args:
            None

        PARAMS output:
            items : dict()
        """
        newDict = {}
        newDictSorted = {}
        try :
            dictArticle = self.article_cite_by()
        except IOError :
            os.chdir("..")
            dictArticle = self.article_cite_by()
        for cle,valeur in dictArticle.items():
            newDict[cle] = len(valeur)
        items = newDict.items()
        comparateur = lambda a,b : cmp(a[1],b[1])
        return sorted(items, comparateur, reverse=True)

    def generateGraph (self) :
        """
        Utilisation de la librairy networkx, afin de créer les graphes de citation

        Args:
            None

        PARAMS output:
            file : graph_total_citation.gexf
        """
        G=nx.DiGraph()
        try :
            dictArticle = self.article_cite_by()
        except IOError :
            os.chdir("..")
            dictArticle = self.article_cite_by()

        for cle,valeur in dictArticle.items():
            G.add_node(cle)
            if not valeur == None:
                for element in valeur:
                    if not valeur == None:
                        G.add_edge(cle,element)
                    else:
                        pass
        os.chdir("..")
        nx.write_gexf(G, "./graph_total_citation.gexf", encoding='utf-8',
              prettyprint=True, version='1.1draft')

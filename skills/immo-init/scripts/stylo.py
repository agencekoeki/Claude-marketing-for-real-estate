#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stylométrie de la mallette — mesure, ne juge pas. Aucune bibliothèque externe.

  profil  <corpus> [--registre NOM]        → la signature mesurée d'un registre, en markdown daté
  compare <brouillon> <voix.md> [--registre NOM] → les écarts d'un brouillon avec cette signature

<corpus> : un fichier texte, ou un dossier de .txt / .md. Un registre = un corpus homogène :
mails aux vendeurs, mails aux acquéreurs, publications, annonces, messages à Claude.
Sous 2 000 mots, le script le dit : la signature est fragile.

Mesuré : mots-outils (taux et sur-représentation par rapport au français écrit courant),
phrases (moyenne, écart, courtes, longues), paragraphes, ponctuation, ouvertures, clôtures,
richesse, habitudes de caractère — et surtout ce qu'il ne fait JAMAIS, qui est la contrainte
la plus sûre. Jamais les mots du sujet.
"""
import sys, os, re, math, datetime, collections

_BRUT = """le la les l de des du d un une et ou mais donc car or ni que qu qui quoi dont où
je tu il elle on nous vous ils elles ce c cet cette ces ça cela mon ma mes ton ta tes son sa ses
notre votre nos vos leur leurs y en à au aux dans par pour sur sous avec sans chez vers entre
très bien plus moins aussi alors ainsi enfin puis là voilà voici bref sinon quand comme si
tout tous toute toutes déjà encore jamais toujours peu beaucoup trop assez vraiment juste
justement effectivement franchement d'ailleurs pourtant cependant d'abord ensuite après avant
surtout même seulement ok oui non merci bonjour""".split()
MOTS_OUTILS=[w for w in _BRUT if w not in ("coup","fait","final","contre","que")]
MULTI=["du coup","en fait","au final","par contre","parce que","c'est-à-dire","à la limite","en tout cas"]
# français écrit courant, pour 1 000 mots — ordres de grandeur, pas une norme
BASE={"de":42,"la":24,"le":22,"et":20,"à":18,"les":17,"des":13,"en":11,"un":10,"une":9,"que":11,"qui":7,
      "pour":6,"dans":6,"il":6,"est":6,"ce":5,"je":4,"vous":3,"on":2,"nous":2,"mais":3,"ou":2,"donc":1,
      "très":1,"bien":2,"plus":3,"aussi":1,"alors":1,"voilà":0.3,"du coup":0.2,"en fait":0.4,"bref":0.1,
      "ok":0.1,"ça":1.5,"cela":0.6,"vraiment":0.4,"juste":0.5,"d'ailleurs":0.3,"par contre":0.2}
PONCT={",":"virgule",";":"point-virgule",":":"deux-points","!":"exclamation","?":"interrogation",
       "…":"points de suspension","...":"trois points","(":"parenthèse","—":"tiret cadratin","«":"guillemets français",'"':"guillemets droits"}
MOIS=datetime.date.today().strftime("%Y-%m")

def lire(chemin):
    docs=[]
    if os.path.isdir(chemin):
        for f in sorted(os.listdir(chemin)):
            if f.endswith((".txt",".md")):
                t=open(os.path.join(chemin,f),encoding="utf-8",errors="ignore").read()
                docs.append(re.sub(r"^---.*?---\s*","",t,flags=re.S))
    else: docs=[open(chemin,encoding="utf-8",errors="ignore").read()]
    return [d for d in docs if d.strip()]

def phrases(t):
    t=re.sub(r"\s+"," ",t)
    return [p.strip() for p in re.split(r"(?<=[.!?…])\s+",t) if len(p.strip().split())>=2]

def mots(t):
    t=t.lower().replace("’","'")
    t=re.sub(r"\b([ldjcqnstm]|qu|jusqu|lorsqu|puisqu)'",r"\1 ",t)
    return re.findall(r"[a-zàâäéèêëîïôöùûüç'-]+",t)

def mesurer(docs):
    texte="\n\n".join(docs); ws=mots(texte); ph=[len(mots(p)) for p in phrases(texte)]; n=max(len(ws),1); nc=max(len(texte),1)
    r={"mots":len(ws),"docs":len(docs)}
    if len(ws)<2000: r["avertissement"]=f"corpus de {len(ws)} mots : sous 2 000, la signature est fragile"
    if ph:
        m=sum(ph)/len(ph); v=math.sqrt(sum((x-m)**2 for x in ph)/len(ph))
        r["phrase"]=(round(m,1),round(v,1),round(100*sum(1 for x in ph if x<=8)/len(ph)),round(100*sum(1 for x in ph if x>=25)/len(ph)))
    paras=[len(mots(p)) for d in docs for p in re.split(r"\n\s*\n",d) if mots(p)]
    r["para"]=round(sum(paras)/len(paras),1) if paras else 0
    r["ponct"]={}
    for sym,nom in PONCT.items():
        c=texte.count(sym) if sym!="..." else len(re.findall(r"(?<!\.)\.\.\.(?!\.)",texte))
        r["ponct"][nom]=round(1000*c/nc,1)
    r["exclam_ph"]=round(texte.count("!")/max(len(ph),1),2); r["quest_ph"]=round(texte.count("?")/max(len(ph),1),2)
    cnt=collections.Counter(ws); tl=texte.lower()
    fo={w:round(1000*cnt[w]/n,1) for w in MOTS_OUTILS if cnt[w]}
    for m_ in MULTI:
        c=len(re.findall(r"\b"+re.escape(m_)+r"\b",tl))
        if c: fo[m_]=round(1000*c/n,1)
    r["outils"]=dict(sorted(fo.items(),key=lambda kv:-kv[1])[:20])
    sur=[]
    for w,v in fo.items():
        b=BASE.get(w)
        if b and v>=2.5*b and cnt.get(w,0)+len(re.findall(r"\b"+re.escape(w)+r"\b",tl))>=5: sur.append((w,v,b))
    r["sur"]=sorted(sur,key=lambda x:-x[1]/x[2])[:8]
    prem=ws[:1000]; r["richesse"]=round(len(set(prem))/max(len(prem),1),2)
    r["ouv"]=[o for o,_ in collections.Counter(" ".join(mots(d.strip().split("\n")[0])[:3]) for d in docs).most_common(3) if o]
    r["clo"]=[c for c,_ in collections.Counter(d.strip().split("\n")[-1].strip()[:40].lower() for d in docs).most_common(3) if c]
    r["maj"]=round(1000*sum(1 for c in texte if c.isupper())/nc,1)
    r["emoji"]=len(re.findall(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]",texte))
    r["nbsp"]=len(re.findall(r"\u00a0[!?:;]",texte)); r["esp_avant"]=len(re.findall(r" [!?:;]",texte)); r["colle"]=len(re.findall(r"\w[!?:;]",texte))
    r["ca_sans_cedille"]=len(re.findall(r"\bca\b",tl)); r["maj_accent"]=len(re.findall(r"\b(?:É|È|À|Ê)\w",texte)); r["maj_sans_accent"]=len(re.findall(r"\b(?:Etat|Ecole|Eglise|Etage|Equipe|A) ",texte))
    r["debuts"]=[d for d,_ in collections.Counter(" ".join(mots(p)[:2]) for p in phrases(texte)).most_common(5)]
    jam=[nom for nom,v in r["ponct"].items() if v==0 and nom in ("exclamation","tiret cadratin","points de suspension","trois points","point-virgule","guillemets français","parenthèse")]
    if r["emoji"]==0: jam.append("emoji")
    if r["nbsp"]==0 and r["esp_avant"]==0: jam.append("espace avant ? ! : ;")
    if r["exclam_ph"]==0 and "exclamation" not in jam: jam.append("phrase exclamative")
    r["jamais"]=jam
    return r

def carte(r,registre):
    L=[f"### Registre : {registre}",f"- [vu {MOIS}] mesuré sur {r['docs']} texte(s), {r['mots']} mots"]
    if "avertissement" in r: L.append(f"- [vu {MOIS}] {r['avertissement']}")
    if "phrase" in r:
        m,v,c,l=r["phrase"]; L.append(f"- [vu {MOIS}] phrases : {m} mots en moyenne, écart {v} · {c} % de courtes (≤ 8), {l} % de longues (≥ 25)")
    L.append(f"- [vu {MOIS}] paragraphes : {r['para']} mots en moyenne")
    L.append(f"- [vu {MOIS}] ponctuation pour 1 000 caractères : "+" · ".join(f"{k} {v}" for k,v in r["ponct"].items()))
    L.append(f"- [vu {MOIS}] {r['exclam_ph']} exclamation par phrase · {r['quest_ph']} question par phrase")
    L.append(f"- [vu {MOIS}] mots-outils pour 1 000 mots : "+" · ".join(f"{w} {v}" for w,v in r["outils"].items()))
    if r["sur"]: L.append(f"- [vu {MOIS}] sur-représentés par rapport au français courant : "+" · ".join(f"{w} ({v} contre {b})" for w,v,b in r["sur"]))
    L.append(f"- [vu {MOIS}] débuts de phrase les plus fréquents : "+" · ".join(f"« {d} »" for d in r["debuts"]))
    L.append(f"- [vu {MOIS}] richesse du vocabulaire sur 1 000 mots : {r['richesse']}")
    if r["ouv"]: L.append(f"- [vu {MOIS}] ouvertures : "+" · ".join(f"« {o} »" for o in r["ouv"]))
    if r["clo"]: L.append(f"- [vu {MOIS}] clôtures : "+" · ".join(f"« {c} »" for c in r["clo"]))
    L.append(f"- [vu {MOIS}] habitudes de caractère : majuscules {r['maj']} pour 1 000 · emoji {r['emoji']} · espace insécable avant ponctuation {r['nbsp']} · espace simple {r['esp_avant']} · collé {r['colle']} · « ca » sans cédille {r['ca_sans_cedille']} · majuscules accentuées {r['maj_accent']}, non accentuées {r['maj_sans_accent']}")
    L.append(f"- [vu {MOIS}] **jamais** : "+(" · ".join(r["jamais"]) if r["jamais"] else "rien d'absent — tout apparaît au moins une fois"))
    return "\n".join(L)

def lire_carte(voix,registre):
    t=open(voix,encoding="utf-8").read()
    blocs=re.split(r"^### Registre : ",t,flags=re.M)
    cible=None
    for b in blocs[1:]:
        nom=b.split("\n",1)[0].strip()
        if registre is None or nom.lower()==registre.lower(): cible=b; break
    if cible is None: return None,None
    r={}
    m=re.search(r"phrases : ([\d.]+) mots en moyenne, écart ([\d.]+)",cible)
    if m: r["phrase"]=(float(m.group(1)),float(m.group(2)))
    m=re.search(r"ponctuation pour 1 000 caractères : ([^\n]+)",cible)
    if m: r["ponct"]={k.strip():float(v) for k,v in re.findall(r"([a-zé' -]+?) ([\d.]+)",m.group(1))}
    m=re.search(r"mots-outils pour 1 000 mots : ([^\n]+)",cible)
    if m: r["outils"]={w.strip():float(v) for w,v in re.findall(r"([a-zàâäéèêëîïôöùûüç' -]+?) ([\d.]+)",m.group(1))}
    m=re.search(r"\*\*jamais\*\* : ([^\n]+)",cible)
    r["jamais"]=[x.strip() for x in m.group(1).split("·")] if m and "rien d'absent" not in m.group(1) else []
    return r,cible.split("\n",1)[0].strip()

def comparer(brouillon,voix,registre):
    ref,nom=lire_carte(voix,registre)
    if not ref: print(f"ATTENTION voix.md ne porte pas de signature mesurée"+(f" pour le registre « {registre} »" if registre else "")+" — lance « profil » d'abord."); return 1
    r=mesurer([open(brouillon,encoding="utf-8").read()]); ec=[]
    print(f"registre comparé : {nom}")
    for j in ref["jamais"]:
        if j=="emoji" and r["emoji"]>0: ec.append("emoji : il n'en met jamais")
        elif j=="espace avant ? ! : ;" and (r["nbsp"]+r["esp_avant"])>0: ec.append("espace avant ? ! : ; — il n'en met jamais, typographie trop parfaite")
        elif j=="phrase exclamative" and r["exclam_ph"]>0: ec.append("exclamation : il n'en met jamais")
        elif j in r["ponct"] and r["ponct"][j]>0: ec.append(f"{j} : il n'en met jamais, le brouillon en a")
    if "phrase" in ref and "phrase" in r:
        m,v=ref["phrase"]; a,b=r["phrase"][0],r["phrase"][1]
        if abs(a-m)>max(4,0.35*m): ec.append(f"phrases de {a} mots contre {m} chez lui")
        if v>0 and b<0.5*v and r["mots"]>=80: ec.append(f"phrases trop régulières : écart {b} contre {v} chez lui — signature d'outil")
    for nom_p,val in ref.get("ponct",{}).items():
        a=r["ponct"].get(nom_p,0)
        if val>0 and a>2.5*val and a>1: ec.append(f"{nom_p} : {a} contre {val} pour 1 000 caractères chez lui")
    if r["mots"]>=80:
        for w,v in list(ref.get("outils",{}).items())[:6]:
            if v>=15 and r["outils"].get(w,0)==0: ec.append(f"« {w} » : il l'emploie sans arrêt, le brouillon jamais")
    if not ec: print("OK        le brouillon est dans sa signature."); return 0
    for e in ec: print(f"ATTENTION {e}")
    return 1

if __name__=="__main__":
    a=sys.argv[1:]; reg=None
    if "--registre" in a:
        i=a.index("--registre"); reg=a[i+1]; a=a[:i]+a[i+2:]
    if len(a)>=2 and a[0]=="profil": print(carte(mesurer(lire(a[1])),reg or "global")); sys.exit(0)
    if len(a)>=3 and a[0]=="compare": sys.exit(comparer(a[1],a[2],reg))
    print(__doc__); sys.exit(2)

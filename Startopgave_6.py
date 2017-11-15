
# Naam: Ariel Komen
# Datum: 18-10-2017 
# Versie: 1

# Voel je vrij om de variabelen/functies andere namen te geven als je die logischer vind.

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.

def main():
    bestand = "/home/cole/Downloads/GCF_000164845.2_Vicugna_pacos-2.0.2_rna.fna" # Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand
    enzymen_bestand = open ("enzymen.txt")
    enzymenlijst = []
    for regel in enzymen_bestand:
        enzymenlijst.append(regel)
    """
    Hier onder vind je de aanroep van de lees_inhoud functie, die gebruikt maakt van de bestand variabele als argument.
    De resultaten van de functie, de lijst met headers en de lijst met sequenties, sla je op deze manier op in twee losse resultaten.
    """
    combi = lees_inhoud(bestand)

    fastanummer = 0 # op welke positie zit het restricie-enzym? een tellertje die dat verteld
    teller = 0 # deze teller verteld uiteindelijk het totaal aantal hits
        
    zoekwoord = input("Geef een zoekwoord op: ")

    # Ga door alle fasta elementen heen
    for fasta in combi:
        fastanummer +=1
        # Kijk wat we hier hebben
        header = fasta[0]
        sequentie = fasta[1]

        # Conditie 1: is de header okee?
        if header.find(zoekwoord) <0:
            # Het zoekwoord zit niet in de header...
            continue

        # Conditie 2: Is dit dna??
        if is_dna(sequentie):
            # YES het is dna...

            # Conditie 3: knipt dit voor een restrictie-enzym?
            enzymen = knipt(sequentie, enzymenlijst)
            if enzymen != "":
                # We hebben er eentje!!
                print(fastanummer, header, enzymen)
                teller += 1
                
    
    #print(headers)
    #print("-"*80)
    #print(seqs)
    # schrijf hier de rest van de code nodig om de aanroepen te doen
    
    #gevonden = is_dna(seqs)

    #print(gevonden)
    # We zijn klaar
    print("Alles is verwerkt, er zijn zoveel hits:", teller)
    
def lees_inhoud(bestands_naam):
    bestand = open(bestands_naam)
    # headers = []
    # seqs = []
    combi = []

    for regel in bestand:
       if regel.startswith(">"):
           # seqs.append(regel.strip())
           fasta = []
           fasta.append(regel.strip())
       else:
           # headers.append(regel.strip())
           # Plaats de sequentie in lijst fasta
           fasta.append(regel.strip())
           # Plaats het fastalijstje in combi
           combi.append(fasta)

    return combi

    """
    Schrijf hier je eigen code die het bestand inleest en deze splitst in headers en sequenties.
    Lever twee lijsten op:
        - headers = [] met daarin alle headers
        - seqs = [] met daarin alle sequenties behorend bij de headers
    Hieronder vind je de return nodig om deze twee lijsten op te leveren
    """
   
    
def is_dna(sequentie):
    
    
    gevonden = (sequentie.count("M") == 0)
    return gevonden
    
    """
    Deze functie bepaald of de sequentie (een element uit seqs) DNA is.
    Indien ja, return True
    Zo niet, return False
    """
    

def knipt(sequentie, enzymenlijst):


    sEnzymen = ""
    for regel in enzymenlijst:                  #een loopje die het bestand doorleest
        enzym, seq = regel.split()              #het enzym wordt gescheiden  van de regel
        seq = seq.replace("^","")               #het dakje wordt vervangen door niets 
        if sequentie.find(seq) >= 0:            #hier moet ik ervoor zorgen dat het programma met "seq" over de sequenties heen ittereerd
            # Deze seq zit in sequentie
            sEnzymen += enzym + " "
                                                #en als er een hit is, wordt het enzym door gestuurd naar de main() functie                                
    return sEnzymen                                 
    """
    Bij deze functie kan je een deel van de code die je de afgelopen 2 afvinkopdrachten geschreven hebt herbruiken

    Deze functie bepaald of een restrictie enzym in de sequentie (een element uit seqs) knipt.
    Hiervoor mag je kiezen wat je returnt, of wellicht wil je alleen maar printjes maken.
    """
       
    
main()
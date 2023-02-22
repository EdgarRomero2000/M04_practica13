from animal import animal
from vehicle import vehicle
from school import school
from book import book
from user import user
from university import university

#Cridem l'objecte animal
Huma = animal("Mamiferos","Homo Sapiens Sapiens",2,True,"Sexual",1.7)
Huma.salutacio()
Kiwi = animal("Aves","Apterygidae Apteryx",2,True,"Sexual",0.35)
Kiwi.salutacio()
Huma.setTamany(2.0)
Huma.salutacio()
Kiwi.setReproducio("Asexual")
Kiwi.salutacio()

#Cridem l'objecte vehicle
McLaren = vehicle(2,"McLaren",100000,2,1.5,4)
McLaren.salutacio()
Renault = vehicle(4,"Renault",15000,5,3,4)
Renault.salutacio()
McLaren.setPreu(300000)
McLaren.salutacio()
Renault.setRodes(3)
Renault.setPortes(2)
Renault.setSeients(2)
Renault.salutacio()

#Cridem l'objecte school
Lestonnac = school("Bachillerat","Ciencies","Concertada",True,False,"Barcelona")
Lestonnac.salutacio()
Baguette = school("Secundaria","Sin especializacion","Publico",False,True,"Narvona")
Baguette.salutacio()
Lestonnac.setFinanciacio("Privat")
Lestonnac.salutacio()
Baguette.setExtraescolars(False)
Baguette.salutacio()

Libro1 = book(2013,"La casa de Hades","Rick Riordan","Aventura i fantasia",500000,"Dura")
Libro1.info()
Libro2 = book(2014,"La sangre del olimpo","Rick Riordan","Aventura i fantasia",600000,"Dura")
Libro2.info()
Libro1.setTapa("Blanda")
Libro1.info()
Libro2.setTapa("Blanda")
Libro2.info()

User1 = user("Pedro","Lopez","Mcmillan",378948,"Home",2003)
User1.salutacio()
User2 = user("Maria","Lopez","Hadesito",378348,"Dona",2005)
User2.salutacio()
User1.setNom("Pablo")
User1.salutacio()
User2.setNom("Franco")
User2.salutacio()

Uni1 = university("Harvard","Espanya",500000,"Medicina",300,"No")
Uni1.info()
Uni2 = university("Cambridge","Italia",10,"Ingenieria",1000,"Si")
Uni2.info()
Uni1.setPreu(20)
Uni1.info()
Uni2.setPreu(59000)
Uni2.info()